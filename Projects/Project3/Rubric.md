# Project 3 Rubric

/ 20

## README.md and CF Template exist in Project 3 folder in repo ( / 1)

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

## README.md documentation for configuration ( / 11)

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs  
   Description on how file is configured ( / 1)
2. Document how to SSH in between the systems utilizing their private IPs. ( / 1)
3. **_HAProxy configuration & documentation requirements_** ( / 3)
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
     - What configuration(s) were set (if any)
     - How to restart the service after a configuration change
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_** ( / 4)
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots. ( / 2)
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
