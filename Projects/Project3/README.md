# Project 3

- [Objectives](#Objectives)
- [Project Description](#Project-Description)
  - [Provided Resources](#Provided-Resources)
  - [Web Site - Scope and Implementation](#web-site---scope-and-implementation)
- [Part 1 - Cloud Formation Template TODOs](#part-1---cloudformation-template-todos)
- [Part 2 - Setup Load Balancing TODOs](#part-2---setup-load-balancing-todos)
- [Resources and Warnings](#resources-and-warnings)
- [Extra Credit - Hands Free](#extra-credit---hands-free---10) 
- [Extra Credit - HTTPS](#extra-credit---https---20)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives:

- Build a container image from Apache's httpd project with web content - publish it to DockerHub
- Modify the project CF template to meet requirements for this project
- Run the website container on hosts in the pool
- Configure `haproxy` as a load balancer / application delivery controller to direct traffic to the pool

## Project Description

In your repository, create a `Project3` folder.

For this project, you will have three required deliverables:

1. CloudFormation template with modifications per project requirements
2. Folder with your website files and Dockerfile
3. Documentation (and specified screenshots) for configuring the load balancer and hosts in the pool after stack creation. 

### Provided Resources

The following is provided in this project folder:

- [`lb-cf-template.yml`](lb-cf-template.yml)
  - Note: this templated is updated from previous versions to get you started on this project

## Part 1 - Create a Docker Image

1. In your `Project3` folder, create a folder named `web-content`.  The files that follow must exist in this folder.

2. Bring **or** create a website with:
- a minimum of **two** html files (`index` and one other)
- a minimum of **one** css file

You may use generative AI to create you a site per a theme, but you must **cite** which generative AI system you used and the prompt you fed to it.

3. Create a `Dockerfile` with the following two instructions:
- Build from `httpd:2.4`
- Copy all content in `web-content` into the container filesystem in the default web content directory for `httpd` 

4. Build and tag a container image using your `Dockerfile` as the build instructions

5. Login to DockerHub on the command line.  Use a Personal Access Token (PAT) instead of a password.

6. Push your container image to a **public** DockerHub repository.

Recommended: pull your container image and run it to test that it serves your web content.

Documentation requirements will be listed in [Part 4](#part-4---README)

## Part 2 - CloudFormation Template TODOs

Your deliverable for this portion is only **your CloudFormation template**.

If you **could not perform** a task via the Cloud Formation template, you'll need to document how you manually performed the task during [Part 4](#part-4---README) for a partial credit opportunity.  You may specify your research into completing taskings as long as you highlight that it is research based - not something your project implemented.

Modify the template in the following ways:

1. Use AMI of your choice that is Ubuntu 18+ or Amazon Linux 2+
2. VPC CIDR block: `192.168.0.0/23`
3. Public subnet range: `192.168.0.0 - 192.168.0.255`
4. Private subnet range: `192.168.1.0 - 192.168.1.255`
5. Modifications for Security Group:
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `ssh` requests from Wright State IP block (`130.108.0.0/16`)
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
   - *If doing Extra Credit* add `https` rules **in addition to** `http` rules
6. For the load balancer (proxy) instance:
   - assign private IP on the public subnet
   - use instance `UserData` to configure a unique `hostname` on the instance
   - use instance `UserData` to install `haproxy`
      - depending on AMI, also perform steps to start & enable service
7. Create three host instances (one is templated, two more need to be added)
   - tag each with a unique Name Value
   - assign each a private IP on the private subnet
   - use instance `UserData` to configure a unique `hostname` on the instance
   - pull and run your DockerHub image in detached mode bound to host port 80 and container port 80. Use the appropriate flag to have the container restart automatically if the system is rebooted / if the docker service has an outage.
        - [Detached mode - Docker Docs](https://docs.docker.com/reference/cli/docker/container/run/#detach)
        - [Start containers automatically - Docker Docs](https://docs.docker.com/engine/containers/start-containers-automatically/)

**The deliverable for this part is the CloudFormation template in your Project 3 folder. Do not forget to add citations in [Part 4](#part-4---README) if additional resources were used.**

## Part 2 - Setup Load Balancing TODOs

In your `Project3` folder, create a `README.md` file.  This document will focus on finishing configuration after your stack builds.

Your documentation should be written with as though someone is using it as a guide to recreate your project (like a blog post would do).

If you cannot complete all tasks, make sure to document shortcomings / stuck points and note what is "research" on how the rest should be done for partial credit.

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack
   - Provide a description of what resources are built.
   - Diagram that assists with describing the CF template stack
      - See [Project 2 for diagram resources](../Project2/README.md)

2. Connections to instances within the VPC:
   - Description of purpose for configuring in `/etc/hosts` AND / OR `.ssh/config` files.
   - Explanation of entries in `/etc/hosts` AND / OR `.ssh/config` files.
   - Required setup to `ssh` among the instances
   - How to `ssh` among the instances using one or both of the above files for ease of use.

3. Setting up the HAProxy load balancing instance:
   - Explanation of file(s) that will need modified and general purpose of the file(s)
   - Snippets of haproxy configuration file or link to file in repo
   - Explanation of configuration file modifications
   - How to test the haproxy configuration file after revisions
   - Explanation and commands to manage the service (and when to run them)
```
Make sure to use markdown code blocks to properly format snippets
```

4. Setting up Host instances 1, 2, & 3
   - **see notes in [Web Site - Scope and Implementation](#web-site---scope-and-implementation)**
   - Document how to set the hosts to utilize your website, including method used to get site content to host instance and required location of site content

6. Prove in **two ways** that your load balancer is working:
   - Use the browser to show that the hosts in the pool are serving content.
        - Explain how the user can visually test that their load balancer is working
        - Provide screenshot(s) of the project working in your browser
        - Link to the Load Balancer Public IP
   - View `haproxy` logs to show requests being distributed and responses from different hosts in the pool.
      - **Valid logs viewers include**: 
         - following the `haproxy` log file with `tail`
         - enabling and viewing the `stats` page
         - `halog` on the `haproxy` log file   
      - **Deliverables**
        - Record and explain the command(s) to view the logs.
        - Take a screenshot of your logs proving load balancing among hosts in the pool is working

7. Troubleshooting
   - **Provide at least three recommendations** on what to troubleshoot if the load balancer is not working.  This can be at any point of the setup process.
   - Check that you have selected "Start Lab" is not sufficient to count as one ;)

8. Citations / resources used
   - if using generative AI, provide the tool name and the prompt(s) used
   - if using websites, provide the link and a short description of what you used on the page

## Resources and Warnings

- You **DO NOT** need to mess with UFW rules. You may lock yourself out of SSH access.
- You can have a maximum of **FIVE Elastic IP Addresses and FIVE VPCs**
- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [How to Install the Apache Web Server on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [How to Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [Introduction to HAProxy logging & parsing logs](https://www.haproxy.com/blog/introduction-to-haproxy-logging)
   - [Article from Sematext that covers similar things](https://sematext.com/blog/haproxy-logs/)
- [How to edit `/etc/hosts`](https://linuxize.com/post/how-to-edit-your-hosts-file/)
- [The SSH config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [How to SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
- [Create & Extract with `tar`](https://linuxize.com/post/how-to-create-and-extract-archives-using-the-tar-command-in-linux)

## Extra Credit - Hands Free - +10%

Have your CloudFormation template build everything out - configure haproxy to use the hosts & the hosts are configured with your site content, copy in `hosts` and / or `config files, etc.

Things your template should not do:
- copy a private key for ssh access among instances (this implies you would somehow expose your private key on GitHub)
- delete the NAT Gateway resource & associated EIP

## Extra Credit - HTTPS - +20%

Enable HTTPS (SSL encryption) for your load balancer.  I am going to leave some choice here of whether you have only your load balancer decrypt / encrypt packets for the hosts or have the hosts handle the decryption / encryption.

You will owe a very good write up on all elements involved to set up HTTPS.  A start, which mentions some additional things you'll need, is [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination)

### Useful HTTPS Resources
These are a collection of sites I used to set up HTTPS and get the correct SSL certificate (remember haproxy wants a "combo" file of the private and public cert)
- [Haproxy - HAProxy SSL Termination (Offloading) Everything You Need to Know](https://www.haproxy.com/blog/haproxy-ssl-termination)
- [Tecmint - How to Configure a CA SSL Certificate in HAProxy](https://www.tecmint.com/configure-ssl-certificate-haproxy/)
- [Linuxize - Creating an SSL certificate](https://linuxize.com/post/creating-a-self-signed-ssl-certificate/)
- [StackOverflow - haproxy - unable to load SSL private key from PEM file](https://stackoverflow.com/questions/27947982/haproxy-unable-to-load-ssl-private-key-from-pem-file)
- [Cloud 66 - Help - Remove passphrase from certificate key](https://help.cloud66.com/docs/security/remove-passphrase)

## Submission

1. Your repo should contain:
   - `YOURLASTNAME-cf.yml` (your modified CloudFormation template)
   - a folder with your website content
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   - Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Project3

3. **Only delete the NAT Gateway** once your project is complete.  I will turn on your AWS environments for grading to check the load balancer is operational.
   - Once project grades are posted you may return and delete the stack

## Rubric

[Rubric](Rubric.md)
