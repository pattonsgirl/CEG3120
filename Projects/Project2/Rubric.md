# Project 2 Rubric

## Project Score: / 25

## Required Documents ( / 1)
- [ ] `README.md` file
- [ ] CloudFormation template

## Modifications to CF Template ( / 20)

- [ ] Template description revised to describe what template builds
- [ ] AMI changed to P1 AMI
- [ ] VPC range to `192.168.0.0/23`
- [ ] Subnet range to `192.168.0.0 - 192.168.0.255`
- [ ] Resources have added tag with Name and Value of `LASTNAME-CF-RESOURCE`
- [ ] Security Group rule for inbound SSH within VPC
- [ ] Security Group rule for inbound SSH from home / trusted network(s)
- [ ] Security Group rule for inbound SSH from WSU
- [ ] Security Group rule for inbound HTTP to port 80 from any IP
- [ ] Security Group rule for inbound HTTP to port 8080 from any IP
- [ ] Network ACL denies outgoing traffic to `wttr.in` but allows all other traffic outbound
- [ ] Instance sets a private IP in subnet range

Instance's `UserData` script:  

- [ ] Changes hostname
- [ ] Installs `wamerican`, `git`, `python3`, `pip3` (0.25 pt / each)
- [ ] Installs `apache2` and `docker` (0.5 pt / each)
    - enables and starts the services if needed per AMI 
- [ ] Copies wordle.sh to default user's home directory
- [ ] Copies index.html to the default web content directory for `apache2`
- Docker container `wsukduncan/cheatsheet`
    - [ ] runs as a detached process
    - [ ] is set to restart if stopped
    - [ ] is bound to host port 8080 and container port 80

## README Documentation ( / 4)

- [ ] includes description of project
- [ ] includes description to explain your diagram
- [ ] Diagram visible / embedded in `README.md` file
- [ ] Diagram logically illustrates how resources are connected

## Point Deductions - Penalty Total: 

- [ ] CF Template does not build a successful stack - 2 point penalty
- [ ] Not all resources tagged with Name and Value - 0.5 point penalty per untagged resource)
- [ ] Security Group has additional rules that make it too open - 1 point penalty per badly formed rule
- [ ] Bad NACL rule order - 1 point penalty
