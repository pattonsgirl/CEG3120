Day 1:
- Syllabus
- Install Docker (likely Docker Desktop), recommend git and vscode
- run `docker` and `docker run -d -p 80:80 docker/getting-started` to validate install

Day 2:
- What is `docker run -d -p 80:80 docker/getting-started`
- `docker ps`, `docker ps -a`, `docker images`
- Docker Hub
- `docker pull busybox`
- `docker run -it busybox`

Day 3:
- `chroot`
- copying required files for `bash`
- https://github.com/pattonsgirl/CEG3120/blob/main/CourseNotes/container-exercises.md
- what would it take to build a git server?
    - hardware
    - OS
    - git
    - networking
    - what are good questions to ask?
- picking a base image
    - comfort?
    - function?
- in-dev requirements vs. in-production
- breaking down `git@github.com:pattonsgirl/CEG2350.git`
- start a container with ubuntu, make a git user

Day 4:
- starting and connecting to an exited container
- fixing git user
- installing git
- ssh?
