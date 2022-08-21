# Project 4

- [Objectives](#Objectives)
- [Project Description](#Project-Description)
  - [Provided Resources](#Provided-Resources)
- [Part 1 - Cloud Formation Template TODOs](#Part-1---Cloud-Formation-Template-TODOs)
- [Part 2 - Setup Load Balancing TODOs](#Part-2---Setup-Load-Balancing-TODOs)
- [Resources and Warnings](#Resources-and-Warnings)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives:

- Modify the CF template to meet updated requirements
- Run a website of choice using nginx or apache2
- Configure the HAProxy load balancer to direct traffic to two backend systems

## Project Description

In your repository, create a `Project4` folder.

For this project, you will be creating resources to use for a load balancing setup. This project will  
keep things simple - you will have one server accessible from the world. You will have two more servers  
that are accessible only within your VPC.

As mentioned in class, you are welcome to use your own website for this project. **However** in order to  
visually check that load balancing is working, you will need to include screenshots that show different content  
fetched from each server. If you look at the `html` files provided, which you are welcome to use, you'll  
see that one has text that is is from server 1 and the other text that it is from server 2.

### Provided Resources

The following is provided in this project folder:

- [cf-template.yml](cf-template.yml)
  - Note: this templated is updated from previous versions to get you started on this project
- [index.srv1.html](index.srv1.html)
  - Note: you can use your own webpage, but for this project you'll need the files to be "different"  
    so that you can tell the content is coming from a different server
- [index.srv2.html](index.srv2.html)

## Part 1 - CloudFormation Template TODOs

The CloudFormation template provided in this project folder is updated to get you started on this project.

Sections you should pay attention to have comments with TODO

All said and done, your template should do the following:

1. Modify the Security Group Ingress rules to have the following additional rules:
   - Access HTTP from any IP address
     - I will allow trusted IPs if you're feeling shy
   - Access HTTP from within the VPC
2. For the HAProxy instance:
   - install haproxy
3. For the pool of content servers:
   - create two total backend host instances
     - one is created already as a template to refer to
   - attach them to the private subnet
     - the private subnet is already configured to route traffic through the NAT gateway
   - assign each instance a unique private IP within the private subnet
   - install webserver of choice on each instance
     - apache2 or nginx is fine
   - on each instance, change the hostname and Tag name to be unique for each system

The deliverable for this part is the CloudFormation template included in your repo folder.

## Part 2 - Setup Load Balancing TODOs

Setup the following and add documentation or screenshots to your `README.md` file as specified.

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs.
   - Description of how file is configured
2. Document how to SSH in between the systems utilizing their private IPs.
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
     - What configuration(s) were set (if any)
     - How to restart the service after a configuration change
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
6. (Optional) - link to your proxy so I can click it.

## Resources and Warnings

- You **DO NOT** need to mess with UFW rules. You may lock yourself out of SSH access.
- You can have a maximum of **FIVE Elastic IP Addresses and FIVE VPCs**
- To manage resources & keep costs down, you will need to delete your CloudFormation stack in between build & test
- Note: feel free to share additional resources over in Discord. I'll be updating this if I see you guys sharing something useful
- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [How to Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [How to Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [How to edit /etc/hosts](https://linuxize.com/post/how-to-edit-your-hosts-file/)
- [The SSH config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [How to SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course  
   repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project4
