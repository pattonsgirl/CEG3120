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
        - https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html
- AWS Regions and Availability Zones
    - https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ 
    - If logged in, can use this view: https://us-east-1.console.aws.amazon.com/awsglobalview/home?region=us-east-1#RegionsAndZones:tabId=lz 
- Sign in to your AWS instance
- Talk through security example

Day 14:

- CloudFormation templates
- https://github.com/pattonsgirl/CEG3120/blob/main/CourseNotes/AWS-CF-Breakdown.md

Day 15:

- CloudFormation - debugging strategies
- Infrastructure Compose for template validation
    - This catches bad / misspelled fields and formatting errors in json / yml - not value validity
- Compiling and reading errors during stack build

Day 16:

- CloudFormation - debugging instances / script
- `journalctl` / cloud log
    - **`/var/log/cloud-init-output.log`**: This is the most critical file for UserData troubleshooting. It captures all standard output (stdout) and standard error (stderr) generated by your shell scripts or #cloud-config directives.
    - `/var/log/cloud-init.log`: Contains the internal, verbose cloud-init process events and cloud provider metadata retrieval details.

```yml
            #!/bin/bash -xe
            apt-get update && \
            apt-get install -y \
              git \
              bloop && \
            echo "This is from the CF template" > /home/ubuntu/hello.txt && \
            reboot
```

```yml
            #!/bin/bash -xe
            apt-get update 
            apt-get install -y 
              git 
              htop 
              sl 
            echo "This is from the CF template" > /home/ubuntu/hello.txt
            reboot
```

```yml
            #!/bin/bash -xe
            apt-get update && \
            apt-get install -y \
              git \
              htop \
              sl && \
            hostnamectl set-hostname wheeeee && \
            reboot
```

Day 17:

- Testing and breaking connectivity at NACL & SG Layer
- `nslookup` - domains only (`wttr.in`), not protocols (`https://wttr.in`)
    - if googling "ips for domain" be careful - they might be a DNS resolver!
- Demo one: NACL inbound, denying `5.9.243.187`
- Demo two: `ping` uses ICMP - why can't I `ping 34.198.162.255` from the instance? Toying with Security Groups and stateful resolution

Day 18:

- Docker bind mounts & volumes
- create something silly:
    - `echo "<h1>Keep It Simple</h1>" > index.html`
- have html content, want a container with a web serving service
    - https://hub.docker.com/_/nginx
- COPY
    - may use `docker cp`
    - going to focus on `Dockerfile` `COPY` instruction
- Bind mount 
    - bind folder / file on host to folder / file in container
    - `docker run -d --name bind -p 8082:80 -v "$(pwd)/site":/usr/share/nginx/html nginx:alpine`
    - note that if container is removed, host files are not effected
- Volume - persistent storage
    - `docker volume create webdata`
    - `docker run -d --name vol1 -p 8083:80 -v webdata:/usr/share/nginx/html nginx:alpine`
    - volumes are seeded from images contents
    - `docker exec vol1 sh -c 'echo "<h1>Volume data</h1>" > /usr/share/nginx/html/index.html'`
    - `docker run -d --name vol2 -p 8084:80 -v webdata:/usr/share/nginx/html nginx:alpine`
    - To remove the data, you need to remove the volume: `docker volume rm webdata`
    - usually in combo with docker compose files
- Reflect: what's best when?
    - COPY - container files isolated from host. Changes do not persist
    - Bind mount - container files bound to host. Changes persist
    - Volume - data needs to stay persistent across container. Changes persist
        - mainly seen when dealing with databases
        - AI models don't favor this - preference for bind mounts as data usually also needs accessibility from host

Day 19:

- NAT Gateway
- configuring a private subnet
- Early concept: how / why do companies set up load balancers
- Q: How we will connect to the instance on the private subnet?

Day 20:

- Midterm exam

Day 21:

- Upcoming project tools
    - HAProxy for load balancing: https://www.haproxy.org/
    - Web server using nginx or apache containers:
        - https://hub.docker.com/_/nginx
        - https://hub.docker.com/_/httpd
        - *Optional rabbit hole* https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations
    - Web content for web server
        - use old HTML site with two static pages and some image files
        - use AI to generate on topic of choice
            - keep it appropriate
            - SITE how you generated it
            - EXPLAIN what it does
- Resources in zones continuing issue - would recommend building in alternative zones inside us-east-1 such as us-east-1a, us-east-1b, us-east-1c, or us-east-1d via your subnet configuration
- Building NAT Gateway and configuring the private subnet
    - NEW: NAT Gateways now "auto-configure" - allocating an EIP for themselves & associating with the public subnet
- Configure private route table to point external traffic to NAT Gateway
- Adding an instance to the private subnet
- SG interference

Day 22:

- When does an instance need public network access?
- Load balancing - vocab lesson
- Load balancing - strategies
- https://github.com/pattonsgirl/CEG3120/blob/main/CourseNotes/load-balancers.md


Day 23:

- Project 5: recommend getting website running in container & outlining what systems will go where - intent & design
    - https://github.com/pattonsgirl/CEG3120/tree/main/Projects/Project5
- Two subnets - public and private. One instance on public, will run proxy. Three on private, EIP through NAT Gateway
- HAProxy will run the proxying service on the proxy server
- Docker container running on hosts in pool on private subnet
- 4 HAProxy sections - https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration
    - global
    - defaults
    - frontend
    - backend
- load balancing algorithms
    - https://www.haproxy.com/glossary/what-are-load-balancing-algorithms
- health checks
    - TCP tests (think ping)
    - HTTP checks - request based on status codes: https://www.iana.org/assignments/http-status-codes
- cookies
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies

Day 24:

- Layer 4 (TCP mode) versus Layer 7 (HTTP mode): https://www.haproxy.com/blog/layer-4-and-layer-7-proxy-mode

| Feature | `mode tcp` (Layer 4) | `mode http` (Layer 7) |
|---|---|---|
| **OSI Layer** | Layer 4 (Transport) | Layer 7 (Application) |
| **Inspection Depth** | Looks only at IP addresses and ports. | Inspects URLs, HTTP headers, cookies, and body. |
| **Performance** | Extremely fast and lightweight; lower CPU overhead. | Higher CPU usage due to parsing full text streams. |
| **SSL/TLS Handling** | Passes encrypted traffic straight to backend (SSL Passthrough). | Decrypts and encrypts traffic (SSL Termination). |
| **Routing Decisions** | Based strictly on destination IP, port, or SNI (Server Name Indication). | Based on URL paths, request methods, domain headers, etc. |
| **Modifications** | Cannot alter the payload or inject headers. | Can inject headers (e.g., X-Forwarded-For), alter cookies, or compress data. |

- Load Balancing algorithms: https://www.youtube.com/watch?v=dBmxNsS3BGE
- Enabling stats: https://www.haproxy.com/blog/exploring-the-haproxy-stats-page
    - Ex: ip:8404/stats

Day 25:

- [AWS Calculator (no account)](https://calculator.aws/#/addService?trk=e8c13544-17d6-4cc0-abab-a4348449de09&sc_channel=ps&ef_id=Cj0KCQjwlsfWBhD4ARIsACL7p1FwMZYGx4m91RpBA7DT22Jsyivj6sc39YdRBj1gdwiHrGSZdzDcLGQaAsgHEALw_wcB:G:s&gads_camp=23532472510&gads_ag=199502799824&gads_ad=795877020713&gads_kw=aws&gads_matchtype=p&gads_network=g&gads_device=c&gads_geo=9015845&gad_source=1&gad_campaignid=24281356734&gbraid=0AAAAADjHtp-hFBhEhKRiaL_DgGsQWqddV&gclid=Cj0KCQjwlsfWBhD4ARIsACL7p1FwMZYGx4m91RpBA7DT22Jsyivj6sc39YdRBj1gdwiHrGSZdzDcLGQaAsgHEALw_wcB)
- Blackholes (post deleting NAT Gateway)
- Super simple test traffic - https://github.com/rakyll/hey
- Strategies to perform scalability tests:
    - number of requests; longevity of high load requests
    - Which language (stack) can handle the most users?: https://www.youtube.com/watch?v=sQXFhh_PiG4&list=WL&index=100&t=1s
- Side topic: testing resiliency
    - Netflix's Chaos Monkey: https://netflix.github.io/chaosmonkey/Outage-checker/
- Session persistence
    - Persistence profiles: https://www.youtube.com/watch?v=5yFXd38C9ZQ
        - source IP: client IP noted, requests go to same server
            - ineffective for dynamic IPs or NAT
        - cookie-based: LB puts cookie in client's browser with session identifier
            - better for dynamic IPs
        - server-inserted: app server (host) puts cookie in response, LB uses cookie for persistence
    - This is separate from AUTH!: https://www.youtube.com/watch?v=iX8g4LqF8p8

Day 26: 

- Demo

Day 27 / 28 / 29:

A detour into monitoring services & docker compose files

- Prometheus Node Exporter
    - install on each server / node you want to monitor
        - Don't forget NAT Gateways if you have hosts that now need external routes
    - https://prometheus.io/docs/guides/node-exporter/
    - sudo apt install -y prometheus-node-exporter

- Prometheus
    - https://prometheus.io/
    - https://hub.docker.com/r/prom/prometheus

- Grafana
    - https://grafana.com/docs/grafana/latest/introduction/
    - https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/
    - https://hub.docker.com/r/grafana/grafana

- Docker Compose
    - https://docs.docker.com/compose/intro/compose-application-model/ - main page to get info on sections
    - https://docs.docker.com/compose/intro/compose-application-model/ - key commands for docker compose / diagram on how a docker compose works
    - verify / install docker compose plugin
        - https://docs.docker.com/compose/install/linux/
    - (if needed) installing docker compose - may need to add docker official repo to apt
        - https://hostim.dev/learn/docker/fix-docker-compose-plugin-error/

- Setup monitor
    - new instance (eg. monitor)
        - *would strongly recommend a t2.medium*
        - *think about volumes*
    - [docker-compose.yml](monitoring-helpers/docker-compose.yml) file
        - define set of services (prometheus & grafana)
            - add volumes for persistent storage
            - bind mount configuration file for prometheus
    - [prometheus.yml](monitoring-helpers/prometheus.yml) file
        - define systems for prometheus to query and query frequency
    - Browse to Grafana on port 3000
        - Navigate to Connections > Data Sources > Add data source
        - Select Prometheus and set the URL to your Prometheus server (e.g., http://prometheus:9090) - Save and Test
        - Go to Dashboards > New > Import
        - Enter Dashboard ID 1860 (the popular "Node Exporter Full" community dashboard) and click Load.
            - https://grafana.com/grafana/dashboards/1860-node-exporter-full/

- Grafana k6
    - https://k6.io/
    - https://grafana.com/docs/k6/latest/
    - https://grafana.com/docs/k6/latest/using-k6/ - test parameters
    - https://hub.docker.com/r/grafana/k6
        - note this version is *without* the web browser.  Who needs GUIs?

- Setup tester
    - [build or borrow test files](k6-tests/)
    - `docker run --rm -i -v "$PWD:/scripts:ro" -e BASE_URL=http://34.196.111.132/ grafana/k6 run /scripts/smoke.js`
        - `--rm` = docker rm when done
        - `-i` = keeps the container's STDIN open, and lets you send input to the container through standard input 
            - can end test with CTRL+C for example
        - `-v "$PWD:/scripts:ro"` = bind mounting current directory to containers `/scripts` folder in *read only* mode - container cannot edit
        - `-e BASE_URL=http://34.196.111.132/` = set environment variable; test scripts use env variable
        - `grafana/k6` = docker hub image name
        - `run /scripts/smoke.js` = k6 run command; specify which test to run
    - YouTube: types of tests overview: https://www.youtube.com/watch?v=ghuo8m7AXEM&t=55s


Day 30:

- CI / CD
- GitHub Actions
- YouTube - How big tech ships code to production: https://www.youtube.com/watch?v=551lh10g_go


