# Midterm Review for CEG 3120

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

# Midterm will expect introductory understanding here

## Week 7 / 8

- Using CloudFormation Templates
  - using YAML/JSON formatted files
- Debugging CF Templates

### Project 2

- Create CloudFormation template
  - should mimic what was manually created

