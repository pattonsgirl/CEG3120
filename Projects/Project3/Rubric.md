# Project 3 Rubric

Common notes:

- Leaving this in with the default location of 0.0.0.0/0 for SSHLocation = SSH from anywhere

```
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: !Ref SSHLocation
```

- (-0.25) apt install pip3 does not install pip3. apt install python3-pip does

/ 12

## CloudFormation template submitted ( / 1)

## Modifications required for credit ( / 11)

1. description of template
2. ami replaced to AMI selected in project 2
3. VPC range to 10.0.0.0/24
4. subnet range to 10.0.0.0/28
5. resources tagged with names
6. security group setting for inbound SSH within VPC
7. security group setting for inbound SSH from home / trusted network(s)
8. security group setting for inbound SSH from WSU
9. instance setting to set "Tag" "Name" to "CF-instance"
10. instance setting to set a private IP in your subnet range
11. instance setting to change the configuration script built into the cf-template to do the following:
    - Install git, python3, pip3
    - Change hostname
