# Project 5 Rubric

## Project Score: / 80

Grading notes:
- 1 point per box unless noted.
- Research-only notes for an unfinished step (clearly labeled as research) earn up to half of that item's points.
- Documented values (AMI, IPs, names, commands) must match your template and your running stack.

## Required Documents ( / 5)

In `AWS-LB/`:
- a folder named `web-content` with:
   - [ ] your web site files (at least two `.html` files, including `index.html`, and one `.css` file)
   - [ ] `Dockerfile`
- [ ] `YOURLASTNAME-lb-cf.yml` 
- [ ] `haproxy.cfg` file
- [ ] `README.md`

## Dockerfile & Image ( / 3)

- [ ] Builds from `httpd:2.4`
- [ ] Copies the content of `web-content` into the default web content directory for `httpd` (`/usr/local/apache2/htdocs/`)
- [ ] Image pushed to a **public** DockerHub repository, and it is the image the hosts run

## haproxy configuration file ( / 11)

- [ ] Creates a frontend section named `lastname-frontend`
   - [ ] binds to host port `80`
   - [ ] defines the default backend as `lastname-pool`
- [ ] Creates a backend section named `lastname-pool`
   - [ ] defines a balancing algorithm (2 pts)
   - servers in the pool, each with the port the application runs on:
      - [ ] host 1
      - [ ] host 2
      - [ ] host 3
- [ ] Enables the `haproxy` statistics page with a `frontend` or `listen` section (2 pts)

## CloudFormation template ( / 24)

- [ ] Template description revised to describe what the template builds (no `TODO`, no base-template text)
- [ ] AMI changed to Ubuntu 24 or newer, or Amazon Linux 2 or newer
- [ ] VPC CIDR block: `192.168.0.0/23`
- [ ] Public subnet range: `192.168.0.0/24`
- [ ] Private subnet range: `192.168.1.0/24`
- `Name` tag `LASTNAME-LB-<resource type>`:
   - [ ] on the networking resources - VPC, both subnets, internet gateway, NAT gateway, both route tables (0.5 pt)
   - [ ] on both security groups (0.5 pt)
- Security Group for the proxy instance (no rules open to `0.0.0.0/0` except HTTP):
   - [ ] `ssh` from within the VPC CIDR block (`192.168.0.0/23`)
   - [ ] `ssh` from your home IP (`/32`)
   - [ ] `ssh` from the Wright State IP block (`130.108.0.0/16`)
   - [ ] `http` from any IP
- Security Group for the host pool instances (no rules open to `0.0.0.0/0`):
   - [ ] `ssh` from the proxy instance's private IP (`/32`)
   - [ ] `http` from within the VPC CIDR block (`192.168.0.0/23`)
- Load balancer (proxy) instance:
   - [ ] uses the proxy Security Group
   - [ ] tagged with a unique Name Value
   - [ ] assigned a private IP on the public subnet
   - [ ] `UserData` sets a unique `hostname` that persists after reboot
   - [ ] `UserData` installs `haproxy` (enabled and started as needed for the AMI) (2 pts)
- Host pool instances - each box requires **all three** hosts:
   - [ ] use the host pool Security Group
   - [ ] tagged with unique Name Values
   - [ ] assigned private IPs on the private subnet
   - [ ] `UserData` sets a unique `hostname` on each that persists after reboot
   - [ ] `UserData` installs `docker` (enabled and started as needed for the AMI)
   - [ ] `UserData` pulls and runs your web site image detached (`-d`), with a restart policy (`always` / `unless-stopped`), bound to host port 80 and container port 80

## Testing & Proof ( / 16)

Screenshots embedded in the README, each with a sentence saying what it proves.

- [ ] Stack build - status `CREATE_COMPLETE` (stack name visible) and the Resources tab
- [ ] SSH to the proxy's public IP with its hostname in the prompt
- [ ] SSH from the proxy to a host using your `.ssh/config` or `/etc/hosts` entry, with the host's hostname in the prompt
- [ ] `haproxy` service active (`systemctl status haproxy`) and `haproxy -c -f <config file>` reporting `Configuration file is valid` (2 pts)
- [ ] On a host: `docker ps` showing your image on `80->80` and its restart policy (`docker inspect`)
- [ ] From the proxy: `curl` to **each** host's private IP returns your site (2 pts)
- [ ] Your site loading in a browser at `http://<proxy public IP>` (2 pts)
- Traffic distributed across your pool by your algorithm:
   - [ ] `haproxy` stats page showing all three servers UP, with traffic spread across them (2 pts)
   - [ ] log evidence - a `tail` of the `haproxy` log or `halog` output showing requests going to different hosts (2 pts)
   - [ ] explanation of how the evidence matches your balancing algorithm (2 pts)

## README.md documentation ( / 21)

1. Project description:
   - [ ] Overview of the project goal
   - [ ] How to use the CF template to create a stack
   - [ ] What resources are built
2. Diagram:
   - [ ] Embedded and renders on GitHub (a photo of a paper drawing is accepted; feedback recommends a digital tool)
   - Shows the stack in terms of:
      - [ ] networking (subnets) & routes (including the IGW and NAT GW)
      - [ ] firewalls (Security Groups)
      - [ ] instances (what is on what subnet, including the NAT GW)
   - [ ] Companion notes that explain the diagram, including how a request reaches a host through the load balancer
3. Building a web service container:
   - [ ] Explanation of and links to web site content
   - [ ] Explanation of and link to `Dockerfile`
   - [ ] Instructions to build and push the container image to your DockerHub repository, including creating a PAT and the recommended PAT scope
   - [ ] Link to the DockerHub repository with your site image
4. Connections to instances within the VPC:
   - [ ] Purpose of configuring `/etc/hosts` AND / OR `.ssh/config`
   - [ ] Explanation of your entries in `/etc/hosts` AND / OR `.ssh/config`
   - [ ] Required setup to `ssh` among the instances
   - [ ] How to `ssh` among the instances using one or both of the above files
5. Setting up the HAProxy load balancing instance:
   - [ ] General purpose of and required location for the `haproxy` configuration file
   - [ ] Link to the `haproxy` configuration file in the repo
   - [ ] Explanation of the added sections in the configuration file
   - [ ] How to test the configuration file after revisions but before reloading the service
   - [ ] Scenarios when the `haproxy` service needs to be controlled (start, stop, restart / reload), with the command for each

## Extra Credit - HAProxy Container Image

Worth +10%. Your project must have commits against the required work *before* the extra credit work. If documentation requirements are not complete, no extra credit will be awarded.

- [ ] Explanation of and link to the haproxy configuration file
- [ ] Explanation of and link to the `Dockerfile`
- [ ] Link to the DockerHub repository with your haproxy container
- [ ] Link to your `yourlastname-nohands-cf.yml` 
   - [ ] Notes on the difference(s) between it and `YOURLASTNAME-lb-cf.yml` 

## Extra Credit - Setup HTTPS 

Worth +10%. Your project must have commits against the required work *before* the extra credit work. If documentation requirements are not complete, no extra credit will be awarded.

- [ ] Creating a self-signed certificate
- [ ] Changes to `YOURLASTNAME-lb-cf.yml` to enable HTTPS (`https` rules **in addition to** the `http` rules on both security groups as needed)
- [ ] `haproxy` requirements to handle HTTPS
- [ ] Server configuration changes to handle HTTPS
- [ ] Screenshot(s) proving HTTPS is operational

## Point Deductions - Penalty Total: 

- Incomplete work - the CF template has apparent issues or doesn't build (fails validation, or no `CREATE_COMPLETE` proof). Apply **one** tier, based on how the README documents it:
   - [ ] 10% penalty - README indicates the work is complete
   - [ ] 5% penalty - README notes the areas where blockers were hit
   - [ ] 2% penalty - README notes the blockers, the things tried, and clearly delineates next steps that have not been tested; the CF template's errors are in line with what the README describes (it may not build)
- [ ] Security Group has additional rules that make it too open - 1 point penalty per rule
- [ ] images not included in markdown documentation - 5% penalty (no screenshots embedded); 2.5% penalty (some screenshots missing or not displaying) - the diagram is scored under README documentation
- [ ] poor markdown formatting - up to 10% penalty, scaled by severity (10% = illegible)
    - includes project / rubric tasking text left in the documentation - 5% penalty
- [ ] Single or mass commit - project not built up over multiple small, descriptive commits - 5% penalty
- [ ] No citations - sources (including AI tools, with the prompts used) not cited - 10% penalty
- [ ] Late submission - 10% per day, up to 3 days
- [ ] Submission appears AI-generated without citation or describes work not done - score held at 0 pending an instructor meeting

Percentage deductions are taken from the total possible (e.g. 10% of 80 = 8).
