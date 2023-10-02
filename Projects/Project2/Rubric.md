# Project 2 Rubric

/ 16

## CloudFormation template submitted ( / 1)

## Modifications to template ( / 12)

1. description of template
2. AMI replaced
3. VPC range to `172.18.0.0/23`
4. subnet range to `172.18.0.0 - 172.18.0.255`
5. resources tagged with names
6. security group setting for inbound SSH within VPC
7. security group setting for inbound SSH from home / trusted network(s)
8. security group setting for inbound SSH from WSU
9. instance setting to set "Tag" "Name" to "CF-instance"
10. instance setting to set a private IP in your subnet range
11. (2 points total) instance setting to change the configuration script built into the `cf-template` to do the following:
    - Install `git`, `python3`, `pip3` (the package manager for `python3`), and `apache2` 
        - (-0.25) points per incorrect installation
    - Change `hostname`
        - (-1) point if hostname is not changed via command in template

## Diagram ( / 3)

- description of your diagram
- diagram accurately illustrates how resources are connected
- image is included in your markdown documentation
