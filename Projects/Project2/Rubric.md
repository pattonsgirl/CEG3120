# Project 2 Rubric

/ 20

## CloudFormation template submitted ( / 1)

## Modifications to template ( / 15)

1. Template description revised to what template builds
2. AMI changed to P1 AMI
3. VPC range to `172.18.0.0/23`
4. Subnet range to `172.18.0.0 - 172.18.0.255`
5. Resources have added tag with Name and Value of `LASTNAME-CF-RESOURCE`
6. Security Group rule for inbound SSH within VPC
7. Security Group rule for inbound SSH from home / trusted network(s)
8. Security Group rule for inbound SSH from WSU
9. Security Group rule for inbound HTTP from any IP
10. Network ACL denies traffic to `wttr.in`
11. Instance set a private IP in subnet range

Instance's `UserData` script:  

12. Changes hostname
13. Installs `git`, `python3`, `pip3`, `apache2`, and `wamerican` (.2 pts / each)
14. Copies wordle.sh to default user's home directory
15. Copies index.html to default apache2 web content directory

## Diagram ( / 4)

- viewable in `README.md` file
- includes description of project
- includes description to explain your diagram
- diagram logically illustrates how resources are connected

## Point Deductions

- Not all resources tagged with Name and Value (-0.5 / untagged resource)
- Security Group has additional rules that make it too open (-1 / rule)
- Bad NACL rule order (-1)
