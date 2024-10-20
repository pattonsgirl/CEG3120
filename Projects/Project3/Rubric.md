# Project 3 Rubric

## Project Score: / 42

## CloudFormation template ( / 27)

1. AMI adjusted to Ubuntu 18+ or Amazon Linux 2
2. VPC CIDR block: `172.18.0.0/23`
3. Public subnet range: `172.18.0.0 - 172.18.0.255`
4. Private subnet range: `172.18.1.0 - 172.18.1.255`
5. Modifications for Security Group: (5 points)
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `ssh` requests from Wright State IP block
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
6. For the load balancer (proxy) instance: (3 points)
   - assign private IP on public subnet
   - configure a unique `hostname` on the instance
   - install `haproxy`
      - service start & enable steps, if applicable
7. Create three total host instances: (5 points / host instance)
   - tag each with a unique name
   - assign each a private IP on private subnet
   - configure a unique `hostname` on each instance
   - install `apache2` or `nginx` on each instance
       - depending on AMI, also perform steps to start & enable service 
   - download and extract to default site content directory `simple-site.tar.gz`

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