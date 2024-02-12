# Project 2 Rubric

/ 18

## CloudFormation template submitted ( / 1)

## Modifications to template ( / 13)

1. description of template updated
2. AMI updated
3. VPC range to `172.18.0.0/23`
4. subnet range to `172.18.0.0 - 172.18.0.255`
5. resources have added tag with name and value
6. security group rule for inbound SSH within VPC
7. security group rule for inbound SSH from home / trusted network(s)
8. security group rule for inbound SSH from WSU
9. security group rule for inbound HTTP from any IP
10. instance set "Tag" "Name" to "CF-instance"
11. instance set a private IP in your subnet range
12. (2 points total) instance setting to change the configuration script built into the `cf-template` to do the following:
    - Install `git`, `python3`, `pip3` (the package manager for `python3`), and `apache2` 
        - (-0.25) points per incorrect installation
    - Change `hostname`
        - (-1) point if hostname is not changed via command in template

## Diagram ( / 4)

- viewable in `README.md` file
- includes description of project
- includes description to explain your diagram
- diagram logically illustrates how resources are connected
