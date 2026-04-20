# Final Review for CEG 3120

## Week 1 / 4

- create aws stack
- terminal command reminder
- users & groups
- permissions
- ssh keys
  - private vs public
  - .ssh/config
  - .ssh/authorized_keys
  - .ssh/known_hosts
  - viewing status of / start / stop ssh service
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
- containers
  - isolation
  - docker
    - pull
    - push
    - ps
    - images
    - run (`-it`, `-d`, `-p HOST:CONTAINER`, bind mount)
    - attach
    - exec
    - start
    - stop / kill
    - rm
    - build (`-t`)
    - import
    - export
    - inspect
    - logs
    - login
  - Dockerfile
    - FROM
    - COPY
    - WORKDIR
    - RUN
    - CMD 

### Project 0

- git guide
- docker guide
- ssh with different tools (GitHub & AWS)


### Project 0.5

- build instructions for a container
  - git server built into a container
  - containerize your own app with dependencies
  - containerize Duncan's pre-req scraper

## Background Networking Know-How

- networking know how
  - IPv4 addresses
  - Subnets & CIDR blocks
  - routes
  - gateways
  - NAT
  - Firewalls
    - stateful vs stateless
    - whitelist vs blacklist
    - network wide
    - per machine (iptables)

## Week 5 / 7

- the cloud
  - types of cloud services (IaaS, PaaS, SaaS)
  - regions - in that others exist and define their own AMI IDs, instance types, etc.

- AWS
  - VPC
  - Subnets (~~private~~ vs public)
  - Routes & route tables
  - Internet Gateway
  - Security Group vs Network ACLs
  - Elastic IPs vs public IP
  - ~~NAT Gateway (focus on public)~~
  - Instance types
  - AMIs
  - Volumes

### Project 1

- Manually creating the resources
  - VPC
  - NACL & SG configuration
  - instance type & AMI
  - SSH to instance with EIP

## Week 7 / 8

- Using CloudFormation Templates
  - using YAML/JSON formatted files
- Debugging CF Templates

### Project 2

- Create CloudFormation template
  - should mimic what was manually created

## Week 9 / 10

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

## Week 11 / 12

- Continuous integration using GitHub Actions
- Terminology in GitHub Actions:
  - workflow (and where it goes)
  - events
  - runners
  - jobs
    - steps
  - actions
    - `uses`, `with`
- semantic versioning
- `git` tags
- versioning DockerHub images with GitHub Actions

### Project 4

- use GitHub action to build image on push and push image to DockerHub using semantic versioning

## Week 13 / 14

- Continuous Deployment
- WebHooks / reverse APIs
  - payload sender
    - triggering payload sending
    - configuration thoughts
  - listener
    - service configuration
    - considerations:
      - validating hook delivery / inspecting payloads
      - creating a service
      - viewing logs

### Project 5

- use DockerHub or GitHub to send payload with WebHooks
- configure and run webhook listener on server to process payload deliveries
