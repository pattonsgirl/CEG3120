# Project 3

- [Objectives](#Objectives)
- [Project Description](#Project-Description)
  - [Provided Resources](#Provided-Resources)
- [Part 1 - Cloud Formation Template TODOs](#part-1---cloudformation-template-todos)
- [Part 2 - Setup Load Balancing TODOs](#part-2---setup-load-balancing-todos)
- [Resources and Warnings](#resources-and-warnings)
- [Extra Credit - HTTPS](#extra-credit---https)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives:

- Modify the CF template to meet updated requirements
- Run a website using `nginx` or `apache2` on hosts in the pool
- Configure `haproxy` as a load balancer / application delevery controller to direct traffic to the pool

## Project Description

In your repository, create a `Project3` folder.

For this project, you will have two deliverables:

1. CloudFormation template with modifications per project requirements
2. Documentation (and specified screenshots) for configuring the load balancer and hosts in the pool after stack creation. 

### Provided Resources

The following is provided in this project folder:

- [`lb-cf-template.yml`](lb-cf-template.yml)
  - Note: this templated is updated from previous versions to get you started on this project
- [`simple-site.tar.gz`](site.tar.gz)
  - A multi-file static site in a compressed tar archive

## Part 1 - CloudFormation Template TODOs

The CloudFormation template provided in this project folder is **updated from Project 2** to get you started on this project.

Your deliverable for this portion is only **your CloudFormation template**.

Modify the template in the following ways:

1. Use AMI of your choice (from P1/P2 for example)
2. VPC CIDR block: `172.18.0.0/23`
3. Public subnet range: `172.18.0.0 - 172.18.0.255`
4. Private subnet range: `172.18.1.0 - 172.18.1.255`
5. Modifications for Security Group:
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
   - *If doing Extra Credit* Add `https` rules in addition to `http` rules
6. For the load balancer (proxy) instance:
   - assign private IP on public subnet
   - install `haproxy`
   - configure a unique `hostname` on the instance
7. Create three total host instances (one is templated, two more need to be added)
   - tag each with a unique name
   - assign each a private IP on private subnet
   - configure a unique `hostname` on each instance
   - install `apache2` or `nginx` on each instance
       - depending on AMI, also perform steps to start & enable service 
   - download and extract to default site content directory [simple-site.tar.gz](https://github.com/pattonsgirl/CEG3120/raw/refs/heads/main/Projects/Project3/simple-site.tar.gz) on each instance
       - This tasking is **required** even if you plan to replace this content with your own site content in Part 2

**The deliverable for this part is the CloudFormation template in your Project 3 folder.**

## Part 2 - Setup Load Balancing TODOs

In your `Project3` folder, create a `README.md` file.  This document will focus on finishing configuration after your stack builds.

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack and what resources are created.
   - Create a **diagram** of how the load balancer works in context of the resources your CF template builds
      - See [Project 2 for diagram resources](../Project2/README.md)
2. `ssh` to instances with the VPC:
   - On each instance, configure `/etc/hosts` OR `.ssh/config`
   - Document how to `ssh` among the instances utilizing one (or both) files for ease of access
       - Your documentation should be sufficient that a reader understands how to set it up similarly for themselves
3. Setting up the HAProxy load balancing instance:
   - Explain files that will need modified and general purpose of each file
   - Explain the configuration blocks within each changed file
   - Explain how to restart the service after a configuration change
   - Resources used (websites)
4. Setting up Host instances 1, 2, & 3
   - If using your own site:
     - Document how to place your site content in the default content directory
   - If using `simple-site`'s content:
     - Document where changes need to be made to insert your last name where YOURLASTNAMEHERE text is
   - If changes were made:
       - Explain files that will need modified and general purpose of each file
       - Explain the configuration blocks within each changed file
   - Explain how to reload the browser after web content changes
   - Explain how to restart the service after a service configuration change
   - Resources used (websites)
6. Prove in two ways that your load balancer is working:
   - Use the browser to show that the hosts in the pool are taking turns serving content.  Options include:
      - Hosts have a unique word / phrase on the index.html page
      - Inspection of the cookie payload (if enabled) to show which host the content came from
      - **Delvierables**
        - Explain how the user can visually test that their load balancer is working based on your method choice and supporting documentation
        - Take a set of screenshots that show hosts rotating content serving.
   - View `haproxy` logs to show requests being dstirbuted and responses from different hosts in the pool.
      - **Deliverables**
        - Record and explain the command(s) to view the logs.
        - Take a screenshot of your logs proving load balancing among hosts in the pool is working

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

## Extra Credit - HTTPS

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
   - `README.md`

2. In Pilot, paste the link to your project folder.  
   - Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Project3

## Rubric

[Rubric](Rubric.md)
