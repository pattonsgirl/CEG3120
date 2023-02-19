# Midterm Review for CEG 3120

## Spring 2022

## Da Rules

Midterm: Friday, 2/24

- Available 1:25 PM to 2:20 PM
- 1 attempt, 55 minutes once started
- Open note, open terminal
- No class - only exam.

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
    - IAM tokens for **authorization** 
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

### Project

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

### Project 2

- CF Template
  - create one instance with public IP
  - create one NAT gateway
  - connect host instances to private subnet
- Configure load balancer
- Configure hosts in backend pool to serve content