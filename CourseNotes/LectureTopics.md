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
    - docker `start` and `attach` (to PID 1 of container), `exec` (after started) to spawn a completely new separate process inside the container.
- fixing git user
    - the woes of using `useradd`, review of permissions
        - `rwx`, user, group, other
        - `chmod`, `chown`, `chgrp`
- cleaning up
    - docker `rm` for container processes, `rmi` for container images

Day 5:
- installing git
    - what's with `apt`?
    - note the additional packages - one of them is `openssh-client`
- installing / configuring ssh
    - `apt install openssh-server`
    - `ssh-keygen`
    - client
        - `known_hosts`
        - `config`
    - server
        - `authorized_keys`
    - `sshd` vs `ssh` (server program vs client)
        - service
        - process

- sidebar - paste in vim in container shell
    1. In Vim, press Esc to ensure you are in Normal mode.
    2. Type the following command and hit `Enter`: `:set mouse=`

Day 6:

- `init` a git repo
- get `sshd` running
    - starting and checking service status
        - mentioning `systemctl`
        - focusing on `service`
    - concept: will need this to be the **foreground** process
- docker `export` vs `import`
- port binds
    - `-p` host:container

Day 7:
- `init` a git repo
    - existing / new project locally 
    - just a git tracking dir, not a working dir - `--bare`
- Configuring the `config` file
- Dockerfile
    - templating what we built for a DIY git server

Day 8:

- sketch out Dockerfile based on how we built diy git container
- Dockerfile
    - `FROM`, `RUN`, `COPY`, `CMD`, `WORKDIR`
- building an image from a Dockerfile
    - `docker build -t image_name:tag .` - the `.` sets build context (what files it has access to)
- setting the default process (`sshd`)
    - we aren't controlling a service - instead we are setting sshd (the ssh server) as the foreground process
    - `/usr/sbin/sshd -D`
- run a container process from image built by dockerfile - profit?

Day 9:

- DockerHub & `docker login`
    - Personal Access Tokens (name, longevity, appropriate rights)
- `tag` original / source to new name
    - If for DockerHub, remember repo ref must be included (`wsukduncan/repo_name:tag`)
- `push` an image
- AWS invites
- AWS - easy mode
    - grab a template - https://wsu-cecs-cf-templates.s3.us-east-2.amazonaws.com/course-templates/ceg2350.yml
    - build a stack
    - sign in
        - default private key (vockey) is available for download through AWS Details
    - ssh in

Day 10:

- AWS outage for instructor account - talked through concepts, no live demos
- install docker on OS (Ubuntu)
    - https://docs.docker.com/engine/install/ubuntu/
    - Post installation: https://docs.docker.com/engine/install/linux-postinstall/
- `pull` an image
    - consequences of private (must log in, even to pull) vs public repos
- IaaS, PaaS, SaaS - course will focus on AWS concepts in IaaS tools (VPC, EC2, CloudFormation)
- AWS concepts, ref https://github.com/pattonsgirl/CEG3120/blob/main/CourseNotes/AWS-VPC-EC2.md
    - review networking - specifically subnets and CIDR notation
    - VPC
    - Subnets (private and public)
    - Route table (for each subnet)
    - Internet Gateway

Day 11:

- Sent invites to `ceg3120-aws-NAME-f26` repos
- Build VPC, subnets, Internet Gateway, and route tables in AWS
- Security: **Network** Access Control List (NACL)
    - Inbound and outbound control
    - Allow or deny control
    - Rules apply in order (first match wins - pay attention to rule numbering)
    - Can set whitelist or blacklist perspective
    - Rules apply to associated subnets (across the whole subnet network)
    - STATELESS
- Security: Security Groups
    - allow only
    - can control Inbound and Outbound
    - associated with an instance / resource, which is on a subnet (subnet has NACL & route table)
    - whitelist by default (no rule, not allowed in)
    - STATEFUL

Day 12:

- Security Groups vs NACLs
    - stateful vs stateless
- instance creation
    - AMI
    - instance types
    - key pairs
        - if create - one time prompt to download private key
        - if `vockey` - private key is accessible in AWS Details tab

Day 13:

- Finish instance creation
    - network configuration
    - volume selection
- Talk through security example

Day 14:

- CloudFormation templates
