# Project 3

## Objectives:

- Create a CloudFormation to specification to remove manual creation

## Assignment Notes / Hints

For this project you need access to your AWS console. [Return to here and click "Start Lab"](https://awsacademy.instructure.com/courses/13269/modules/items/1137325). **Once the icon next to "AWS" is green, click "AWS" to open the console.**

Create a `Project3` folder in your GitHub Classrooms repo. This project is mostly modying a CloudFormation template, so you are welcome to work wherever you are comfortable. I would float towards VSCode myself.

You are welcome to include notes in a README.md file in your folder in your repo if you need to write notes for partial credit.

- It will be handy, but not necessary, to compare / contrast the resources you are making with the working "stack" you created way back when. That stack is based on a template, and that template defined all of these resources - and worked.
- When asked to create "tags", you want to make a "Name" tag and then write the name in the value field. Sometimes the "Name" tag will be autofilled for you. Sometimes not.
- If you get to a point where you need to start over, carefully go through and delete the resources you have already created. Using CloudFormation templates, you can now delete stacks, which is a big improvement.
  1. This is good maintainence. Leaving behind junk is frowned upon in any industry
  2. This will keep you from leaving up resources you can be charged for (like unused instances and elastic IPs)
- Remember you only get 5 elastic IPs...
- This stack can be deleted once your CloudFormation template can successfully create it

## Your first CloudFormation template

I think we can agree that was a lot of menus to go through and things to check. If you were working for, say, a web development company, and you had to do that everytime you got a new customer who wanted a webpage, there would be some frustrations. The "cloud" agrees, and therefore cloud services created templates. In AWS, these are called CloudFormation templates. In these files, you layout every detail of how you want your EC2 setup to be, from VPC to instances. AWS CloudFormation can take these files as input, and feed the values into API calls that create and configure the resources.

A [base template](cf-template.yml) has been provided for you. Due to how many things are in these templates, I would use this base and make the modifications requested.

Your deliverable is a CloudFormation template. Make sure you include it in your repository. Your CloudFormation template should build a VPC (including subnet, gateway, route table, security group) and an instance with an elastic IP address:

1. Description:

   - Modify Description string to state that this is your template and creates the following
   - Example description:
   - `Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address`

2. Mappings:
   - Adjust AMI to be the AMI of your choice
   - This section:
   ```
   AWSRegionUbuntu: # AMI for Ubuntu server in each supported region
   us-east-1:   # N. Virginia
     PV64: NOT_SUPPORTED
     HVM64: ami-07d0cf3af28718ef8
     HVMG2: NOT_SUPPORTED
   ```
3. Resources:

   - VPC range to be /24
   - Subnet range to be /28
   - Tag each resource with a name - last name, cloudformation, resource: `Duncan-CF-VPC`

4. Security Group Settings:

   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses starting with 130.108)
     - Instances within the VPC

5. Instance settings:
   - Set "Tag" "Name" to "LastName-CF-instance"
   - Set a private IP in your subnet range
   - Using the configuration script built into the cf-template
     - Change hostname
     - Install `git`, `python3`, `pip3`

- Use the "CloudFormation" in the AWS console to test your CloudFormation template.

  1. Do not leave stacks running.
  2. If a stack fails during creation, associated resources will also be deleted (it is an all or nothing creation process)
  3. Once your template creates a stack successfully, you may delete the stack

- Extra notes:
  - Anytime you see `!Ref`, there is a reference being made to a value defined elsewhere. These are fun to track down.
  - The configuration script uses some bash syntax.
    - space \ ` \` means the command continues on a new line. Very nice for readability
    - && `&&` need to go inbetween commands. You will see space && \ ` && \` in between commands - again, readability

## Identifying Success

A successful stack will (once created) have an instance you can ssh into.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `YOURLASTNAME-cf.yml`
   - `README.md` (optional for notes)

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project3
