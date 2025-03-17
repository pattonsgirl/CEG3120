# Project 3

- [Objectives](#Objectives)
- [Project Description](#Project-Description)
  - [Provided Resources](#Provided-Resources)
  - [Web Site - Scope and Implementation](#web-site---scope-and-implementation)
- [Part 1 - Cloud Formation Template TODOs](#part-1---cloudformation-template-todos)
- [Part 2 - Setup Load Balancing TODOs](#part-2---setup-load-balancing-todos)
- [Resources and Warnings](#resources-and-warnings)
- [Extra Credit - HTTPS](#extra-credit---https---20)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives:

- Modify the CF template to meet updated requirements
- Run a website using `nginx` or `apache2` on hosts in the pool
- Configure `haproxy` as a load balancer / application delivery controller to direct traffic to the pool

## Project Description

In your repository, create a `Project3` folder.

For this project, you will have three required deliverables:

1. CloudFormation template with modifications per project requirements
2. Folder with your website files
3. Documentation (and specified screenshots) for configuring the load balancer and hosts in the pool after stack creation. 
4. Optional - compressed folder with your site files (`.tar.gz`) 

### Provided Resources

The following is provided in this project folder:

- [`lb-cf-template.yml`](lb-cf-template.yml)
  - Note: this templated is updated from previous versions to get you started on this project

### Web Site - Scope and Implementation

You may - and are encouraged to - bring your own site just to make grading more fun.

Your site must contain a minimum of:

- an index.html file
- .css file(s) and / or image file(s) referred to by your .html file(s)

You may use generative AI to create these, but you must cite the generative AI used and the prompt fed to it.

There are three choices of setting up your site on your host.  I am ordering these from best choice to "completed the task" choice.
1. Create a compressed version of your site files (usually a `.tar.gz`).  Download it via your CF template to the hosts, then extract it to the default content directory for `apache`
2. Download your site files from your GitHub repo to your host to the default content directory for `apache`
3. Sign in to each host after the CF template builds you stack and download your site content to the default content directory for `apache`

## Part 1 - CloudFormation Template TODOs

Your deliverable for this portion is only **your CloudFormation template**.

If you **could not perform** a task via the Cloud Formation template, you'll need to document how you manually performed the task during Part 2 for a partial credit opportunity.

Modify the template in the following ways:

1. Use AMI of your choice (from P1/P2 for example)
2. VPC CIDR block: `172.18.0.0/23`
3. Public subnet range: `172.18.0.0 - 172.18.0.255`
4. Private subnet range: `172.18.1.0 - 172.18.1.255`
5. Modifications for Security Group:
   - Allow `ssh` requests within VPC CIDR block
   - Allow `ssh` requests from your home IP
   - Allow `ssh` requests from Wright State IP block (`130.108.0.0/16`)
   - Allow `http` requests from within VPC CIDR block
   - Allow `http` requests from any IP
   - *If doing Extra Credit* Add `https` rules in addition to `http` rules
6. For the load balancer (proxy) instance:
   - assign private IP on the public subnet
   - configure a unique `hostname` on the instance
   - install `haproxy`
      - depending on AMI, also perform steps to start & enable service
7. Create three total host instances (one is templated, two more need to be added)
   - tag each with a unique name
   - assign each a private IP on the private subnet
   - configure a unique `hostname` on each instance
   - install `apache2` or `nginx` on each instance
       - depending on AMI, also perform steps to start & enable service 
   - **see notes in [Web Site - Scope and Implementation](#web-site---scope-and-implementation)**

**The deliverable for this part is the CloudFormation template in your Project 3 folder. Do not forget to add citations to this portion if additional resources were used.**

## Part 2 - Setup Load Balancing TODOs

In your `Project3` folder, create a `README.md` file.  This document will focus on finishing configuration after your stack builds.

Your documentation should be written with as though someone is using it as a guide to recreate your project (like a blog post would do).

**You will not receive credit if your documentation copies all of my bullets and plugs answers in after them.**

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack and what resources are built.
   - Create a **diagram** of how the load balancer works in context of the resources your CF template builds
      - See [Project 2 for diagram resources](../Project2/README.md)

2. `ssh` to instances with the VPC:
   - On each instance, configure `/etc/hosts` AND / OR `.ssh/config`.  Explain your entries in either or both files.
   - Document how to `ssh` among the instances utilizing one (or both) files for ease of access
       - Your documentation should be sufficient that a reader understands how to set it up similarly for themselves

3. Setting up the HAProxy load balancing instance:
   - Explain files that will need modified and general purpose of each file
   - Explain the configuration blocks within each changed file
   - Explain how to restart the service after a configuration change

4. Setting up Host instances 1, 2, & 3
   - **see notes in [Web Site - Scope and Implementation](#web-site---scope-and-implementation)**
   - Document how to set the host to utilize your website (or where to make changes so that the user of you documentation can customize your setup with their own)
   - Explain how to restart the service after a service configuration change

6. Prove in **two ways** that your load balancer is working:
   - Use the browser to show that the hosts in the pool are serving content.
        - Explain how the user can visually test that their load balancer is working and how to troubleshoot if it is not
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

7. Troubleshooting and warnings
   - What are some troubleshooting guidelines the user should look for if something "isn't working"
   - Does your template create anything the user should change or be warned about?

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

3. **Only delete** the NAT Gateway once your project is complete.  I will turn on your AWS environments for grading to check the load balancer is operational.
   - Once project grades are posted you may return and delete the stack

## Rubric

[Rubric](Rubric.md)
