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

## Hello World!
`docker run hello-world`  
- What is this command?
- What does it do?
- Where did it come from?

`docker run -d -p 80:80 docker/getting-started`  
- What is this command?
- What does it do?
- Where did it come from?

`docker run -it alpine`  
- What is this command?
- What does it do?
- Where did it come from?

`docker run -it ubuntu`  
- What is this command?
- What does it do?
- Where did it come from?

# Make your own hello-world

## Using something compiled
1. Compile a c / c++ program
2. Copy into container (scratch?)
    - run container as detached
    - cp file into container
3. Run program
    - exec code

Wouldn't it be great if the container could have an image where this was already copied?  `Dockerfile` to the rescue!

https://iximiuz.com/en/posts/not-every-container-has-an-operating-system-inside/ 

# Explore container images

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