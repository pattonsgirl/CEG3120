# Project 3

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
- Run a website of choice using `nginx` or `apache2` on hosts in the pool
- Configure `haproxy` as a load balancer to direct traffic to the pool

## Project Description

In your repository, create a `Project3` folder.

For this project, you will have two deliverables:

1. CloudFormation template with modifications for project
2. Documentation (and specified screenshots) for configuring the ADC and hosts post stack creation. 

### Provided Resources

The following is provided in this project folder:

- [`lb-cf-template.yml`](lb-cf-template.yml)
  - Note: this templated is updated from previous versions to get you started on this project
- [`site.tar.gz`](site.tar.gz)
  - Note: you can use your own site content, but for this project you'll need the site content on each host to be "different" so that you can tell the content is coming from a different server.

## Part 1 - CloudFormation Template TODOs

The CloudFormation template provided in this project folder is **updated from Project 2** to get you started on this project.

Your deliverable for this portion is only **your CloudFormation template**.

Modify the template in the following ways:

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

**The deliverable for this part is the CloudFormation template in your Project 3 folder.**

## Part 2 - Setup Load Balancing TODOs

In your `Project3` folder, create a `README.md` file.  This document will focus on finishing configuration after your stack builds.

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
   - image must include proxy IP (i.e. URL bar)

## Resources and Warnings

- You **DO NOT** need to mess with UFW rules. You may lock yourself out of SSH access.
- You can have a maximum of **FIVE Elastic IP Addresses and FIVE VPCs**
- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [How to Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [How to Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [How to edit /etc/hosts](https://linuxize.com/post/how-to-edit-your-hosts-file/)
- [The SSH config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [How to SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
- [Create & Extract with `tar`](https://linuxize.com/post/how-to-create-and-extract-archives-using-the-tar-command-in-linux)

## Submission

1. Your repo should contain:
   - `YOURLASTNAME-cf.yml` (your modified CloudFormation template)
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   - Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project3

## Rubric

[Rubric](Rubric.md)
