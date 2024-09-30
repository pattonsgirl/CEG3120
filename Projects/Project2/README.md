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

Other notes: 
- If you prefer JSON, you may convert the provided template to JSON. Your deliverable would be the `json` file.
- Check out [CloudFormation Breakdown](../../CourseNotes/AWS-CF-Breakdown.md) for a breakdown of what is inside of these templates and what is in each section, as well as syntax notes and hints.
- I strongly recommend using Visual Studio Code. The YAML and CloudFormation extensions have not been super useful to me, but please share your experience. The CloudFormation Designer tool accessible via the AWS Console CloudFormation menu has been the most useful at debugging if needed.

1. Description Settings:

   - Modify `Description` string to describe your template and what it creates
     - Example description:
     - `Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address`
   - Choose: leave or remove `SSH Location`

2. Mappings Settings:

   - Adjust AMI to be the AMI of your choice (yes, it must be changed).
     - You can use the AMI from Project 1

3. Resources Settings:

   - Make the following modification for `Resources`
     - VPC range to be `172.18.0.0/23`
     - Subnet range to be `172.18.0.0 - 172.18.0.255`
     - "Tag" each resource with a "Name" - ex. `YOURNAME-CF-VPC`
       - Resources include the VPC, subnet, route table, internet gateway, elastic IP, security group, etc..

4. Security Group Settings:

   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (CIDR block 130.108.0.0/16)
     - Instances within the VPC or subnet
   - Allow HTTP access from any IP source

5. Network ACL Settings:
    - TODO: add NCAL & sample rules to template: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html
    - Deny outgoing requests to [wttr.in](https://wttr.in/)

7. Instance settings:

   - Set "Tag" "Name" to "LastName-CF-instance"
   - Set a private IP in your subnet range
   - Using the configuration script in the `cf-template` to also:
     - Change `hostname`
     - Install `git`, `python3`, `pip3`, `apache2`, and `wamerican`
       - Note these are the names of the executable once installed - you'll need to find the correct package name & package repository manager per your AMI / Linux distribution
     - Copy the raw contents of the following files to specific directories on the instance:
       - [wordle.sh](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project2/wordle.sh) to the default user's home directory
       - [index.html](https://raw.githubusercontent.com/pattonsgirl/CEG3120/refs/heads/main/Projects/Project2/index.html) to the default apache2 web content directory

8. Use the "CloudFormation" in the AWS console to test your CloudFormation template and make sure it builds an image per specification.  See [Identifying Success](#identifying-success)
   - If a stack fails during creation, associated resources (even if create was a success) will also be deleted (it is an all or nothing creation process)

8. Diagram:
   - how resources are connected.  I'm leaving some creative openness here.  You can combine an explanation to go with your visualization.
       - creating your diagram with the CloudFormation template Designer **will not** count for credit.  
   - Recommended diagramming resources: 
     - [Lucid Charts](https://www.lucidchart.com/pages/)
     - [Textographo](https://textografo.com/)
     - [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
     - [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
     - [mhlabs - CFN Diagram Generator](https://github.com/mhlabs/cfn-diagram)
     - PowerPoint and OneNote are still good choices

## Identifying Success

A successful stack will (once created) have an instance you can `ssh` into. Your instance created by the stack should have the specified software installed & the hostname changed via the configuration script.

- You can check for installed software by querying its version once you `ssh` in
- You can check that hostname was changed by looking at the command prompt once you `ssh` in
- If something did not work, [try browsing the boot logs](https://www.cyberciti.biz/faq/ubuntu-view-boot-log/)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md` with your diagram & companion notes

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBUSERNAME/blob/main/Projects/Project2

3. Do not leave stacks running. Once your template creates a stack and instance to specification successfully, you may delete the stack

## Rubric

[Rubric](Rubric.md)
