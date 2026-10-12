# Project 5 - Balance

**Due:** TBD, 11:59 PM. Late policy: 2-hour grace period, then -10% per day for up to 3 days. Work committed after that is not graded.

- [Objectives](#objectives)
- [Project Description](#project-description)
  - [Deliverables](#deliverables)
  - [Provided Resources](#provided-resources)
- [Part 1 - Create a Docker Image](#part-1---create-a-docker-image)
- [Part 2 - CloudFormation Template TODOs](#part-2---cloudformation-template-todos)
- [Part 3 - Setup Proxy Server](#part-3---setup-proxy-server)
- [Part 4 - README](#part-4---readme)
- [Testing and Proof](#testing-and-proof)
- [Formatting, Task Text, and Images](#formatting-task-text-and-images)
- [Commits, Sources, and AI](#commits-sources-and-ai)
- [Recommended Resources and Warnings](#recommended-resources-and-warnings)
- [Extra Credit - Haproxy Container Image](#extra-credit---haproxy-container-image---10) 
- [Extra Credit - HTTPS](#extra-credit---https---10)
- [Submission](#submission)
- [Rubric](Rubric.md)

## Objectives:

- Build a container image from Apache's httpd project with web content - publish it to DockerHub
- Modify the project CF template to meet requirements for this project
- Run the website container on hosts in the pool
- Configure `haproxy` as a load balancer / application delivery controller to direct traffic to the pool
- Test and prove that your load balancer distributes traffic across the pool

## Project Description

### Deliverables

In your **aws** repository (`ceg3120-aws-lastname-f26`) - not your basics repository - create a **top-level** folder named exactly `AWS-LB` containing:

1. `web-content/` - your website files and your `Dockerfile` ([Part 1](#part-1---create-a-docker-image))
2. `YOURLASTNAME-lb-cf.yml` - your CloudFormation template with modifications per project requirements ([Part 2](#part-2---cloudformation-template-todos))
3. `haproxy.cfg` - your `haproxy` configuration file ([Part 3](#part-3---setup-proxy-server))
4. `README.md` - named exactly this, so GitHub displays it when someone opens the folder ([Part 4](#part-4---readme))
5. `images/` - your screenshots and diagram

### Write about *your* build

- Document what **you** built, with your actual values: your names, IPs, AMI ID, image name, and commands. Don't leave placeholders like `YOURLASTNAME`, `ami-xxxxxxxx`, or `<YOUR_IP>`.
- Everything you document must match your template and your running stack.
- **If you could not complete a step**, note where you got stuck and what you tried for debugging. Notes that show research into how the rest should be done can earn **up to half** of that item's points - **as long as you clearly label them as research**, separate from what you implemented and tested.
- **Be honest about incomplete work.** If your CF template has issues or doesn't build, the deduction depends on how your README documents it:
   - **-10%** - the README indicates the work is complete
   - **-5%** - the README notes the areas where blockers were hit
   - **-2%** - the README notes the blockers, what you tried, and clearly delineates next steps that have not been tested, and your template's errors line up with what the README describes
- **If a link or instruction in this project doesn't work or doesn't make sense, ask before the deadline.** The intent of a requirement is never that something stays broken.

### Provided Resources

The following is provided in this project folder:

- [`lb-cf-template.yml`](lb-cf-template.yml)
  - Note: this template is updated from previous versions to get you started on this project
  - **The base template contains examples, not requirements.** Before submitting, remove every `TODO` comment, replace the template's description with your own, and replace the example values (CIDRs, IPs, the placeholder home IP `0.0.0.0/0` - left as-is, it opens SSH to the entire internet, the `git` install).

## Part 1 - Create a Docker Image

1. In your `AWS-LB` folder, create a folder named `web-content`.  The files that follow must exist in this folder.

2. Bring **or** create a website with:
   - a minimum of **two** html files (`index.html` and one other)
   - a minimum of **one** css file

   You may use generative AI to create a site per a theme, but you must **cite** which generative AI system you used and the prompt you fed to it.

3. Create a `Dockerfile` with the following two instructions:
   - Build from `httpd:2.4`
   - Copy all content in `web-content` into the container filesystem in the default web content directory for `httpd` 

4. Build and tag a container image using your `Dockerfile` as the build instructions

5. Login to DockerHub on the command line.  Use a Personal Access Token (PAT) instead of a password.
   - **Never commit your PAT** or paste it into your README - treat it like a password.

6. Push your container image to a **public** DockerHub repository in your account.

Recommended: pull your container image and run it to test that it serves your web content.

Documentation requirements will be listed in [Part 4](#part-4---readme). **Do not forget to cite resources used** - see [Commits, Sources, and AI](#commits-sources-and-ai).

## Part 2 - CloudFormation Template TODOs

Your deliverable for this portion is only **your CloudFormation template**.

Copy [`lb-cf-template.yml`](lb-cf-template.yml) to your `AWS-LB` folder.  Name it `YOURLASTNAME-lb-cf.yml`

If you **could not perform** a task via the CloudFormation template, document how you manually performed the task in [Part 4](#part-4---readme) for a partial credit opportunity.  You may specify your research into completing taskings as long as you highlight that it is research based - not something your project implemented.

`cfn-lint` (`pipx install cfn-lint`) checks a template for errors before you upload it. YAML is sensitive to indentation - one misplaced space stops the whole template from building.

Modify the template in the following ways:

1. Update the template's `Description` to describe what your template builds.

2. Use an AMI of your choice that is **Ubuntu 24 or newer** or **Amazon Linux 2 or newer**. Your `UserData` scripts must use the package manager and package names for **this** AMI.

3. VPC CIDR block: `192.168.0.0/23`

4. Public subnet range: `192.168.0.0/24` (`192.168.0.0 - 192.168.0.255`)

5. Private subnet range: `192.168.1.0/24` (`192.168.1.0 - 192.168.1.255`)

6. **Tag every resource with `Key: Name` and a value of `LASTNAME-LB-RESOURCE`, replacing `RESOURCE` with the resource type** - e.g. `Duncan-LB-VPC`, `Duncan-LB-PublicSubnet`, `Duncan-LB-NATGW`, `Duncan-LB-ProxySG`.
   - Resources: VPC, both subnets, internet gateway, NAT gateway, both route tables, both security groups, and all four instances.
   - Each instance needs a unique name - e.g. `Duncan-LB-Proxy`, `Duncan-LB-Host1`, `Duncan-LB-Host2`, `Duncan-LB-Host3`.

7. Modify the provided SecurityGroup for use with your **proxy** instance:
   - Allow `ssh` requests from within the VPC CIDR block (`192.168.0.0/23`)
   - Allow `ssh` requests from your home IP - a single address, `x.x.x.x/32`
   - Allow `ssh` requests from the Wright State IP block (`130.108.0.0/16`)
   - Allow `http` requests from any IP
   - *Optional* allow ICMP for `ping`
   - *If doing Extra Credit* add `https` rules **in addition to** `http` rules
   - No other rules may be open to `0.0.0.0/0`.

8. Create a second SecurityGroup for use with your **host pool** instances:
   - Allow `ssh` requests from your proxy instance - use the proxy's private IP as a `/32` (e.g. `192.168.0.10/32`)
   - Allow `http` requests from within the VPC CIDR block (`192.168.0.0/23`)
   - *Optional* allow ICMP for `ping`
   - *If doing Extra Credit* add `https` rules **in addition to** `http` rules
   - No rules may be open to `0.0.0.0/0` - the hosts are only reached through the proxy.

9. For the load balancer (proxy) instance:
   - use the SecurityGroup for your proxy instance
   - assign a private IP on the public subnet
   - use instance `UserData` to set a unique `hostname` that persists after reboot (use `hostnamectl set-hostname`) - e.g. `Duncan-proxy`
   - use instance `UserData` to install `haproxy`
      - depending on AMI, also perform steps to start & enable the service

10. Create three host instances (one is templated, two more need to be added). For each host:
    - use the SecurityGroup for your host pool instances
    - tag with a unique Name (see step 6)
    - assign a private IP on the private subnet
    - use instance `UserData` to set a unique `hostname` that persists after reboot (use `hostnamectl set-hostname`) - e.g. `Duncan-host1`
    - install docker (depending on AMI, also start & enable the service)
    - pull and run your DockerHub image in detached mode bound to host port 80 and container port 80. Use the appropriate flag to have the container restart automatically if the system is rebooted / if the docker service has an outage.
        - [Detached mode - Docker Docs](https://docs.docker.com/reference/cli/docker/container/run/#detach)
        - [Start containers automatically - Docker Docs](https://docs.docker.com/engine/containers/start-containers-automatically/)

**Don't hide failures.** The `UserData` scripts run with `#!/bin/bash -xe`, so the first command that fails stops the rest of the script. Don't add `|| true` to commands, and after the stack builds, read `/var/log/cloud-init-output.log` on each instance to confirm every step ran.

> Why no NACL?
> A VPC has a default NACL that the subnets are inherently associated with if no other NACL is specified. The default NACL has an Inbound Allow All traffic from any source and Outbound Allow All traffic to any source - this is sufficient for our purposes since Security Groups will still determine what new requests are allowed to get to the server.

Build a stack from your template in the CloudFormation console. If a stack fails during creation, all of its resources are deleted - the **Events** tab shows the first resource that failed and why. If you get a capacity error for an instance type in an Availability Zone, try another zone or wait - it usually clears within an hour - and tell the instructor if it persists.

**The deliverable for this part is the CloudFormation template in your AWS-LB folder.**

## Part 3 - Setup Proxy Server

Configure your proxy server per the following requirements.  If you **could not perform** a task or your project is not functional, note what is / is not working and what you've tried for debugging in [Part 4](#part-4---readme).  

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

6. View the logs and stats of the `haproxy` server via the following methods - your focus is on finding evidence that the algorithm is distributing among your hosts:
   - following the `haproxy` log file with `tail`
   - `halog` on the `haproxy` log file 
   - viewing the `stats` page

Recommended: generate traffic that actually puts your `haproxy` server to the test. [`hey` is a tiny program that sends some load to a web application](https://github.com/rakyll/hey). It is available in `apt` - look up the package name for other package managers.

Add your `haproxy` configuration file to your `AWS-LB` folder as `haproxy.cfg`.

Documentation requirements will be listed in [Part 4](#part-4---readme)

## Part 4 - README

In your `AWS-LB` folder, create a `README.md` file.  This document will be an overall guide to your project.

Your documentation should be written as though someone is using it as a guide to recreate your project (like a blog post would do).

If you could not complete a step or steps in any of the tasks above, document shortcomings / stuck points and label what is "research" on how the rest should be done for partial credit.

1. Project description
   - Provide an overview of the project goal
   - Provide a description of how to use the CF template to create a stack
   - Provide a description of what resources are built
   - **Diagram** of the CF template stack. At minimum, it should display the resources your CF template creates in terms of:
      - networking (subnets) & routes (include IGW and NAT GW)
      - firewalls (Security Groups)
      - instances (what is on what subnet, including NAT GW)
   - The diagram must **render on GitHub**: an embedded image (`![diagram](images/diagram.png)`), or a Mermaid diagram in a fenced ` ```mermaid ` code block. Check how it looks on GitHub after you push.
      - Diagram the AWS resources, not the sections of the template file (Parameters, Mappings, ...).
      - Creating your diagram with the CloudFormation Designer / Infrastructure Composer **will not** count for credit.
      - Paper drawings are accepted, but feedback will be to practice with a digital tool.
      - See [Project 4 for diagram resources](../Project4/README.md)
   - **Companion notes:** walk the reader through the *diagram* - the path a request takes from the internet, through the load balancer, to a host - and what each security group allows and why.

2. Building a web service container:
   - Explanation of and links to web site content
   - Explanation of and link to `Dockerfile`
   - Instructions to build and push the container image to your DockerHub repository
      - Add instructions to create a PAT and the recommended PAT scope
   - Link to the DockerHub repository with your site image

3. Connections to instances within the VPC:
   > While this project is changing to take more advantage of `docker`, you still need to acknowledge how to navigate around your instances. Play with using `/etc/hosts` AND / OR `.ssh/config` to simplify connecting among your systems.
   - Description of purpose for configuring `/etc/hosts` AND / OR `.ssh/config` files.
   - Explanation of entries in `/etc/hosts` AND / OR `.ssh/config` files.
   - Required setup to `ssh` among the instances
   - How to `ssh` among the instances using one or both of the above files for ease of use.
   - **Never commit your private key (`.pem`)** - add `*.pem` to your `.gitignore`.

4. Setting up the HAProxy load balancing instance:
   - General purpose of and required location for the `haproxy` configuration file
   - Link to `haproxy` configuration file in repo
   - Explanation of added sections in configuration file
   - Explain how to test the haproxy configuration file after revisions but before reloading the service
   - Explain scenarios when your `haproxy` service needs to be controlled - start, stop, restart / reload.  Provide the command to control the `haproxy` service based on the scenario.

5. Testing and proof - your screenshots and explanations. See [Testing and Proof](#testing-and-proof).

6. Sources - see [Commits, Sources, and AI](#commits-sources-and-ai).

## Testing and Proof

Build your stack, complete Part 3, then add these screenshots to `AWS-LB/images/` and embed each one in your README **with a sentence saying what it proves**.

If something in a `UserData` script did not work, check that instance's `/var/log/cloud-init-output.log`.

1. **Stack build** - the CloudFormation console showing your stack with status `CREATE_COMPLETE` (stack name visible), and the **Resources** tab listing your resources.
2. **SSH to the proxy** - an SSH session to the proxy's public IP with its hostname in the prompt.
3. **SSH among instances** - from the proxy, an SSH session to a host using your `.ssh/config` or `/etc/hosts` entry, with the host's hostname in the prompt.
4. **haproxy** - `systemctl status haproxy` showing the service active, and `haproxy -c -f <config file>` reporting `Configuration file is valid`.
5. **Host containers** - on a host, `docker ps` showing your image running with `0.0.0.0:80->80/tcp`, and `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container>` showing your restart policy.
6. **Hosts serve your site** - from the proxy, `curl` to **each** host's private IP returns your site.
7. **Load balancer serves your site** - a browser showing your site at `http://<proxy public IP>` - type the full `http://`, since browsers may switch to `https://`, which isn't open (unless you did the HTTPS extra credit).
8. **Traffic is distributed** - evidence that your load balancer is **using your pool of hosts** with **your selected algorithm**:
   - the `haproxy` stats page showing all three servers UP, with traffic spread across them
   - **and** log evidence - a `tail` of the `haproxy` log or `halog` output showing requests going to different hosts
   - **and** an explanation of how this evidence matches your balancing algorithm (e.g. round robin should spread requests evenly across the three hosts)

## Formatting, Task Text, and Images

- **Formatting:** your README should be easy to read on GitHub - headings, lists, code formatting for commands, file names, and IPs (`` `haproxy -c -f haproxy.cfg` `` or fenced code blocks), and tables that render. Poor formatting is up to a 10% deduction, scaled by severity - 10% if the document is illegible.
- **Task text:** do not leave project or rubric task text in your documentation. It muddles what your work was versus what the assignment tasking is, and is a 5% formatting deduction. Section headings are fine; pasting the instruction bullets or prompts is not.
- **Images:** every screenshot and your diagram must be **embedded** so it displays in your README on GitHub - not just uploaded to the repo. Use relative paths (`images/stats.png`), match the filename's capitalization exactly, and avoid spaces in filenames (or wrap the path in angle brackets: `![stats](<images/my stats.png>)`). After you push, open your README on GitHub and confirm every image appears. No embedded screenshots is a 5% deduction; some missing or not displaying is 2.5%.

## Commits, Sources, and AI

- **Commit as you work.** The project should be built up over **multiple small commits**, with messages that say what changed (e.g. "Add host pool security group"). One or two commits for the whole project, or messages like "update", "fixes", or "complete", lose points.
- **Cite your sources.** Cite every source you use - documentation, tutorials, forums, and AI tools - and say what you used it for. You may place citations next to the sections they relate to or in one Sources section.
   - if using generative AI, provide the tool name and the prompt(s) used
   - if using websites, provide the link and a short description of what you used on the page
   - A submission with no citations loses 10%.
- **Your work must be your own and must describe what you built.** Submissions that appear AI-generated without citation, or that describe work you didn't do, are held at 0 until you meet with the instructor.
- **Never commit secrets** - your `.pem` key or your DockerHub PAT. Add `*.pem` (and `.DS_Store`) to your `.gitignore`.

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

Create a folder in `AWS-LB` called `haproxy`.

Copy in your `haproxy` configuration file.  Create a `Dockerfile` that will build from the [`haproxy` Official Image](https://hub.docker.com/_/haproxy/) and copies your `haproxy` configuration file to the default location for `haproxy` in the container filesystem.

Build and push a container image to a **public** DockerHub repository in your account (don't overwrite your website repository :wink:)

Create a copy of your Project 5 CloudFormation template (`YOURLASTNAME-lb-cf.yml`, with your modifications per this project's requirements) named `yourlastname-nohands-cf.yml`. Modify that template to pull and run your `haproxy` container image - do not install `haproxy` to the instance.

Add a section to [Part 4](#part-4---readme) explaining your additions.

## Extra Credit - HTTPS - +10%

Your project must have commits against the required work *before* doing the extra credit portions.

Enable HTTPS (SSL encryption) for your load balancer.  I am going to leave some choice here of whether you have only your load balancer decrypt / encrypt packets for the hosts or have the hosts handle the decryption / encryption.

A start, which mentions some additional things you'll need, is [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination)

Add a section to [Part 4](#part-4---readme) explaining your additions.

### Useful HTTPS Resources
These are a collection of sites I used to set up HTTPS and get the correct SSL certificate (remember haproxy wants a "combo" file of the private and public cert)
- [Haproxy - HAProxy SSL Termination (Offloading) Everything You Need to Know](https://www.haproxy.com/blog/haproxy-ssl-termination)
- [Tecmint - How to Configure a CA SSL Certificate in HAProxy](https://www.tecmint.com/configure-ssl-certificate-haproxy/)
- [Linuxize - Creating an SSL certificate](https://linuxize.com/post/creating-a-self-signed-ssl-certificate/)
- [StackOverflow - haproxy - unable to load SSL private key from PEM file](https://stackoverflow.com/questions/27947982/haproxy-unable-to-load-ssl-private-key-from-pem-file)
- [Cloud 66 - Help - Remove passphrase from certificate key](https://help.cloud66.com/docs/security/remove-passphrase)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-aws-lastname-f26

   - Your `AWS-LB/` folder should contain:
     - `web-content/` with your web site files and your `Dockerfile`
     - `YOURLASTNAME-lb-cf.yml` (your modified CloudFormation template)
     - `haproxy.cfg`
     - `README.md`
     - `images/` with your screenshots and diagram
   - Open `AWS-LB/README.md` on GitHub and confirm every image displays.

2. In Pilot, paste the link to your project folder.  
   - Sample link: https://github.com/WSU-kduncan/ceg3120-aws-lastname-f26/blob/main/AWS-LB/README.md

3. **Do not delete your stack** when you finish - the instructor will turn on your AWS environment during grading to check the load balancer is operational. **Only delete the NAT Gateway** once your project is complete (it is charged by the hour).
   - Once project grades are posted you may return and delete the stack

4. You may complete *one or both* of the extra credit offerings.

## Rubric

[Rubric](Rubric.md)
