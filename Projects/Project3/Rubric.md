# Project 3 Rubric

/ 31

## CloudFormation template ( / 15)

1 point per bullet / task

1. Use AMI of your choice (from P1/P2 for example)
2. VPC CIDR block: `172.18.0.0/23`
3. Public subnet range: `172.18.0.0 - 172.18.0.255`
4. Private subnet range: `172.18.1.0 - 172.18.1.255`
5. Modifications for Security Group:
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
6. For the load balancer (proxy) instance:
   - assign private IP on public subnet
   - install `haproxy`
7. For host instances:
   - create three total host instances
   - tag each with a unique name
   - assign each private IP on private subnet
   - install `apache2` or `nginx` on each
   - configure a unique `hostname` on each instance

## README.md documentation for configuration ( / 16)

If document does not use well formatted markdown it will receive a 0.

If document includes all project instruction text (my assignment words) it will receive a 0.

1 point per bullet / task

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack and what resources are created.
2. `ssh` within VPC:
   - Describe how the file is configured on each instance and what the benefit is
   - Document how to `ssh` among the instances
3. How to set up a HAProxy load balancer:
   - What file(s) where modified & their location
   - What configuration(s) were set (if any)
   - How to restart the service after a configuration change
   - Resources used (websites)
4. How to set up Hosts 1, 2, & 3 to serve web content
   - Document any changed configurations (if any)
   - Document where site content files are located (and why)
   - Web content has been modified from base files given (validated in proof screenshot)
   - How to restart the service in case of a configuration change
   - Resources used (websites)
5. Load balancing proof:
   - screenshot of alternate hosts' content displaying to browser
   - command to view `haproxy` logs to show traffic is being distributed among hosts
   - screenshot of `haproxy` logs 

## Extra Credit - Setup HTTPS ( / 5)

1. Documents general needs to set up HTTPS
2. Documents `haproxy` needs to handle HTTPS
3. Documents `apache2` OR `nginx` needs to handle HTTPS
4. Documents changes in VPC resources to handle HTTPS
5. Proves that configuration worked