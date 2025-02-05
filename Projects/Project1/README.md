# Project 1

## Objectives:

- Understand and build a private cloud network
- Understand and build an EC2 instance

## Assignment Notes

For this project you need access to your AWS "console". Return to the AWS Learner Lab page and click "Start Lab".  **Once the icon next to "AWS" is green (or timer countdown begins), click "AWS" to open the console.**

Create a `Project1` folder in your GitHub Classrooms repo.  Create a file named `README.md` Do your documentation work here. You are welcome to work on your documentation and in your repo wherever you are comfortable. I would float towards VSCode myself.

Mark & document points when you are stuck, or have not solved or implemented a piece of the project and differentiate your attempts and progress versus your research in how parts would come together if they did work.

Do not leave project task text in your documentation.  It muddles what your work was versus what the assignment taskings were, and may result in a poor grade due to lack of good documentation forms.

Some hints / useful notes:
- It will be handy, but not necessary, to compare / contrast the resources you are making with the working "stack" you have. That stack is based on a template, and that template defined all of these resources - and worked.
- When asked to create "tags", you want to make a "Name" tag and then write the name in the value field. Sometimes the "Name" tag will be auto-filled for you. Sometimes not.
- If you get to a point where you need to start over, carefully go through and delete the resources you have already created.
  1. This is good maintenance. Leaving behind junk is frowned upon in any industry
  2. This will keep you from running resources you can be charged for (like unused instances and elastic IPs)
- In markdown, you can reference an image and include it in the md file using this syntax:
```
![image description](path/to/img/file.jpg)
```
![sample image](sample.png)

## Part 1 - Build a VPC

For each step below, provide 
   - a description of what the resource does (what is its role).
   - responses to additional requests for information in any step.
   - a screenshot that shows the network resource has been created according to specification  
   
You may add whatever additional notes you would like. Getting a good screenshot can be done by clicking on the resource and showing configurations in the details menu.

1. Create a **VPC**
   - Tag the "Name" with "YOURLASTNAME-VPC"
   - Specify a CIDR block of 172.18.0.0/23
2. Create a **Subnet**
   - Tag the "Name" with "YOURLASTNAME-Subnet"
   - Reserve 172.18.0.0 - 172.18.0.255 for use on this subnet
   - Attach it to your VPC
   - Document the reserved block for the subnet **and** the remaining block(s) available in VPC
3. Create an **Internet Gateway**
   - Tag the "Name" with "YOURLASTNAME-gw"
   - Attach it to your VPC
4. Create a **Route Table**
   - Tag the "Name" with "YOURLASTNAME-rt"
   - Attach it to your VPC
   - Associate it with your subnet
   - Add a routing table rule that sends traffic to destinations external to your subnet CIDR block to your internet gateway
5. Create a **Security Group**
   - Tag the "Name" with "YOURLASTNAME-sg"
   - Allow SSH for a set of trusted source networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses in CIDR block 130.108.0.0/16)
     - Instances within the VPC
   - Attach it to your VPC
   - Make sure screenshot includes content of the Inbound rules
6. Modify or create a **Network ACL**
   - Tag the "Name" with "YOURLASTNAME-nacl"
   - Affirm association or associate resource with the subnet
   - Verify that for Inbound & Outbound there is a rule that `Allow`s any IP (v4 only is sufficient) on all ports
     - If this rule does not exist, you'll need to create it.  Created Network ACL's are `Deny` all traffic on all ports, Inbound and Outbound, by default.
   - Deny outbound connections to any port on [wttr.in](https://wttr.in/)
7. Identify OR create a **Key Pair**
   - Document how the public and private keys of a key pair are stored.
8. Reserve an **Elastic IP address**. 
   - Tag the "Name" with "YOURLASTNAME-EIP". 
   - Document the difference between an Elastic IP and a Public IP.

## Part 2 - EC2 Instance Creation

This part will focus on configuring an instance in your VPC.

For each step below, provide a description of steps to complete the tasks (screenshots not required) and any additional documentation required by the step.

Note: these steps are ordered based on the "Launch Instances" wizard.

1. Create a new **Instance**. In addition to describing what an instance is and how-to launch a new one, find and document the following information about the instance you have built:
   - AMI selected - AMI id & OS with version
   - default username of the instance type selected
   - instance type selected 
   - keypair selected
   - describe why you need to select a keypair
   - the how-to launch an instance instructions should include coverage on how-to:
      - Attach the instance to your subnet within your VPC
      - Associate your security group, "YOURLASTNAME-sg" to your instance.
      - Attach a volume to your instance. 
      - Tag your instance with a "Name" of "YOURLASTNAME-instance". 
2. Associate the Elastic IP with your instance.
3. Create a **screenshot of your instance details** after instance has been launched and add it to your project write up. 

## Part 3 - Instance Configuration

This part will focus on configurations and tests once you `ssh` in to your instance.

For each step below, provide a description of steps to complete the tasks and any additional documentation required by the step.

1. `ssh` in to your instance. 
2. Change the hostname to "YOURLASTNAME-AMI" where AMI is some identifier of the AMI you chose. 
   - Notes on changing a system hostname: 
      1. It is wise to copy config files you are about to change to filename.old For `/etc/hostname`, for example, I would first copy the current `hostname` file to `/etc/hostname.old`
      2. You should not change permissions on any files you are modifying. They are system config files. You may need to access them with administrative privileges.
      3. Here is a helpful resource: https://www.tecmint.com/set-hostname-permanently-in-linux/ I did not modify `/etc/hosts` on mine - do so or not as you wish.
3. Create a **screenshot of your `ssh` connection to your instance** and add it to your project write up - make sure it shows your new hostname in the CLI prompt.
4. Prove with trial descriptions & screenshots that your Network ACL and Security Group are allowing or blocking traffic per your configurations.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `images` folder (optional depending on how you implement including screenshots)
   - `README.md`

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project1

3. You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic IP.  If I have questions about your work, your documentation should be good enough to quickly rebuild.

## Rubric

[Link to Rubric](Rubric.md)
