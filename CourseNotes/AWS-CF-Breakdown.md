# Breakdown of an AWS CloudFormation Template

Define version of API being used. Last update was 2010-09-09

- No, do not set this to today's date.

```
AWSTemplateFormatVersion: 2010-09-09
```

Description of what this stack does

- Documentation only, not required

```
Description: >-
  Testing area for AWS: This template builds a linux VM for CEG 2350 @ WSU.
```

Need a user to provide something unique? Create parameter fields.

- This example has two parameters:
- One that pulls available key pair names so user can select a key pair
- Another that allows the user to specify a subnet
  - Could be used in SecurityGroups by referring to `SSHLocation` parameter

```
Parameters:
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: 'AWS::EC2::KeyPair::KeyName'
    ConstraintDescription: must be the name of an existing EC2 KeyPair.
  SSHLocation:
    Description: ' The IP address range that can be used to access the EC2 instance'
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
```

Specify region, instance type, and AMI ID

- The AMI in this template (`ami-07d0cf3af28718ef8`) will pull what?
- Remember different AMIs can have different default users
- [AWS CF Mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html)

```
Mappings:
  AWSInstanceType2Arch:  # Supported architectures (x64bit only)
    t2.micro:
      Arch: HVM64
  AWSRegionUbuntu: # AMI for Ubuntu server in each supported region
    us-east-1:   # N. Virginia
      PV64: NOT_SUPPORTED
      HVM64: ami-07d0cf3af28718ef8
      HVMG2: NOT_SUPPORTED
```

Begin defining all resources to be created by using this template when creating a stack.

Define VPC, CIDR block, and `Name` of VPC

- `!Ref` will refer to another resource (or parameter name). Think "refer to value stored in variable". You'll see `!Ref`'s throughout the CF template

```
Resources:
  VPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: 10.0.0.0/16
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
        - Key: Name
          Value: CEG2350 VPC
```

Define subnet (or subnets), attach to VPC by ID, CIDR block.

- TODO: Define a key/value pair to create a `Name` for the resource

```
  Subnet:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.0.0/24
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
```

Define an Internet Gateway

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html

```
  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'
    Properties:
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
```

Attach the gateway to the VPC

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html

```
  AttachGateway:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
```

Define a route table, attach to VPC

```
  RouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
```

IF internet gateway has been attached to VPC  
Direct external traffic through internet gateway  
ELSE wait

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html

```
  Route:
    Type: 'AWS::EC2::Route'
    DependsOn: AttachGateway
    Properties:
      RouteTableId: !Ref RouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
```

Associate route table with subnet

```
  SubnetRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref Subnet
      RouteTableId: !Ref RouteTable
```

Reserve an Elastic IP address, associate with instance

```
  UbuntuIPAddress:
    Type: 'AWS::EC2::EIP'
    DependsOn: AttachGateway
    Properties:
      Domain: vpc
      InstanceId: !Ref PublicUbuntuInstance
```

Define a Security Group, attach it to VPC

- Ingress = Inbound rules
- Egress = Outbound rules
  - by default, outbound traffic is not restricted.
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html

```
  Lab1SecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId: !Ref VPC
      GroupDescription: Enable SSH access via port 22 and open all insternal ports.
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: !Ref SSHLocation
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 130.108.0.0/16  # WSU CIDR
        - IpProtocol: -1
          FromPort: '-1'
          ToPort: '-1'
          CidrIp: 10.0.0.0/24
        - IpProtocol: tcp
          FromPort: '1'
          ToPort: '65535'
          CidrIp: 0.0.0.0/0
```

Side note:  What about Network ACLs?
  - Define a [Network ACL](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html)
  - Define [Network ACL Entry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#aws-resource-ec2-network-acl-entry--examples) Rules

Define an instance, use the `Mappings` settings where instance type and AMI ID were defined

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html

```
  PublicUbuntuInstance:
    Type: 'AWS::EC2::Instance'
    DependsOn: AttachGateway
    Properties:
      ImageId: !FindInMap
        - AWSRegionUbuntu
        - !Ref 'AWS::Region'
        - !FindInMap
          - AWSInstanceType2Arch
          - t2.micro
          - Arch
      InstanceType: t2.micro
      KeyName: !Ref KeyName
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
        - Key: Name
          Value: CEG2350 Ubuntu
```

For the instance, define a private IP within subnet, associate Security Group.  
Public IP was already defined to associate with instance

```
      NetworkInterfaces:
        - GroupSet:
            - !Ref Lab1SecurityGroup
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: !Ref Subnet
          PrivateIpAddress: 10.0.0.25
```

Can create a do-on-boot script. `root` will be the user while this runs

- symbols in the script:
  - `\` = new line
  - `&&` = then do the next command
  - `&& \` = do the next command on the next line
- With respect to "when to use &&":
  - `&& \` needs to be between full commands
  - The `&&` says "and do this command next"
  - The `\` says it will be on the next line

As a sample, let's say I want to install two packages:
- `apt install cowsay apt-get install git` is bad (check in your own terminal)
- `apt install cowsay && apt-get install git` is good

In your script, this may look like:
```
apt install cowsay && \
apt install git && \
reboot
# note, there is no "next" command after reboot, thus no \
```

```
      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash -xe
            apt-get update && \
            apt-get install -y \
              git \
              htop \
              sl && \
            echo "This is from the CF template" > /home/ubuntu/hello.txt && \
            reboot
```
