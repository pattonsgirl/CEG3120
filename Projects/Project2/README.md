# Project 2

## Objectives:

- Create a CloudFormation to specification to remove manual creation
- Understand the role of Infrastructure as Code (IaC)

## Getting Started

For this project you need access to your AWS console. Return to LearnerLab and select "Start Lab".

**Once the icon next to "AWS" is green, click "AWS" to open the console.**

Create a `Project2` folder in your GitHub Classrooms repo. This project is mostly modifying a CloudFormation template, so you are welcome to work wherever you are comfortable. I would float towards VSCode myself.

You are welcome to include notes in a README.md file in your folder in your repo if you need to write notes for partial credit.

## Project Description

I think we can agree that manually creating a VPC network to host an instance and the instance itself was a lot of menus to go through and things to check. If you were working for, say, a web development company, and you had to do that every time you got a new customer who wanted a webpage, there would be some frustrations. 

The "cloud" agrees, and therefore cloud services created templates. In AWS, these are called CloudFormation templates. In these files, you layout every detail of how you want your EC2 setup to be, from VPC to instance(s). AWS CloudFormation can take these files as input, and feed the values into API calls that create and configure the resources.

Your deliverables are:
- a **CloudFormation template named `YOURNAME-CF.yml`**. A [base YAML template - `cf-template.yml`](cf-template.yml) has been provided for you. Due to how many things are in these templates, I would use this base and make the modifications requested. You can Google how these are defined the way they are, additional parameters, etc.
- a **diagram** of the resources how they connect (and any companion explanation to your visualization)

Other notes: 
- If you prefer JSON, you may convert the provided template to JSON. Your deliverable would be the `json` file. Have fun ;)
- Check out [CloudFormation Breakdown](../../CourseNotes/AWS-CF-Breakdown.md) for a breakdown of what is inside of these templates and what is in each section, as well as syntax notes and hints.
- I strongly recommend using Visual Studio Code. The YAML and CloudFormation extensions have not been super useful to me. The CloudFormation Designer tool accessible via the AWS Console CloudFormation menu has been the most useful at debugging if needed.

1. Description:

- Modify Description string to state that this is your template and creates the following
  - Example description:
  - `Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address`

2. Mappings:

- Adjust AMI to be the AMI of your choice (yes, it must be changed)

3. Resources:

- Make the following modification for `Resources`
  - VPC range to be `192.168.0.0/23`
  - Subnet range to be `192.168.0.0 - 192.168.0.255`
  - "Tag" each resource with a "Name": `YOURNAME-CF-VPC`
    - Resources include the VPC, subnet, route table, etc.

4. Security Group Settings:

   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses starting with 130.108)
     - Instances within the VPC or subnet

5. Instance settings:

   - Set "Tag" "Name" to "LastName-CF-instance"
   - Set a private IP in your subnet range
   - Using the configuration script in the `cf-template` to also:
     - Change `hostname`
     - Install `git`, `python3`, `pip3`

- Use the "CloudFormation" in the AWS console to test your CloudFormation template.
  - If a stack fails during creation, associated resources (even if create was a success) will also be deleted (it is an all or nothing creation process)

6. Diagram:
- how resources made by your template are connected.  I'm leaving some creative openness here.  You can combine an explanation to go with your visualization.
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
  You can check that hostname was changed by looking at the command prompt once you `ssh` in

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md` with your diagram & companion notes

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project2

3. Do not leave stacks running. Once your template creates a stack successfully, you may delete the stack
