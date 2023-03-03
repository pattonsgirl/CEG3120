# Containers

Objectives of this module:
- understand what a container is
- understand what a container solves
- use the essential container management commands
- build container images from a `Dockerfile`
- use a container image repository for your images

You are going to see two container managers focused on in this document: Docker and Podman.  My feeling is Podman is gaining traction (for good reasons), so I want to create a document that covers both and does a bit of compare and contrast.  

You may have heard of Singularity - Singularity is another container manager that works well for High Performance Computing.  You'll hear more about it in our HPC focused courses.  The good news is a lot of the core overlaps - the differences between Singularity, Docker, and Podman lie at a lower level.

You will see a lot of references to [Ivan Velichko's blog](https://iximiuz.com/) because it is great - he makes solid tutorials, dives into the inner workings, and his diagrams and something I aspire to create.

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

Now you can have a bit more respect for what a container manager handles.

### History of Containers

Containers aren't new, but they have exploded in popularity.  Kubernetes was a bit of a game changer.  While being aware of the history of containers isn't required, it is a good conversation in the evolution of features and usability.

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

## Running Containers 101

### pull

### images

### run

- `-it`
- `-d`
- `-p`
    - `HOST_PORT:CONTAINER_PORT`
- `-name`
- `--rm`
- `-v`
    - mount `host_folder:container_folder`

### stop

### kill

### ps

### rm

### image rm

### exec

### attach

- [iximiuz - attach vs exec](https://iximiuz.com/en/posts/containers-101-attach-vs-exec/)

## Building Container Images

### `Dockerfile`

### `.dockerignore`

### build

- `-t`

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

### push

## Things to Think On

- This is too many commands to get wrong
    - Manageable for one system and just you.  How about 50 systems?
- Scripting is an answer, but all scripts need to stay synced
- Where does this need to build?
- How do you update the systems the container is running on?

## Other Articles

- [RedHat - podman + systemd & starting on boot](https://www.redhat.com/sysadmin/container-systemd-persist-reboot)

## Blogs to Follow

If you, like me, think containers are the bees knees, here is a list of who I follow:
- [Ivan Velichko's blog](https://iximiuz.com/)
- [aqua](https://blog.aquasec.com/)
