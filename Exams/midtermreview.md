# Midterm Review for CEG 3120

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
- containers
  - isolation
  - docker
    - pull
    - ps
    - images
    - run (`-it` `-p HOST:CONTAINER`)
    - exec
    - start
    - stop / kill
    - rm
    - import
    - export  

### Project 0

- git guide
- docker guide
- ssh with different tools (GitHub & AWS)

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
  - ~~access management of cloud resources~~
    - IAM tokens for **authorization**
      - can create(?) access(?) delete(?) view billing(?)
- AWS
  - VPC
  - Subnets (private vs public)
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
- ~~proxies~~
  - forward vs reverse
- ~~load balancers~~
  - terminology
  - function
  - Layer 4 vs Layer 7
