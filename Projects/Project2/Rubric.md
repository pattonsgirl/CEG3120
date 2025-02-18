# Project 2 Rubric

## Project Score: / 20

## Required Documents ( / 1)
- [ ] `README.md` file
- [ ] CloudFormation template

## Modifications to CF Template ( / 15)

- [ ] Template description revised to describe what template builds
- [ ] AMI changed to P1 AMI
- [ ] VPC range to `172.18.0.0/23`
- [ ] Subnet range to `172.18.0.0 - 172.18.0.255`
- [ ] Resources have added tag with Name and Value of `LASTNAME-CF-RESOURCE`
    - see deduction penalty in bottom section if this box is not selected as complete
- [ ] Security Group rule for inbound SSH within VPC
- [ ] Security Group rule for inbound SSH from home / trusted network(s)
- [ ] Security Group rule for inbound SSH from WSU
- [ ] Security Group rule for inbound HTTP from any IP
- [ ] Network ACL denies outgoing traffic to `wttr.in` but allows all other traffic outbound
    - see deduction penalty in bottom section if this box is not selected as complete
- [ ] Instance sets a private IP in subnet range

Instance's `UserData` script:  

- [ ] Changes hostname
- [ ] Installs `git`, `python3`, `pip3`, `apache2`, and `wamerican` (.2 pts / each)
- [ ] Copies wordle.sh to default user's home directory
- [ ] Copies index.html to default apache2 web content directory

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
