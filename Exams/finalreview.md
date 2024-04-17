# Final Review for CEG 3120

## Week 1 / 2

- create aws stack
- terminal command reminder
- users & groups
- permissions
- ssh keys
  - private vs public
  - .ssh/config
  - .ssh/authorized_keys
  - .ssh/known_hosts
- git & GitHub
  - clone
  - init
  - add
  - rm (and rm --cached)
  - commit
  - push
  - pull
  - branch
  - fetch / merge
  - checkout
  - merge conflicts
  - Pull Requests
  - .gitignore
  - markdown essentials

### Project 0

- git guide

## Week 2 / 3

- networking review
  - IPv4 addresses
  - Subnets & CIDR blocks
  - routes
  - gateways
  - NAT
  - Firewalls
    - network wide
    - per machine (iptables)

## Week 3 / 4

- the cloud
  - types of cloud services
  - regions
  - access management of cloud resources
    - ~~IAM tokens for **authorization**~~
      - can create(?) access(?) delete(?) view billing(?)
- AWS
  - VPC
  - Subnets (private vs public)
  - Routes & route tables
  - Internet Gateway
  - Security Group vs Network ACLs
  - Elastic IPs vs public IP
  - NAT Gateway (focus on public)
  - Instance types
  - AMIs
  - Volumes

### Project 1

- Manually creating the resources
  - VPC
  - instance type & AMI
  - EIP to instance

## Week 5 / 6

- Using CloudFormation Templates
  - using YAML/JSON formatted files
- Debugging CF Templates

### Project 2

- Create CloudFormation template
  - should mimic what was manually created

## Week 6 / 7

- system logs & service control
- installing and configuring a webserver
  - apache vs nginx
  - status / control of services (systemctl)
  - service logs (apache & ssh)
- proxies
  - forward vs reverse
- load balancers  
  - terminology
  - function
  - Layer 4 vs Layer 7
- fault tolerance
- monitoring

### Project 3

- CF Template
  - create one instance with public IP
  - create one NAT gateway
  - connect host instances to private subnet
- Configure load balancer
- Configure hosts in backend pool to serve content

## Week 8 / 9 / 10

- containers using Docker
  - purpose & constraints
  - images & image selection
    - `docker pull ___`
    - `docker images`
    - `docker image rm ___`
  - Running containers
    - `docker run` + options (`--name`, `--rm`, `-v`, `-p`, `-d`, `-it`)
    - `docker ps` + `-a`
    - `docker kill ___` (or) `docker stop ___`
    - `docker rm ___` (and why...)
  - Dockerfiles (recipes)
    - `docker build` + `-t`
    - `FROM`, `WORKDIR`, `RUN`, `COPY`, `CMD`
  - using container registry (DockerHub)
    - `docker push ___`
    - tagging considerations
- Continuous integration using GitHub Actions
- Terminology in GitHub Actions:
  - workflow (and where it goes)
  - events
  - runners
  - jobs
    - steps
  - actions
    - `uses`, `with`

### Project 4

- containerize a website
- use GitHub action to build image on push and push image to DockerHub

## Week 11 / 12

- semantic versioning
- `git` tags
- versioning DockerHub images with GitHub Actions
- Continuous Deployment
- WebHooks / reverse APIs
  - what does client need for configuration
  - what does server need for configuration
  - considerations:
    - validating hook delivery
    - creating a service
    - viewing logs

### Project 5

- versioning DockerHub images with GitHub Actions
- use DockerHub or GitHub to send payload with WebHooks
