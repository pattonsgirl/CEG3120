# AWS Setup Guide

You should have received an email regarding your AWS  
Educate account for this class. We will be using AWS to create virtual environments  
for you to use to complete the tasks given.

**Important Note:** This AWS environment only allows inbound access from following ports:

- 22

## Getting Started:

- [Setup your environment](EnvironmentSetup.md)

## Before you start: Register for AWS Educate

You should have an email from AWS Educate to guide you through account creation.  
Note: The email was sent to your wright.edu email account

Once you have filled in the registration information and verified your email address, you will get an account  
approval email. For reference, mine took 2-3 minutes to arrive.

_Registration form warnings_:

- Make sure you set a graduation date IN THE FUTURE
  - For Spring 2022, I recommend using 12/30/2026
- The last field on the right is a Promotional Code field. Your autofill may mistake it for a  
  zip code and unhelpfully fill it out for you. Make sure the Promotional Code field is _blank_ (empty)

## Provision the lab environment in AWS.

Assuming you have registered for AWS Educate and have access to this class, perform the following:

- [Sign in to AWS educate](https://www.awseducate.com/signin/SiteLogin)

  - Click the `My Classrooms` Button
  - Click the blue `Go to classroom` button for _Design of Info Tech Systems_
  - Click the blue `AWS Console` button

  This will launch the AWS console  
  Note: If you were already logged in with your personal account, click the log out prompt and  
  log back in with your university account

  Your username in the top right should look something like this  
  `vocstartsoft/user236529=lastname.number@wright.edu`.

Create an SSH key pair to get to your virtual machine.

- Click the Services menu, then select EC2 under Compute  
  [EC2 service from the AWS console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Home:)  
  In the center area you should see a list of all Resources you have available.  
  Right now they should all be 0.
- Click on [Key Pairs](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName)
- Click on the `Create Key Pair` blue button.
  - Choose the name for your key. I used `ceg3120-aws-vm`  
    **MAKE SURE YOU SELECT SSH (pem) as the key type**
  - This creates a public/private key pair, stores the public key in AWS, and downloads the private key to your local machine.
  - **Do not lose the downloaded key.**
  - Back it up to a USB drive or your Office365 account. Once you go through the steps below, this key will be the only way to log in to your AWS environment. If the key is lost, you will need to delete the environment and start from scratch.

Create your AWS environment

- Once you have created your SSH key, [click here to provision your virtual environment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=CEG-2350&templateURL=https:%2F%2Fwsu-cecs-cf-templates.s3.us-east-2.amazonaws.com%2Fceg2350.yml)
  This link autofills many fields for creating our virtual machine.

  - On the first menu, click Next
  - On the second menu, under Parameters, type the name of the key pair you made in the  
    step above. If you don't remember, you can [open your key list here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName). Click Next
  - On the third menu, select Next
  - Scroll to the bottom and select Create Stack
  - You will be redirected to a status page that says CREATE_IN_PROGRESS

- Once you have created the AWS Cloud formation stack you can [return to the EC2 service](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Home:).  
  Here you should see additional resources have been created (not everything says 0 anymore)
- Click on [Running Instances](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:sort=instanceState)
- Our machine should now be created (or almost ready).
- Your machine will be assigned an Elastic IP address. This IP address is what we will use to SSH into the virtual environment.

**WARNING**
While exploring and discovery is an important part of this course, any additional resources you create in AWS have an associated charge. If resources besides those strictly asked for by this course stay running, you risk running out of funds for this course. While fixable, this will hinder your ability to complete projects on time.

## Connecting to the AWS environment

**You are now ready to make an SSH connection to your AWS server.**

- Open a terminal.
- Copy of the AWS SSH key that was downloaded to your home directory
  - Helpful commands: `cp, ls, man`
  - The manual method: Create a file with a useful name (or the same name as the downloaded file) `ceg3120-aws-vm.pem`
  - Open a text editor (`vim` or `nano`)
  - Copy and paste the contents of the key that was downloaded from AWS Educate into the file.
- Change the permissions on the key file in your directory
  - Because private keys need to be protected, the key needs to be changed to readable by your user by using `chmod`
  - `chmod 600 /path/to/private/key` - replace _/path/to/private/key_ with your information
  - Resource on how to use [chmod](https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/)
- SSH into your AWS server with the following command  
   `ssh -i /path/to/private/key ubuntu@ElasticIP`  
   Note: replace _/path/to/private/key_ and _ElasticIP_ with your information
  - If your connection was refused, you may have forgotten to put the username `ubuntu` in front of your Elastic IP address
- You are now signed in to your AWS Educate system as the user `ubuntu`

## Troubleshooting

### Destroying Excess Cloud Formations

1. Go to the Services dropdown, under Management and Governance, select CloudFormation
2. Select the unwanted Stack, then select Delete
   - It is important to remove old stacks. Each stack has a charge associated with it, so you risk running out of funds for this course. While fixable, this will delay your ability to complete labs on time.

### Remaking your AWS Educate environment

The steps below should only be needed if you lost your key from AWS Educate. If you still have your key but your enviromnent is broken, only follow steps 1-2, then go back to the instructions above and rebuild your stack.

1. Go to the Services dropdown, under Management and Governance, select CloudFormation
2. Select your Stack, then select Delete
   - It is important to remove old stacks. Each stack has a charge associated with it, so you risk running out of funds for this course. While fixable, this will delay your ability to complete labs on time.
3. Go to the Services Dropdown, under Compute select EC2
4. Select Key Pairs
5. Select your key pair(s) and select Delete.
6. Recreate your environment by following the steps above

### Acknowledgement

Credit to Matt Kijowski's GitHub Repo - [Lab 1 for Cyber Security Analysis](https://github.com/mkijowski/cyber-security-analysis-applied/blob/master/labs/lab1.md)
