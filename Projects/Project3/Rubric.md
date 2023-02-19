# Project 3 Rubric

/ 30

## CloudFormation template ( / 15)

Note: 1 point per bullet / task

1. Use AMI of your choice (from P1/P2 for example)
2. VPC CIDR block: `192.168.0.0/23`
3. Public subnet range: `192.168.0.0 - 192.168.0.255`
4. Private subnet range: `192.168.1.0 - 192.168.1.255`
5. Modifications for Security Group:
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
6. For the load balancer (proxy) instance:
   - assign private IP on public subnet
   - install `haproxy`
7. For host instances:
   - create three total instances
   - tag with a unique name
   - assign private IP on private subnet
   - install `apache2` or `nginx`
   - configure a unique `hostname` on the instance

## README.md documentation for configuration ( / 15)

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack and what resources are created.
2. `ssh` within VPC:
   - Configure `/etc/hosts` OR `.ssh/config` on each instance
      - I like to do both, but that's me
   - Describe how the file is configured on each instance and what the benefit is
   - Document how to `ssh` among the instances
3. How to set up a HAProxy load balancer:
   - What file(s) where modified & their location
   - What configuration(s) were set (if any)
   - How to restart the service after a configuration change
   - Resources used (websites)
4. How to set up Hosts 1, 2, & 3 to serve web content
   - What file(s) were modified & their location
   - What configuration(s) were set (if any)
   - Where site content files were located (and why)
   - How to restart the service after a configuration change
   - Resources used (websites)
5. From the browser, when connecting to the proxy server, take screenshots that prove the load balancer is configured and uses the allocation strategy set.
