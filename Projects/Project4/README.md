# Project 4 - CF Template

**Due:** See Pilot, 11:59 PM. Late policy: 2-hour grace period, then -10% per day for up to 3 days. Work committed after that is not graded.

## Objectives:

- Create a CloudFormation to specification to remove manual creation
- Understand the role of Infrastructure as Code (IaC)
- Build, test, and prove that your infrastructure works as specified

## Getting Started

For this project you need access to your AWS console. Return to LearnerLab and select "Start Lab".

**Once the icon next to "AWS" is green, click "AWS" to open the console.**

This project is mostly modifying a CloudFormation template, so you are welcome to work wherever you are comfortable. I would float towards VSCode myself.

## Project Description

I think we can agree that manually creating a VPC network to host an instance and the instance itself was a lot of menus to go through and things to check. If you were working for, say, a web development company, and you had to do that every time you got a new customer who wanted a webpage, there would be some frustrations. 

The "cloud" agrees, and therefore cloud services created templates. In AWS, these are called CloudFormation templates. In these files, you layout every detail of how you want your EC2 setup to be, from VPC to instance(s). AWS CloudFormation can take these files as input, and feed the values into API calls that create and configure the resources.

## Deliverables

In your **aws** repository (`ceg3120-aws-lastname-f26`) - not your basics repository - create a **top-level** folder named exactly `AWS-CF` containing:

- `LASTNAME-CF.yml` - your CloudFormation template
  - A [base YAML template - `cf-template.yml`](cf-template.yml) has been provided for you. Due to how many things are in these templates, I would use this base and make the modifications requested. You can Google how these are defined the way they are, additional parameters, etc.
  - If you prefer JSON, you may convert the provided template to JSON. Your deliverable would be `LASTNAME-CF.json`.
- `README.md` - named exactly this, so GitHub displays it when someone opens the folder. See [README.md file](#8-readmemd-file).
- `images/` - your screenshots and your diagram

### Other notes: 
- Check out [CloudFormation Breakdown](../../CourseNotes/AWS-CF-Breakdown.md) for a breakdown of what is inside of these templates and what is in each section, as well as syntax notes and hints.
- I strongly recommend using Visual Studio Code. The YAML and CloudFormation extensions have not been super useful to me, but please share your experience.
- `cfn-lint` (`pipx install cfn-lint`) checks a template for errors before you upload it. YAML is sensitive to indentation - one misplaced space stops the whole template from building.
- **The base template contains examples, not requirements.** Before submitting, remove every `TODO` comment, the example packages (`htop`, `sl`), and the `hello.txt` line, and replace every description (template, security group) with your own.
- **If a link or instruction in this project doesn't work or doesn't make sense, ask before the deadline.** The intent of a requirement is never that something stays broken.

### Project Taskings

1. `Description` & `Parameters` Settings:

   - Modify `Description` string to describe your template and what it creates
     - Example description:
     - `Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address`
   - Choose: leave or remove `SSHLocation`.
     - If you leave it, its default must be your home IP as a `/32`, or have no default (the stack then asks for it at launch).
     - A default of `0.0.0.0/0` is a vulnerability: anyone who launches the stack and accepts the default opens SSH to the entire internet, where automated scanners find it within minutes.

2. `Mappings` Settings:

   - Change the AMI to the AMI of your choice (yes, it must be changed from the base template's AMI).
     - You can use the AMI from Project 3
     - Your UserData script (step 6) must use the package manager and package names for **this** AMI.

3. `Resources` Settings:

    - VPC range to be `192.168.0.0/23`
    - Subnet range to be `192.168.0.0/24` (`192.168.0.0 - 192.168.0.255`)
    - **Tag every resource with `Key: Name` and a value of `LASTNAME-CF-RESOURCE`, replacing `RESOURCE` with the resource type**
      - Example: `Duncan-CF-VPC`, `Duncan-CF-Subnet`, `Duncan-CF-SG`
      - Resources: VPC, subnet, internet gateway, route table, Elastic IP, security group, network ACL, instance
      - The console only displays a tag whose key is `Name`. If every resource has the same name, you can't tell them apart.

4. `Security Group` Settings:

   - Allow SSH **and** ICMP from each trusted source network:
     - Your home / where you usually connect to your instances from - a single address, `x.x.x.x/32`
     - Wright State (addresses in CIDR block `130.108.0.0/16`)
     - Instances within the VPC - the VPC CIDR `192.168.0.0/23` (not the subnet's `/24`)
   - Allow HTTP over port 80 from any IP source
   - Allow HTTP over port 8080 from any IP source
   - Do not keep the base template's example rules - no other rules may be open to `0.0.0.0/0`.

5. `Network ACL` Settings:
    - NACL rules are evaluated **lowest rule number first**, and the first match wins. Number your deny rules **below** your allow rules (e.g. deny #90, allow #100), or they never apply.
    - Inbound & Outbound: keep a rule that `Allow`s any IP (v4 only is sufficient) on all ports. Without it, the default `*` rule denies everything.
    - Deny inbound SSH (TCP port 22) from `107.23.4.178/32` (this is another AWS instance I have in another class)
    - Deny outbound connections on any port to [wttr.in](https://wttr.in/)
      - NACL rules need an IP, not a hostname. Look it up with `dig +short wttr.in` (or `nslookup wttr.in`) and deny that address as a `/32`.

6. `Instance` settings:

   - Set a private IP in your subnet range
   - Using the configuration script (`UserData`) in the `cf-template`:
     1. Start by requesting all updates, and then performing any upgrades to latest versions
     2. Change `hostname` to "YOURLASTNAME-AMI" where `YOURLASTNAME` is your last name and where `AMI` is some identifier of the AMI you chose (e.g. `Duncan-Ubuntu24`, `Duncan-AL2023`)
        - The hostname must survive the reboot at the end of the script - use `hostnamectl set-hostname`.
     3. Install `git`, `python3`, `pip3`, `apache2`, `wamerican` and `docker`
        - These are the names of the executables / packages on Ubuntu. Use the correct package names & package manager for your AMI:

          | Requirement | Ubuntu (`apt-get`) | Amazon Linux 2023 (`dnf`) |
          |---|---|---|
          | git | `git` | `git` |
          | python3 / pip3 | `python3`, `python3-pip` | `python3`, `python3-pip` |
          | apache2 | `apache2` | `httpd` |
          | wamerican | `wamerican` | `words` |
          | docker | `docker.io` (or Docker's install script) | `docker` |

        - If you are using an AMI where the service needs to be **enabled and started**, add commands to do so for `apache2` and `docker`
     4. Copy the raw contents of the following files to specific directories on the instance with `wget -O` or `curl -fsSL -o`, using **these raw URLs**:
        - [wordle.sh](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project4/wordle.sh) to the default user's home directory
          - `https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project4/wordle.sh`
          - The script must be **owned by the default user** and **executable** - UserData runs as root, so files it downloads are owned by root.
        - [index.html](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project4/dockerfile-demo/index.html) to the default apache2 web content directory. This page will display when you use HTTP to connect to port 80 on your instance.
          - `https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project4/dockerfile-demo/index.html`
          - Note: you may bring in any index file **BUT** download it with `wget` or `curl`. 
        - Avoid hard coding (copy / pasting) file contents in your template - it will rarely go well.
        - A `github.com/.../blob/...` link downloads GitHub's web page, not the file - use the `raw.githubusercontent.com` URL.
        - Your course repository is private - the instance has no credentials to download from it.
     5. Run the [wsukduncan/cheatsheet](https://hub.docker.com/r/wsukduncan/cheatsheet) image in detached mode bound to host port 8080 and container port 80. Use the appropriate flag to have the container restart automatically if the system is rebooted / if the docker service has an outage.
        - [Detached mode - Docker Docs](https://docs.docker.com/reference/cli/docker/container/run/#detach)
        - [Start containers automatically - Docker Docs](https://docs.docker.com/engine/containers/start-containers-automatically/)
     6. Reboot as the last instruction
   - **Don't hide failures.** The script runs with `#!/bin/bash -xe`, so the first command that fails stops the rest of the script. Don't add `|| true` to commands, use `curl -f` so a failed download is noticed, and after the stack builds, read `/var/log/cloud-init-output.log` to confirm every step ran.

7. Use the "CloudFormation" in the AWS console to build a stack from your template and make sure it builds per specification. Then complete [Testing and Proof](#testing-and-proof).
   
   - If a stack fails during creation, associated resources (even if create was a success) will also be deleted (it is an all or nothing creation process). The **Events** tab shows the first resource that failed and why.
   - If you get a capacity error for an instance type in an Availability Zone, try another zone or wait - it usually clears within an hour - and tell the instructor if it persists.

8. `README.md` file
  - **Description:** detail what *your* CF template does - what someone gets by running it and how it's set up. This should be sufficient that someone looking at your repo can get a quick summary of what your template will get them. It must match your template.
  - **Diagram:** lay out the AWS resources - internet gateway, VPC, subnet, route table, network ACL, security group, Elastic IP, instance, and the two web services - and how traffic flows between them, with the settings your resources are configured for. You can think of how my in-class diagrams include boxes around different resources and arrows noting what goes where. I'm leaving some creative openness here.
    - The diagram must **render on GitHub**: an embedded image (`![diagram](images/diagram.png)`), or a Mermaid diagram in a fenced ` ```mermaid ` code block. Check how it looks on GitHub after you push.
    - Diagram the AWS resources, not the sections of the template file (Parameters, Mappings, ...).
    - Creating your diagram with the CloudFormation Designer / Infrastructure Composer **will not** count for credit.  
    - Recommended diagramming resources: 
      - [Lucid Charts](https://www.lucidchart.com/pages/)
      - [Textographo](https://textografo.com/)
      - [Mermaid - markdown diagrams](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
      - [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
      - [mhlabs - CFN Diagram Generator](https://github.com/mhlabs/cfn-diagram)
      - PowerPoint and OneNote are still good choices
  - **Companion notes:** walk the reader through the *diagram* - the path traffic takes into your instance, and what each NACL and security group rule does and why.
  - **Testing and proof:** your screenshots - see [Testing and Proof](#testing-and-proof).
  - **Sources:** cite every source you used, including AI tools, and say what you used each one for.

## Testing and Proof

Build your stack, then add these screenshots to `AWS-CF/images/` and embed each one in your README **with a sentence saying what it proves**:

1. **Stack build** - the CloudFormation console showing your stack with status `CREATE_COMPLETE` (stack name visible), and the **Resources** tab listing your resources.
2. **SSH and hostname** - an SSH session to your Elastic IP with your new hostname in the prompt, plus the output of `hostnamectl`.
3. **Installed software** - versions from `git --version`, `python3 --version`, `pip3 --version`, `apache2 -v` (or `httpd -v`), `docker --version`, and proof the word list exists (`ls /usr/share/dict/words`).
4. **wordle.sh permissions** - as the **default user, without `sudo`**:
   - `ls -l ~/wordle.sh` showing the default user as owner and the `x` (execute) permission
   - `./wordle.sh` running and accepting at least one guess
5. **Docker container**:
   - `docker ps` (as the default user, without `sudo` - log out and back in after adding the user to the `docker` group) showing `wsukduncan/cheatsheet` running with `0.0.0.0:8080->80/tcp`
   - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container>` showing your restart policy
   - a browser showing `http://<Elastic IP>:8080`
   - a browser showing `http://<Elastic IP>` (port 80, your `index.html`) - type the full `http://`, since browsers may switch to `https://`, which isn't open
6. **Security group tests** - one **allowed** and one **blocked** test:
   - allowed: `ping` and `ssh` to your Elastic IP from home or campus succeed
   - blocked: the same `ping` from a network that is **not** in your rules (e.g. a phone hotspot) times out
7. **Network ACL tests** - from the instance:
   - `curl -m 5 wttr.in` times out
   - `curl -I http://example.com` returns `200 OK` (so you know outbound works in general)
   - for the `107.23.4.178` SSH deny, which you can't test from that address, a screenshot of your NACL's inbound rules in the console

If something did not work, [try browsing the boot logs](https://www.cyberciti.biz/faq/ubuntu-view-boot-log/) - `/var/log/cloud-init-output.log` has the output of your UserData script.

## Commits, Sources, and AI

- **Commit as you work.** The project should be built up over **multiple small commits**, with messages that say what changed (e.g. "Add SG rules for SSH/ICMP from WSU and VPC"). One or two commits for the whole project, or messages like "update", "fixes", or "complete", lose points.
- **Cite your sources.** Cite every source you use - documentation, tutorials, forums, and AI tools - in your README's Sources section, and say what you used it for. A submission with no citations loses points.
- **Your work must be your own and must match your template.** Submissions that appear AI-generated, or whose README describes work that isn't in the template, are held at 0 until you meet with the instructor.
- **Never commit key files** (`*.pem`) to a repository, even a private one - add `*.pem` (and `.DS_Store`) to your `.gitignore`. Your Learner Lab `labsuser.pem` can't be rotated, so a committed copy can't be undone.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-aws-lastname-f26

   - Your `AWS-CF/` folder should contain:
     - `LASTNAME-CF.yml`
     - `README.md` with 
        - Description of project
        - Diagram explaining project CF Template
        - Companion notes / descriptions for diagram
        - Testing and proof screenshots
        - Sources
     - `images/` with your screenshots and diagram

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-aws-lastname-f26/blob/main/AWS-CF/README.md

3. Do not leave stacks running. Once your template creates a stack and instance to specification successfully, and you have your screenshots, you may delete the stack

## Rubric

[Rubric](Rubric.md)
