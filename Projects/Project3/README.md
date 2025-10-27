# Project 3

- [Objectives](#Objectives)
- [Project Description](#Project-Description)
  - [Provided Resources](#Provided-Resources)
- [Part 1 - Create a Docker Image](#part-1---create-a-docker-image)
- [Part 2 - CloudFormation Template TODOs](#part-2---cloudformation-template-todos)
- [Part 3 - Setup Proxy Server](#part-3---setup-proxy-server)
- [Part 4 - README](#part-4---readme)
- [Recommended Resources and Warnings](#recommended-resources-and-warnings)
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

6. Push your container image to a **public** DockerHub repository in your account.

Recommended: pull your container image and run it to test that it serves your web content.

**Do not forget to add citations in [Part 4](#part-4---README) of resources used.**

Documentation requirements will be listed in [Part 4](#part-4---README)

## Part 2 - CloudFormation Template TODOs

Your deliverable for this portion is only **your CloudFormation template**.

Copy [`lb-cf-template.yml`](lb-cf-template.yml) to your `Project3` folder.  Name it `YOURLASTNAME-lb-cf.yml`

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

## Part 3 - Setup Proxy Server

Configure your proxy server per the following requirements.  If you **could not perform** a task or your project is not functional, note what is / is not working and what you've tried for debugging in [Part 4](#part-4---README).  

**Do not forget to add citations in [Part 4](#part-4---README) of resources used.**

Configure the following in your `haproxy` configuration file

1. Create a frontend section named `lastname-frontend`
   - bind to host port `80`
   - define the default backend as `lastname-pool`

2. Create a backend section named `lastname-pool`
   - define a balancing algorithm (round robin is anticipated - others may be chosen)
      - [Haproxy - supported algorithms](https://www.haproxy.com/documentation/haproxy-configuration-manual/latest/#4.2-balance)
   - add your three hosts as servers in the pool.  Don't forget to define the port the application is running on the hosts.

3. Enable the `haproxy` statistics page with either a `frontend` section or a `listen` section

4. Validate your `haproxy` configuration file. Address errors if the message is not `Configuration file is valid`

5. Reload the `haproxy` service and confirm your load balancer is distributing traffic among the hosts in your pool.

6. View the logs and stats of the `haproxy` server via the following methods - your focus is on finding evidence that the algorithm is distrubuting among your hosts:
   - following the `haproxy` log file with `tail`
   - `halog` on the `haproxy` log file 
   - viewing the `stats` page

Recommended: generate traffic that actually puts your `haproxy` server to the test. [`hey` is a tiny program that sends some load to a web application](https://github.com/rakyll/hey). It is available in `apt` - have not looked up package name for other package managers. 

Add your `haproxy` configuration file to your `Project3` folder.

Documentation requirements will be listed in [Part 4](#part-4---README)

## Part 4 - README

In your `Project3` folder, create a `README.md` file.  This document will be an overall guide to your project.

Your documentation should be written with as though someone is using it as a guide to recreate your project (like a blog post would do).

If you could not complete a step or steps in any of the tasks above you document shortcomings / stuck points and note what is "research" on how the rest should be done for partial credit.

**Do not forget to add citations in your `README.md` of resources used.**

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack
   - Provide a description of what resources are built.
   - Diagram that assists with describing the CF template stack
      - See [Project 2 for diagram resources](../Project2/README.md)

2. Building a web service container:
   - Explanation and links to web site content
   - Explanation of and link to `Dockerfile`
   - Instructions to build and push container image to your DockerHub repository
      - Add instructions to create PAT && recommended PAT scope

3. Connections to instances within the VPC:
   - Description of purpose for configuring in `/etc/hosts` AND / OR `.ssh/config` files.
   - Explanation of entries in `/etc/hosts` AND / OR `.ssh/config` files.
   - Required setup to `ssh` among the instances
   - How to `ssh` among the instances using one or both of the above files for ease of use.

4. Setting up the HAProxy load balancing instance:
   - General pupose of and required location for the `haproxy` configuration file
   - Link to `haproxy` configuration file in repo
   - Explanation of added sections in configuration file
   - Explain how to test the haproxy configuration file after revisions but before reloading the service
   - Explain scenarios when your `haproxy` service needs to be controlled - start, stop, restart / reload.  Provide the command to control the `haproxy` service based on the scenario.

5. Prove the load balancer is working:
   - Link to the via Load Balancer Public IP
   - Use a mix of screenshots and explanitory text to prove that your load balancer is successfully **using your pool of hosts**
   - Use a mix of screenshots and explanitory text to prove that your load balancer is successfully **using the algorithm selected to distribute traffic**
   - Hint: remember being asked to look at logs and the statistics page in Part 3 - lean on this to help with "proof"

6. Citations / resources used
   - if using generative AI, provide the tool name and the prompt(s) used
   - if using websites, provide the link and a short description of what you used on the page

## Recommended Resources and Warnings

### AWS Notes
- You can have a maximum of **FIVE Elastic IP Addresses and FIVE VPCs**

### HAProxy Resources
- [An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [Testing your HAProxy Configuration](https://www.haproxy.com/blog/testing-your-haproxy-configuration)
- [HAProxy Stats Page - Guide to all metrics](https://www.haproxy.com/blog/exploring-the-haproxy-stats-page)
   - [HAProxy listen section x stats](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration#what-about-listen)
- [Introduction to HAProxy logging & parsing logs](https://www.haproxy.com/blog/introduction-to-haproxy-logging)
   - [Article from Sematext that covers similar things](https://sematext.com/blog/haproxy-logs/)

### Other Knowledge
- [How to edit `/etc/hosts`](https://linuxize.com/post/how-to-edit-your-hosts-file/)
- [The SSH config file](https://linuxize.com/post/using-the-ssh-config-file/)
- [How to SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
- [Generate HTTP traffic with `hey`](https://github.com/rakyll/hey)

## Extra Credit - Haproxy Container Image - +10%

Your project must have commits against the required work *before* doing the extra credit portions.

Create a folder in `Project3` called `haproxy`.

Copy in your `haproxy` configuration file.  Create a `Dockerfile` that will build from the [`haproxy` Official Iamge](https://hub.docker.com/_/haproxy/) and copies your `haproxy` configuration file to the default location for `haproxy` in the container filesystem.

Build and push a container image to a **public** DockerHub repository in your account (don't overwrite your website repository :wink:)

Modify your CloudFormation template to pull and run your `haproxy` container image - do not install `haproxy` to the instance.

Add a section to [Part 4](#part-4---README) explaining your additions.

## Extra Credit - HTTPS - +10%

Your project must have commits against the required work *before* doing the extra credit portions.

Enable HTTPS (SSL encryption) for your load balancer.  I am going to leave some choice here of whether you have only your load balancer decrypt / encrypt packets for the hosts or have the hosts handle the decryption / encryption.

A start, which mentions some additional things you'll need, is [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination)

Add a section to [Part 4](#part-4---README) explaining your additions.

### Useful HTTPS Resources
These are a collection of sites I used to set up HTTPS and get the correct SSL certificate (remember haproxy wants a "combo" file of the private and public cert)
- [Haproxy - HAProxy SSL Termination (Offloading) Everything You Need to Know](https://www.haproxy.com/blog/haproxy-ssl-termination)
- [Tecmint - How to Configure a CA SSL Certificate in HAProxy](https://www.tecmint.com/configure-ssl-certificate-haproxy/)
- [Linuxize - Creating an SSL certificate](https://linuxize.com/post/creating-a-self-signed-ssl-certificate/)
- [StackOverflow - haproxy - unable to load SSL private key from PEM file](https://stackoverflow.com/questions/27947982/haproxy-unable-to-load-ssl-private-key-from-pem-file)
- [Cloud 66 - Help - Remove passphrase from certificate key](https://help.cloud66.com/docs/security/remove-passphrase)

## Submission

1. Your repo should contain:
   - a folder named `web-content` with:
      - your web site files
      - your `Dockerfile`
   - `YOURLASTNAME-lb-cf.yml` (your modified CloudFormation template)
   - your `haproxy.cfg` file
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   - Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Project3

3. **Only delete the NAT Gateway** once your project is complete.  I will turn on your AWS environments for grading to check the load balancer is operational.
   - Once project grades are posted you may return and delete the stack

4. You may complete *one or both* of the extra credit offerings.

## Rubric

[Rubric](Rubric.md)
