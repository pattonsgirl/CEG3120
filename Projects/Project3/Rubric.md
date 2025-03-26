# Project 3 Rubric

## Project Score: / 42

## Required Documents: / 3
- [ ] `README.md` file
- [ ] CloudFormation template
- [ ] folder with site content

## CloudFormation template: / 25

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

## README.md documentation for configuration: / 15

1. Project description:
   - [ ] Provides an overview of the project goal
   - [ ] Provide a description of how to use the CF template to create a stack
   - [ ] Provide a description of what resources are built.
   - [ ] **Diagram** is visible in description section
2. Diagram:
   - [ ] cleanly presented
   - Explains the CF template for the project in terms of:
      - [ ] networking & routes
      - [ ] firewalls
      - [ ] instances
3. Connections to instances within the VPC:
   - [ ] Description of purpose for configuring in `/etc/hosts` AND / OR `.ssh/config` files.
   - [ ] Explanation of entries in `/etc/hosts` AND / OR `.ssh/config` files.
   - [ ] Required setup to `ssh` among the instances 
   - [ ] How to `ssh` among the instances using one or both of the above files for ease of use.
4. Setting up the HAProxy load balancing instance:
   - [ ] Explanation of file(s) that will need modified and general purpose of the file(s)
   - [ ] Snippets of haproxy configuration file or link to file in repo
   - [ ] Explanation of configuration file modifications
   - [ ] How to test the haproxy configuration file after revisions
   - [ ] Explanation and commands to manage the service (and when to run them)
5. Setting up Hosts 1, 2, & 3 to serve web content:
   - [ ] Document how to set the hosts to utilize your website 
      - [ ] method used to get site content to host instance
      - [ ] location of site content
6. Load balancing proof:
   - Proof via the browser:
      - [ ] Explain how the user can visually test that their load balancer is working 
      - [ ] Screenshot(s) of the project working in your browser
      - [ ] Link to the Load Balancer Public IP
   - Proof via logs:
      - [ ] Explanation of set up chosen log method
      - [ ] Explanation of how to view logs via chosen method (and what user should be attentive to)
      - [ ] Screenshot(s) of log method showing distribution of client connections among hosts
7. Troubleshooting:
   - Provide recommendations on what to troubleshoot if the load balancer is **not** working
      - [ ] Scenario 1
      - [ ] Scenario 2
      - [ ] Scenario 3 
8. Citations / Resources:
   - [ ] Provided

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