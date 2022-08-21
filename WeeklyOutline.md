# Weekly Outline for CEG 3120

## Week 1 & 2

- syllabus
- create aws stack
- terminal command reminder
- users
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
  - merge conficts
  - Pull Requests
  - .gitignore
  - markdown essentials

### Project

- git guide

## Week 3

- crash course python notes
- package version dependencies and usage
- APIs
  - REST APIs
    - querying
    - version dependent (how queries are requested can change)
  - syncronous vs asyncronous APIs
  - Requesting and using OAuth keys
- authentication vs authorization
  - OAuth - allow third party to do x y z
  - JSON Web Tokens & session cookies
    - keeping you logged in and maintaining session details
- process exploration
  - bot runs as long as starting terminal is open
  - screen / background jobs (2350) - detaching processes
  - cloud solutions?
  - containers?

### Project

- Discord Bot using Discord API w/ discord.py
- managing secrets for a project
- using branches for changes

## Week 4

- linters and unit tests
  - using hooks to trigger
- networking review
  - IPv4 addresses
  - Subnets & CIDR notation
  - routes
  - gateways
  - NAT
  - Firewalls
    - network wide (AWS Security Groups)
    - per machine (iptables)

## Week 5

- the cloud
  - types of cloud services
  - regions
  - access management of cloud resources
    - token based can create(?) access(?) delete(?) view billing(?)
- intro to navigating AWS
  - EC2 instance types
  - images / AMI
  - networking (VPC, subnet, gateways, routes, security group)

### Project

- Manually creating the resources
  - VPC
  - instance type & AMI
  - EIP to instance

## Week 6

- intro to contents of CloudFormation Template
  - using YAML/JSON formatted files
- system logs & service control
- installing and configuring a webserver
  - apache vs nginx
  - status / control of services (systemctl)
  - service logs (apache & ssh)
  - security groups
  - iptables? system level firewalls
  - nmap -p 1-5000 server

### Project

- Create CloudFormation template
  - should mimic what was manually created

## Week 7

- intro to proxies & HAProxy
- Midterm review
- Midterm

## Week 8 & 9

- Midterm review
- NAT Gateways
  - one EIP, external communication allowed
- messing with a webserver
  - HTTPS vs HTTP and notes on certificates
- load balancing and fault tolerance
  - HAproxy configurations
  - keeping backend servers private - when are public IPs needed?
  - fault tolerance of non-responsive backends
- monitoring
  - Networked systems (Grafana?)
  - cloud costs and usage

### Project

- CF Template
  - create three instances
  - create one NAT gateway? Connect two instances to that?
- Configure load balancer
- Configure hosts to hold unique content

## Week 10

- containers (Docker)
  - purpose & constraints
  - images
  - Dockerfiles (recipes)
  - deploying containers

## Week 11

## Week 12

- continuous development and integration
  - GitHub actions
  - docker hub
  - GitHub webhooks?

## Week 13

## Week 14

## Topics the need a home:

- Directory service & relational database concepts and usage
  - host db on a system? the books API example?

## Course Learning Objectives:

1. Understanding of what can be accomplished be using modern language features and software development practices to develop a distributed information technology system
2. Understanding of networking roles in a distributed information technology infrastructure
3. Use of and application of modern software development tools and methodologies and part of a team
4. Distributed architecture and fault tolerance concepts
5. Application programming interface design and usage
6. Directory and relational database concepts and integration
7. Introduction to cloud systems and modern deployment techniques
8. Introduction to continuous development and continuous integration

## Course Outline:

1. Using the command line interface & scripting
2. Networking (private vs public accessibility, sockets & ports, SSH keys)
3. Understanding logs, usage of configuration files, process control
4. Development tools (version management, team organization)
5. Cloud infrastructure & Infrastructure as a Service (IaaS)
6. Utilizing Application Programming Interfaces (APIs) & Service Oriented Architecture (SOA)
7. Directory service & relational database concepts and usage
8. Continuous integration & automating change management
9. Continuous deployment & automating production
10. Distributed architecture
11. Infrastructure as Code (IaC)
12. Fault tolerance & health monitoring
13. Introduction to scalability, cost, and maintenance considerations
