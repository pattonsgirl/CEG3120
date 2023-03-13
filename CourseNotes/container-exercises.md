# Play with what containers are made of

1. Collect binaries and libraries of binaries that are essential to working in a directory
2. `chroot` into the folder
    - issues:
        - `chroot` just means separate starting point
        - still has access to process control
        - is `root`!  Can kill processes on system, and cause mayhem

There must be something better... could we start with a base?
1. `debootstrap` https://wiki.debian.org/Debootstrap
    - we are bootstrapping Debian in order to get that base set of binaries and libraries
2. Now we can `unshare` - this will lock it to its own process space

# Run a container image

`docker run hello-world`  
- What is this command?
    - The `docker run` command first creates a writeable container layer over the specified `image`, and then `start`s it using the specified command.
- What does it do?
    - Runs a container from the image `hello-world`
    - If you read the output from the container running it's task:
```
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```
- Where did it come from?
    - If it is not on your system, the image is searched for on DockerHub and the imaging matching that name is downloaded ([the `hello-world` image](https://hub.docker.com/_/hello-world))

`docker run -d -p 80:80 docker/getting-started`  
- What is this command?
    - the `-d` flag detaches the container and prints the container ID
    - if you run a container from the `hello-world` image with `-d`, you won't see the output, but it will still run
    - the `-p` flag **binds** / **publishes** the container’s port(s) to the host
    - since no IP was specified, the port bind is valid for any IP on the host (localhost, private IP, public IP)
- What does it do?
    - hosts a getting started web tutorial
    - you can access it on your host via `127.0.0.1` (localhost) or private IP or (if associated with the host) public IP
- Where did it come from?
    - [docker/getting-started](https://hub.docker.com/r/docker/getting-started)

`docker run -it busybox` (or `scratch`)  
- What is this command?
    - the `-it` gives `shell` access (if a shell exists) and allow standard input / output feed to your terminal
- What does it do?
    - `scratch` is the base-most image you can build a container from
    - `busybox` provides core GNU `fileutils` and `shellutils` and nothing else.  No package manger either.  But it is super light weight is all you need is core tools
- Where did it come from?
    - [`scratch`](https://hub.docker.com/_/scratch)
    - [`busybox`](https://hub.docker.com/_/busybox)

`docker run -it ubuntu` (or `archlinux` or `alpine`)  
- What is this command?
    - if a shell exists in the filesystem of the image, runs it in the foreground
- What does it do?
    - `alpine` is built from `busybox` and has a package manager
    - `ubuntu` image comes with all tools available in a Ubuntu distribution
    - `archlinux` image comes with all tools available to an Arch distribution
    - Why `ubuntu` or `archlinux` or any other distro?  What if all you needed from a distro was the files inside?  You'll be running these on top of the Linux kernel of the host
- Where did it come from?
    - [`alpine`](https://hub.docker.com/_/alpine)
    - [`ubuntu`](https://hub.docker.com/_/ubuntu)
    - [`archlinux`](https://hub.docker.com/_/archlinux)

`docker run -it busybox ls /bin`
- What does it do?
    - runs the command `ls /bin` in a container from a `busybox` image

`docker run -it --rm busybox ls /bin`
- What does it do?
    - `--rm` removes the container after it exists

`docker run -it --name lister busybox ls /bin`
- What does it do?
    - `--name` names the container `lister` and aliases it to the container id

https://iximiuz.com/en/posts/not-every-container-has-an-operating-system-inside/ 


# Play with containers

## Make your own hello-world
1. Compile a c / c++ program
2. Copy into container (scratch?)
    - run container as detached
    - cp file into container
3. Run program
    - exec code

Wouldn't it be great if the container could have an image where this was already copied?  `Dockerfile` to the rescue!

Play with detaching from container  
`$ docker attach --sig-proxy=false test_redis`  
`$ docker attach --detach-keys="ctrl-x" test_redis`

https://www.baeldung.com/ops/docker-attach-detach-container

# Mount from host to container

# Use port forwarding

- cat site
- https://docker-curriculum.com/#our-first-image
```
$ git clone https://github.com/prakhar1989/docker-curriculum.git
$ cd docker-curriculum/flask-app
```
# Build container image with Dockerfile

Look at Dockerfiles that build images we have used

# Use a container image repository

# Discuss limitations