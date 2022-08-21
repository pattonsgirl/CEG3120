# Project 4 Rubric

/ 20

## README.md and CF Template exist in Project 5 folder in repo ( / 1)

## CloudFormation template ( / 8)

Note: 1 pt per bullet

1. Modify the Security Group Ingress rules to have the following additional rules:
   - Access HTTP from any IP address
   - Access HTTP from within the VPC
2. For the HAProxy instance:
   - install haproxy
3. For the pool of content servers:
   - create two total backend host instances
   - attach them to the private subnet
   - assign each instance a unique private IP within the private subnet
   - install webserver of choice on each instance
   - on each instance, change the hostname and Tag name to be unique for each system

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
