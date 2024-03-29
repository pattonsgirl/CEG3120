# Project 1

## Objectives:

- Understand and build a private cloud network
- Understand and build an EC2 instance

## Assignment Notes / Hints

For this project you need access to your AWS "console". Return to the AWS Learner Lab page and click "Start Lab".  **Once the icon next to "AWS" is green (or timer countdown begins), click "AWS" to open the console.**

Create a `Project1` folder in your GitHub Classrooms repo. This project is mostly documentation of work, so you are welcome to work on your documentation and in your repo wherever you are comfortable. I would float towards VSCode myself.

In your `Project1` folder, create a file named `README.md` Do you work for Parts 1 & 2 here.

- It will be handy, but not necessary, to compare / contrast the resources you are making with the working "stack" you have. That stack is based on a template, and that template defined all of these resources - and worked.
- When asked to create "tags", you want to make a "Name" tag and then write the name in the value field. Sometimes the "Name" tag will be auto-filled for you. Sometimes not.
- If you get to a point where you need to start over, carefully go through and delete the resources you have already created.
  1. This is good maintenance. Leaving behind junk is frowned upon in any industry
  2. This will keep you from running resources you can be charged for (like unused instances and elastic IPs)

## Part 1 - Build a VPC

For each step below, provide 
   - a description of what the resource does (what is its role).
   - a screenshot that shows the network resource has been created according to specification  
   
You may add whatever additional notes you would like. Getting a good screenshot can be done by clicking on the resource and showing configurations in the details menu.

1. Create a **VPC**
   - Tag it with "YOURLASTNAME-VPC"
   - Specify a CIDR block of 172.18.0.0/23
2. Create a **Subnet**
   - Tag it with "YOURLASTNAME-Subnet"
   - Reserve 172.18.0.0 - 172.18.0.255 for use on this subnet
   - Attach it to your VPC
   - What block of IPs is still available in your VPC?
3. Create an **Internet Gateway**
   - Tag it with "YOURLASTNAME-gw"
   - Attach it to your VPC
4. Create a **Route Table**
   - Tag it with "YOURLASTNAME-rt"
   - Attach it to your VPC
   - Associate it with your subnet
   - Add a routing table rule that sends traffic to destinations external to your subnet CIDR block to your internet gateway
5. Create a **Security Group**
   - Tag it with "YOURLASTNAME-sg"
   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses in CIDR block 130.108.0.0/16)
     - Instances within the VPC
   - Attach it to your VPC
   - Image should include your Inbound rules
6. Identify OR create a **Key Pair**
   - Document how the public and private keys of a key pair are stored.
   - Image should be which Key Pair you are using.

## Part 2 - EC2 instances

This part will focus on running an instance in your VPC.  You will provide specific documentation at each step and **two** screenshots - one proving that your instance is configured in AWS and another proving that your instance is configured.

1. Create a new **Instance**. 
   - Note: these steps are ordered based on the "Launch Instances" wizard.
2. Fill in the following information about your instance:
   - AMI selected - AMI id & OS with version
   - default username of the instance type selected
   - instance type selected 
   - keypair selected
   - describe why you need to select a keypair
2. Attach the instance to your subnet within your VPC. 
   - Document how you did it and what this does.
3. Determine whether a Public IPv4 address will be auto-assigned to the instance. 
   - Justify your choice to do so (or not do so).  Your answer should include the difference between Public IPv4 addresses and Elastic IP addresses.
   - **NOTE** - in the next few steps, you will be required to request an Elastic IP address and associate it to the instance. Factor that in to your discussion here.
4. Attach a volume to your instance. 
   - Document how you did it and what this does.
5. Tag your instance with a "Name" of "YOURLASTNAME-instance". 
   - Document how you did it.
6. Associate your security group, "YOURLASTNAME-sg" to your instance.
   - Document how you did it and what this does.
7. Reserve an Elastic IP address. 
   - Tag it with "YOURLASTNAME-EIP". 
   - Associate the Elastic IP with your instance.
   - Document how you did it and what this does.
8. Create a **screenshot your instance details** and add it to your project write up. Example below:
   ![sample instance details](sample.png)
9. `ssh` in to your instance. 
   - Change the hostname to "YOURLASTNAME-AMI" where AMI is some identifier of the AMI you chose. 
   - Document how you did it.
   - Notes on changing a system hostname: 
      1. It is wise to copy config files you are about to change to filename.old For `/etc/hostname`, for example, I would first copy the current `hostname` file to `/etc/hostname.old`
      2. You should not change permissions on any files you are modifying. They are system config files. You may need to access them with administrative privileges.
      3. Here is a helpful resource: https://www.tecmint.com/set-hostname-permanently-in-linux/ I did not modify `/etc/hosts` on mine - do so or not as you wish.
10. Create a **screenshot your `ssh` connection to your instance** and add it to your project write up - make sure it shows your new hostname.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

   - Your repo should contain:
   - `images` folder (optional depending on how you implement including screenshots)
   - `README.md`

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project1

3. You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic IP.  If I have questions about your work, your documentation should be good enough to quickly rebuild.

## Rubric

[Link to Rubric](Rubric.md)