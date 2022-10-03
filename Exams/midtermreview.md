# Midterm Review for CEG 3120

## Fall 2022

## Da Rules

Midterm: Friday, 10/7

- Available 9:05 AM to 10:00 AM
- 1 attempt, 55 minutes once started
- Open note, open terminal
- No class - only exam.

## Week 1 & 2

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

## Week 6 / 7

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
