# Project 3 Rubric

## Project Score: / 58

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

## README.md documentation for configuration: / 30

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

## Extra Credit - Hands Free
Worth +10% = 5.8 pts

If documentation requirements are not complete, the extra credit for the CF template will not be awarded.

- [ ] On building from template, load balancers and hosts are fully configured without additional configuration.

## Extra Credit - Setup HTTPS 
Worth +20% = 11.6 pts

If documentation requirements are not complete, the extra credit for setting up HTTPS will not be awarded.

Documentation scope: 
1. [ ] Creating a self-signed certificate
2. [ ] AWS requirements to set up HTTPS
3. [ ] Documents `haproxy` requirements to handle HTTPS
4. [ ] (if needed) `apache2` OR `nginx` requirements to handle HTTPS
5. [ ] Screenshot(s) to prove that configuration worked

## Common Point Deductions:

- [ ] (-100%) Documentation not well organized with markdown OR includes project descriptive text
- [ ] (-10% = 5.8 pts) CF Template does not build
- [ ] (-10% = 5.8 pts) Documentation fails to address what was not implemented and implies the project is fully functional.  Always document shortcomings and note what is "research" on how the rest should be done
- [ ] (-5% = 2.9 pts) Security Group rules allow access beyond project bounds
