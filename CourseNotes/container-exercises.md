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

The general rules of thumb:
1. Pick an `image` from an image repository that aligns with your project / application needs
    - when considering, pick the software that is most intensive to install
2. `run` container from image - choose if you want to start attached (`-it`) or detached (`-d`)
3. Determine what else you need
    - Project files (share or copy?)
    - Additional dependencies / package installs
4. Create an `image` once the dust has settled
    - `Dockerfile`s give you a way to "code" this up
5. Run containers using your `image` & share your `image` with systems that have container engines

## Make a `python` environment

### Option 1: Full DIY
1. Pick a base image, like `ubuntu`, because it's an environment you are used to with `apt` and `vim`, etc.
2. `run` container from image with `-it`
    - update package repo
    - install python version
    - insert python code (create file, add code)
    - exit running container - OR - try Ctrl + Q to detach?
        - `ctrl + shift + q` worked for me to detach but leave running
        - Can set using `--detach-keys="ctrl-x"`
3. `exec` to execute code using `python` interpreter

Downsides: 
- What if a package needs updating?
- What if code needs updating?  
    - is git a reasonable thing within a container?
- How do others know how to execute code?
    - training people in many tools is a headache, and leads to errors, and errors lead to the ~~dark side~~ downtime 

### Option 2: Pick a good base
1. What options does DockerHub have for `python`?
    - Now updates to `python` can be handled by pulling new base
    - [DockerHub python image](https://hub.docker.com/_/python)
2. `run` container from image - what are you in?
    - by default, you are in a python interpreter
    - you could specify `bash` at end of run command to enter bash shell
3. Copy code into container either by
    - detach and use `docker cp`
    - create a bind mount to share a file / folder between host and container
4. `exec` to execute code using `python` interpreter

```
# Copy - copy host folder / file to container filesytem
docker run -d --name pyproj python:3
docker cp /home/kduncan/pyproj pyproj:/
```

```
# Bind mount - share host folder with container filesystem / folder
docker run -it -v /home/kduncan/pyproj:/code python:3 python /code/code.py
# OR
docker run -d -v /home/kduncan/pyproj:/code --name pyproj python:3
docker exec pyproj python /code/code.py
```

Downsides:
- Python libraries still need updating within container
- Still need to remember how to execute code
- What if you "overshare"?

### Option 3: Build an image with `Dockerfile`
A `Dockerfile` will allow us to create a "recipe" for how an image should be built for and to run our project / app
- `FROM` will specify an image from an image repository (`python:3`)
- `COPY` will allow us to copy in folder from host to container (`pyproj` to `/code`)
- `RUN` will run prep commands for our environment (`pip install requirements.txt`)
- `CMD` will specify the command to kick off our application (`python /code/code.py`)

## Make a hello-world container

1. Compile a c / c++ program
    - Statically link libraries: `gcc -o program main.c --static`
        - [more on static linking](https://dev.to/iamkhalil42/all-you-need-to-know-about-c-static-libraries-1o0b)
2. Copy into container (`scratch`?)
    - run container as detached
    - `cp` file into container
    - `exec` to see files in container
        - no `ls` if using `scratch`
3. Run program
    - `exec` code

Wouldn't it be great if the container could have an image where this was already copied?  `Dockerfile` to the rescue!

## Use port binding

Containers can be used to run web applications and other applications that bind (listen) to ports.  Since containers are isolated, networking is part of that isolation.

If a container has an application listening on a port, in `docker` you can bind that port to a host port.  The host will then forward requests to it's port to the container's port, and the application in the container will respond.

### `getting-started`

`docker run -d -p 80:80 docker/getting-started`  

- Starts container from image `docker/getting-started`
- `image` is set to start default task of application that serves web content over port 80 (internal to container network)
- `-p 80:80` binds internal port to host port 80
- Content requests to any valid IP that refers to host on port 80 are forwarded to container port 80
    - `localhost:80` OR `127.0.0.1:80`
    - `private_ip:80` if on private subnet (like WSU-Secure or home network)
    - `public_ip:80` if system is associated with a public IP (like EIP attached to instance)

### Docker Curriculum - flask app

[Docker Curriculum](https://docker-curriculum.com/) has great tutorials overall, but one I like to play with is their flask application.

```
# clone the repo
$ git clone https://github.com/prakhar1989/docker-curriculum.git
# go into the folder
$ cd docker-curriculum/flask-app
```
The application folder contains things:
- `Dockerfile` - instructions to build an image from contents of this folder
- `app.py` - the python application set to run flask and do things (the code)
- `requirements.txt` file with a list of python libraries and specific versions for this project
- `templates` folder with default `index.html` page

Build an image for this project using: `docker build -t demo .`

Run a container using: `docker run -d -p 8080:5000 demo`

How can you see it?
- attach to container?
- host IP?

# Build container image with `Dockerfile`

Look at `Dockerfile`s that build images we have used
- [`Dockerfile`](https://github.com/docker-library/hello-world/blob/master/Dockerfile.build) for [`hello-world`](https://hub.docker.com/_/hello-world/)

# Use a container image repository

1. Create an account on [hub.docker.com](https://hub.docker.com/)
2. Create a repository (one per project)
    - Discuss pros / cons of free accounts on DockerHub
3. Discuss types of account credentials
    - username + password
    - username + token
4. Use `docker login` on command line to provide credentials to access repositories
5. Tag `image`s with `dockerhub_username`/`image`:`version`
6. `push` images to `dockerhub`
7. Discuss: 
    - What does this mean for sharing images?
    - What does this mean for running containers from images?
    - What steps remain complex?
