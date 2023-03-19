# Containers

Objectives of this module:
- understand what a container is
- understand what a container solves
- use the essential container management commands
- build container images from a `Dockerfile`
- use a container image repository for your images

## What is a Container?

The [Open Container Initiative - OCI](https://opencontainers.org/) defines a standard container as having these features:

- Containers are isolated and restricted boxes for running processes
- Containers pack an app and all its dependencies (including OS libs) together
- Containers are for portability - any compliant runtime can run a bundle
    - any container created on one system can run on any other system (laptop to cloud)
- Containers can be implemented using Linux, Windows, and other OS-es
- Virtual Machines also can be used as standard containers

Resources:
- [btholt - What are Containers?](https://btholt.github.io/complete-intro-to-containers/what-are-containers)
- [Rancher by suse - An Introduction to Containers](https://www.suse.com/c/rancher_blog/an-introduction-to-containers/)

### Tools that Containers Use

- `chroot`
    - allows you to set the root directory of a new process
    - [play with chroot](https://btholt.github.io/complete-intro-to-containers/chroot)
- PID namespaces / `unshare`
    - allow you to hide processes from other processes
    - [play with namespaces + chroot](https://btholt.github.io/complete-intro-to-containers/namespaces)
- control groups / `cgroup`
    - allow control of hardware resources to a process
    - "this isolated environment only gets so much CPU, so much memory, etc. and once it's out of those it's out-of-luck, it won't get any more."
    - [play with cgroups + namespaces + chroot](https://btholt.github.io/complete-intro-to-containers/cgroups)
- network namespaces / `nsenter`
    - logically another copy of the network stack, with its own routes, firewall rules, and network devices
    - [create a network namespace](https://iximiuz.com/en/posts/container-networking-is-simple/)
- user namespaces
    - separate the user IDs and group IDs between the host and containers
        - the idea here is if you spin up a process, you own it, and the process has the rights you have
        - if a container is started by `root`, and `root` is the user in the container, if an exploit is found and "they" escape the container, "they" have `root` on the host system
        - instead, you want rights in the container to have no mapping outside the container
    - [podman and user namespaces](https://medium.com/techbull/what-is-user-namespace-and-podmans-rootless-containers-fc4c292c6bad)

Now you can have a bit more respect for what a container manager handles.

More great articles:
- [nginx - What are namespaces & cgroups](https://www.nginx.com/blog/what-are-namespaces-cgroups-how-do-they-work)

### History of Containers

Containers aren't new, but they have exploded in popularity.  Docker and, later, Kubernetes were game changers in their times.  While being aware of the history of containers isn't required, it is a good conversation in the evolution of features and usability.

- [Aqua - Brief History of Containers](https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016)
- [RedHat - History of Containers](https://www.redhat.com/en/blog/history-containers)

## Container Managers

A container manager manages the complete container lifecycle on a single host: creates, starts, stops containers, pulls and stores images, configures mounts, networking, etc.

Some container managers:
- [Docker](https://www.docker.com/)
- [Podman](https://podman.io/)
- [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html)
- [containerd](https://containerd.io/)
    - needs a client on top (`ctr`, `nerdctl`, `crictl`)
        - [want to play?](https://iximiuz.com/en/posts/containerd-command-line-clients/)
    - lots of managers run this under the hood
- [LXD + LXC](https://linuxcontainers.org/)

If you really want to get elbow deep in how the managers manage, you can [follow this blog series](https://iximiuz.com/en/series/implementing-container-manager/) to implement your own.

You are going to see two container managers focused on in this document: Docker and Podman.  My feeling is Podman is gaining traction (for good reasons), so I want to create a document that covers both and does a bit of compare and contrast.  


### Docker

- Windows
    - have WSL2 (Hyper-V may be enough)
    - [install Docker Desktop](https://docs.docker.com/desktop/windows/wsl/)
- Linux
    - [install docker or Docker Desktop](https://docs.docker.com/desktop/install/linux-install/)
- Mac w/ Intel Chip: 
    - [install Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
- Mac w/ Silicon Chip (M1 & M2): 
    - [install Rosetta 2, then install Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)

### Podman

- Windows
    - have WSL2
    - (assuming Ubuntu) `apt install podman`
- Mac
    - unknown support for Silicon Chip
    - [install Homebrew](https://brew.sh/)
    - `brew install podman`
- Linux
    - (assuming Ubuntu) `apt install podman`

### Docker vs Podman

You are about to find out that Docker tries to be an all in one ecosystem.  Podman only manages containers.  There are separate tools that do other tasks, such as `buildah` for building images, and `skopeo` to inspect images.  [This article from RedHat](http://redhatgov.io/workshops/rhel_8/exercise1.8/) looks at putting those different tools to use.

The core differences between Docker and Podman lie in how they manage the containers as processes (and is beyond the scope of this class).  The resources below do great deep dives:

- [lambdatest - Podman vs Docker](https://www.lambdatest.com/blog/podman-vs-docker/)
- [Smart Home Beginner - Podman vs Docker](https://www.smarthomebeginner.com/podman-vs-docker/)

## Running Containers 101

### pull
Download an image from a remote repository.  If no `tag` is given, `latest` is assumed
- `docker pull image:tag` (assumes DockerHub as registry) 
- `docker pull registry/username/image:tag`
- `podman pull registry/username/image:tag`

- [iximiuz - Run a container without an image](https://iximiuz.com/en/posts/you-dont-need-an-image-to-run-a-container/)

### images
List all local images
- `docker images`
- `podman images`

### run
Create and run a container based on the given image
- `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
    - [more on docker run](https://docs.docker.com/engine/reference/commandline/run/)
- `podman run --rm -it [--name name] image:tag command`
    - [more on podman run](https://docs.podman.io/en/latest/markdown/podman-run.1.html)

- `-it`
    - `-t` allocates a pseudo-tty and attach to the standard input of the container
    - `-i` (interactive) keep stdin open even if not attached
- `-d`
    - run the container in the background (detached)
- `-p HOST_PORT:CONTAINER_PORT`
    - expose container port to host port
    - if a container (even stopped) has a port bound on the host, it cannot be rebound until the container is removed
    - If host IP is set to `0.0.0.0` or not set at all, the port will be bound on all IPs on the host.
- `--name container_name`
    - assign a name (alias to container ID)
- `--rm`
    - remove container after it exits (main process completes)
- `-v host_folder:container_folder`
    - creates bind mount host and container.  This is also referred to as a map

### ps
List the running containers on the system (use `--all` or `-a` to include non-running containers)
- `docker ps`
- `podman ps`

### stop
Stop a running container gracefully.  Sends `SIGTERM` to main process within container, sends `SIGKILL` after 10 seconds.
- `docker stop container_id`
- `podman stop container_id`

### start
Start a container
- `docker start container_id`
- `podman start container_id`

### kill
Send a kill signal to running container
- `docker kill container_id`
- `podman kill container_id`

### rm
Remove a container.  Use `-f` to force (`stop`/`kill` + `rm`)
- `docker rm container_id`
- `podman rm container_id`

### rmi
Remove a local image from local cache.  Use `-f` to force
- `docker rmi image:tag` 
- `podman rmi image:tag`

### exec
Run a command in an existing container
- `docker exec container_id command`
- `podman exec container_id command`

### attach
Attach `stdin`,`stdout`, `stderr` to a running container. Helpful if container is detached and you have a need to see live logs.
- `docker attach container_id`
- `podman attach container_id`

- [iximiuz - attach vs exec](https://iximiuz.com/en/posts/containers-101-attach-vs-exec/)

## Building Container Images

Container images are build using containers - a container is spun up, built to spec, then saved to an image.

### `Dockerfile`
Container manager can build images automatically by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image

- [btholt - Intro to Dockerfiles](https://btholt.github.io/complete-intro-to-containers/dockerfile)
- [Docker Curriculum - Dockerfile](https://docker-curriculum.com/#dockerfile)
- [Docker - Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

```
# Specify base image
FROM python:3.8

# set a directory for the app within container
WORKDIR /usr/src/app

# copy all the files to the container
# this states copy all files in host current working directory
#    to container working directory (recall WORKDIR)
COPY . .

# install dependencies
# RUN instructions are executed at image build, not container start
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
# What program should run in the foreground when container is started from image
CMD ["python", "./app.py"]
```

### `.dockerignore`
File in which you can specify ignore rules and exceptions from these rules for files and folder, that won’t be included in the build context and thus won’t be packed into an archive and uploaded to the Docker server.
- [codefresh.io - Do not ignore `.dockerignore`](https://codefresh.io/blog/not-ignore-dockerignore-2/)

### build
Build and `tag` an image from a `Dockerfile` in the current working directory
- `docker build -t <image_name>`
- `podman build -t image:tag .`

### `commit` and `tag` `image`

There are instances where you may not have a `Dockerfile` to work with, but the filesystem within the container needs content updated.  An option is to go through the following steps:

- `start` container from base image
- [`cp` (copy)](https://adamtheautomator.com/docker-cp/) content into container or `attach` and modify content
- `detach` and create a `commit` (snapshot) of the container
- the `commit` created an `image`
- `tag` the image by ID or `tag` during the `commit`

[Steps based on DataSet blog - create docker image](https://www.dataset.com/blog/create-docker-image/)

### `export` and `import`

`commit` and `tag` an image from a running container is one strategy - another is to export the filesystem from the container.

[`docker export`](https://docs.docker.com/engine/reference/commandline/export/) exports a container’s filesystem as a tar archive

[docker import`](https://docs.docker.com/engine/reference/commandline/import/) imports the contents from a tarball to create a filesystem image

## Sharing Container Images

### Container Image Registry

The following is a short list of container registries for which you can have an account and push / pull your own images to / from.

How do you pick?  This [article from RedHat](https://www.redhat.com/en/topics/cloud-native-apps/what-is-a-container-registry) has a good overview of the pieces involved.  If you are just goofing off, DockerHub gets the job done.  Once you need to worry about authentication / authorization restrictions, workflows with other software, etc., then you start investigating the pros and cons of each.

- [DockerHub](https://hub.docker.com/)
- [Quay](https://quay.io/)
- [AWS Elastic Container Registry](https://aws.amazon.com/ecr/)
    - requires AWS IAM credentials to be awesome
- [Google Container Registry](https://cloud.google.com/container-registry)
- [Microsoft Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

### login
Log in to the remote repository (to push / pull to protected registries).  In class we will discuss password authentication versus token based authentication.
- `docker login -u <username>` (assumes login to DockerHub)
- `podman login registryURL -u username [-p password]`

### push
Push a local image to a remote repository
- `docker push <username>/<image_name>` (assumes DockerHub)
- `podman push registry/username/image:tag`

## Things to Think On

- This is too many commands to get wrong
    - Manageable for one system and just you.  How about 50 systems?
- Scripting is an answer, but all scripts need to stay synced
- Where does this need to build?
- How do you update the systems the container is running on?

## Cheat sheets

- [DockerLabs - Docker Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)
- [Mike Polinowski - Podman Cheat Sheet](https://mpolinowski.github.io/docs/DevOps/Linux/2019-09-25--podman-cheat-sheet/2019-09-25)

## Curiosity Articles

- [RedHat - podman + systemd & starting on boot](https://www.redhat.com/sysadmin/container-systemd-persist-reboot)
- [Bauldung - docker attach and detach container](https://www.baeldung.com/ops/docker-attach-detach-container)

## Blogs to Follow

If you, like me, think containers are the bees knees, here is a list of who I follow:
- [Ivan Velichko's blog](https://iximiuz.com/)
- [aqua](https://blog.aquasec.com/)
