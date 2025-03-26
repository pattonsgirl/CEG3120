# Project 3 Rubric

## Project Score: / 42

## Required Documents ( / 3)
- [ ] `README.md` file
- [ ] CloudFormation template
- [ ] folder with site content

## CloudFormation template ( / 25)

- [ ] AMI adjusted to Ubuntu 18+ or Amazon Linux 2
- [ ] VPC CIDR block: `172.18.0.0/23`
- [ ] Public subnet range: `172.18.0.0 - 172.18.0.255`
- [ ] Private subnet range: `172.18.1.0 - 172.18.1.255`
- Security Group:
   - [ ] rule to allow `ssh` requests within VPC CIDR block
   - [ ] rule to allow `ssh` requests from your home IP
   - [ ] rule to allow `ssh` requests from Wright State IP block
   - [ ] rule to allow `http` requests from within VPC CIDR block
   - [ ] rule to allow `http` requests from any IP
   - Possible additions if HTTPS documentation for Extra Credit is complete:
      - [ ] rule to allow `https` requests from within VPC CIDR block
      - [ ] rule to allow `https` requests from any IP
- Load balancer (proxy) instance:
   - [ ] assigned private IP on public subnet
   - [ ] uses command in `UserData` to configure a unique `hostname` on the instance
   - [ ] uses command in `UserData` to install `haproxy`
   - Possible additions:
      - [ ] (if Amazon Linux 2) service start & enable steps
- [ ] Creates three instances to use as hosts in the HAProxy pool
- Host instance 1:
   - [ ] tagged with a unique Name Value
   - [ ] assigned private IP on private subnet
   - [ ] uses command in `UserData` to configure a unique `hostname` on the instance
   - [ ] uses command in `UserData` to install `haproxy`
   - Possible additions:
      - [ ] (if Amazon Linux 2) service start & enable steps
      - [ ] downloads site contents (method reflected in documentation)
      - [ ] extracts site contents (method reflected in documentation)
- Host instance 2:
   - [ ] tagged with a unique Name Value
   - [ ] assigned private IP on private subnet
   - [ ] uses command in `UserData` to configure a unique `hostname` on the instance
   - [ ] uses command in `UserData` to install `haproxy`
   - Possible additions:
      - [ ] (if Amazon Linux 2) service start & enable steps
      - [ ] downloads site contents (method reflected in documentation)
      - [ ] extracts site contents (method reflected in documentation)
- Host instance 3:
   - [ ] tagged with a unique Name Value
   - [ ] assigned private IP on private subnet
   - [ ] uses command in `UserData` to configure a unique `hostname` on the instance
   - [ ] uses command in `UserData` to install `haproxy`
   - Possible additions:
      - [ ] (if Amazon Linux 2) service start & enable steps
      - [ ] downloads site contents (method reflected in documentation)
      - [ ] extracts site contents (method reflected in documentation)

## README.md documentation for configuration ( / 15)

1. Project description (3 points)
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack and what resources are built.
   - **Diagram** of how the load balancer works in context of resources created in CF template
2. `ssh` to instances with the VPC: (2 points)
   - Explain your entries in either or both `/etc/hosts` OR `.ssh/config` files.
   - How to `ssh` among the instances utilizing one (or both) files for ease of access
3. Setting up the HAProxy load balancing instance: (3 points)
   - Explain files that will need modified and general purpose of each file
   - Explain the configuration blocks within each changed file
   - Explain how to restart the service after a configuration change
4. How to set up Hosts 1, 2, & 3 to serve web content (3 points)
   - Document site content set up
   - Explain how to reload after web content changes
   - Explain how to restart the service after a service configuration change
5. Load balancing proof: (4 points)
   - Explain how the user can visually test that their load balancer is working based on your method choice and supporting documentation
   - screenshot of alternate hosts' content displaying to browser
   - Explanation & command to view `haproxy` logs to show traffic is being distributed among hosts
   - screenshot of `haproxy` logs 

## Extra Credit - Setup HTTPS - +20% EC (( / 5) * 8.4) 

1. Documents general requirements to set up HTTPS
2. Documents `haproxy` requirements to handle HTTPS
3. Documents `apache2` OR `nginx` requirements to handle HTTPS
4. Documents changes in VPC resources to handle HTTPS
5. Proves that configuration worked

## Point Deductions:

- (-100%) Documentation not well organized with markdown OR includes project descriptive text
- (-10%) CF Template does not build
- (-1 point / rule) Bad Security Group rules 