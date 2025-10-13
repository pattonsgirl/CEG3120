# Project 2

## Objectives:

- Create a CloudFormation to specification to remove manual creation
- Understand the role of Infrastructure as Code (IaC)

## Getting Started

For this project you need access to your AWS console. Return to LearnerLab and select "Start Lab".

**Once the icon next to "AWS" is green, click "AWS" to open the console.**

Create a `Project2` folder in your GitHub Classrooms repo. This project is mostly modifying a CloudFormation template, so you are welcome to work wherever you are comfortable. I would float towards VSCode myself.
 
## Project Description

I think we can agree that manually creating a VPC network to host an instance and the instance itself was a lot of menus to go through and things to check. If you were working for, say, a web development company, and you had to do that every time you got a new customer who wanted a webpage, there would be some frustrations. 

The "cloud" agrees, and therefore cloud services created templates. In AWS, these are called CloudFormation templates. In these files, you layout every detail of how you want your EC2 setup to be, from VPC to instance(s). AWS CloudFormation can take these files as input, and feed the values into API calls that create and configure the resources.

Create a folder in your repo named `Project2` that contains your deliverables:
- a **CloudFormation template named `YOURNAME-CF.yml`**.
  - A [base YAML template - `cf-template.yml`](cf-template.yml) has been provided for you. Due to how many things are in these templates, I would use this base and make the modifications requested. You can Google how these are defined the way they are, additional parameters, etc.
- a `README.md` file that includes:
  - a project description & any additional how-to notes you'd like to leave for future you
  - a visual **diagram** of the resources how they connect and a companion explanation to your visualization
    - creating your diagram with the CloudFormation template Designer **will not** count for credit
  - you are welcome to include notes in the `README.md` file if you need to write notes about your template for partial credit.

### Other notes: 
- If you prefer JSON, you may convert the provided template to JSON. Your deliverable would be the `json` file.
- Check out [CloudFormation Breakdown](../../CourseNotes/AWS-CF-Breakdown.md) for a breakdown of what is inside of these templates and what is in each section, as well as syntax notes and hints.
- I strongly recommend using Visual Studio Code. The YAML and CloudFormation extensions have not been super useful to me, but please share your experience. The CloudFormation Designer tool accessible via the AWS Console CloudFormation menu has been the most useful at debugging if needed.

### Project Taskings

1. `Description` & `Parameters` Settings:

   - Modify `Description` string to describe your template and what it creates
     - Example description:
     - `Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address`
   - Choose: leave or remove `SSH Location`.  If you leave it, it may not leave a default that would be a vulnerability.

2. `Mappings` Settings:

   - Adjust AMI to be the AMI of your choice (yes, it must be changed).
     - You can use the AMI from Project 1

3. `Resources` Settings:

    - VPC range to be `192.168.0.0/23`
    - Subnet range to be `192.168.0.0 - 192.168.0.255`
    - **"Tag" every resource with a "Name" - ex. `LASTNAME-CF-RESOURCE`**
      - Resources include the VPC, subnet, route table, internet gateway, elastic IP, security group, network acl, instance, etc..

4. `Security Group` Settings:

   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (CIDR block 130.108.0.0/16)
     - Instances within the VPC or subnet
   - Allow HTTP over port 80 from any IP source
   - Allow HTTP over port 8080 from any IP source


5. `Network ACL` Settings:

    - Add rule to deny outgoing requests to [wttr.in](https://wttr.in/)
      - For simplicity, you may deny any protocols and any port attempt to `wttr.in`

6. `Instance` settings:

   - Set a private IP in your subnet range
   - Using the configuration script (`UserData`) in the `cf-template`:
     1. Start by requesting all updates, and then performing any upgrades to latest versions
     2. Change `hostname` to "YOURLASTNAME-AMI" where `YOURLASTNAME` is your last name and where `AMI` is some identifier of the AMI you chose
     3. Install `git`, `python3`, `pip3`, `apache2`, `wamerican` and `docker`
        - Note these are the names of the executable once installed with the `apt` package manager - you'll need to find the correct package name & package repository manager per your AMI / Linux distribution
        - If you are using an AMI where the service needs to be **enabled and started**, add commands to so for `apache2` and `docker`
     4. Copy the raw contents of the following files to specific directories on the instance:
        - [wordle.sh](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project2/wordle.sh) to the default user's home directory
        - [index.html](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project2/index.html) to the default apache2 web content directory. This page will display when you use HTTP to connect to port 80 on your instance.
     5. Run the [wsukduncan/cheatsheet](https://hub.docker.com/r/wsukduncan/cheatsheet) image in detached mode bound to host port 8080 and container port 80. Use the appropriate flag to have the container restart automatically if the system is rebooted / if the docker service has an outage.
        - [Detached mode - Docker Docs](https://docs.docker.com/reference/cli/docker/container/run/#detach)
        - [Start containers automatically - Docker Docs](https://docs.docker.com/engine/containers/start-containers-automatically/)
     6. Reboot as the last instruction
     

7. Use the "CloudFormation" in the AWS console to test your CloudFormation template and make sure it builds an image per specification.  See [Identifying Success](#identifying-success)
   
   - If a stack fails during creation, associated resources (even if create was a success) will also be deleted (it is an all or nothing creation process)

8. Diagram:
   - Your diagram should lay out how all the above resources are connected and the settings that your resources are configured for.  You can think of how my in-class diagrams include boxes around difference resources and arrows noting what goes where (although my 9/27 diagram should never see the light of day).  I'm leaving some creative openness here.  I expect companion notes with your visualization to help someone understand what they are seeing.
       - creating your diagram with the CloudFormation Template Designer **will not** count for credit.  
   - Recommended diagramming resources: 
     - [Lucid Charts](https://www.lucidchart.com/pages/)
     - [Textographo](https://textografo.com/)
     - [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
     - [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
     - [mhlabs - CFN Diagram Generator](https://github.com/mhlabs/cfn-diagram)
     - PowerPoint and OneNote are still good choices

## Identifying Success

A successful stack will (once created) have an instance you can `ssh` into. Your instance created by the stack should have the specified software installed & the hostname changed via the configuration script.

Your instance should be hosting two different websites - one on port 80 (via the instance's apache install), one on port 8080 (via the container's apache install)

- You can check for installed software by querying its version once you `ssh` in
- You can check that hostname was changed by looking at the command prompt once you `ssh` in
- If something did not work, [try browsing the boot logs](https://www.cyberciti.biz/faq/ubuntu-view-boot-log/)
- You can check your firewalls (Security Group & Network ACLs) are working by testing resources running on the server or making requests to sites that should be blocked

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md` with 
      - Description of project
      - Diagram explaining project CF Template
      - Companion notes / descriptions for diagram

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBUSERNAME/blob/main/Projects/Project2

3. Do not leave stacks running. Once your template creates a stack and instance to specification successfully, you may delete the stack

## Rubric

[Rubric](Rubric.md)
