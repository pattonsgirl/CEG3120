# Breakdown of an AWS CloudFormation Template

### Template Format Version

The AWSTemplateFormatVersion section (optional) identifies the capabilities of the template. The latest template format version is `2010-09-09` and is currently the only valid value.
- [AWSTemplateFormatVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/format-version-structure.html)
- No, do not set this to today's date.

```yml
AWSTemplateFormatVersion: 2010-09-09
```

Description of what this stack does
- [Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-description-structure.html)
- Documentation only, not required

```yml
Description: >-
  Testing area for AWS: This template builds a linux VM for CEG 2350 @ WSU.
```

### Parameters

Use the optional Parameters section to customize your templates. Parameters enable you to input custom values to your template each time you create or update a stack.
- [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)
- This example has two parameters:
- One that pulls available key pair names so user can select a key pair
- Another that allows the user to specify a subnet
  - Could be used in SecurityGroups by referring to `SSHLocation` parameter

```yml
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
You use the Ref intrinsic function to reference a parameter, and AWS CloudFormation uses the parameter's value to provision the stack. 

### Mappings

The optional Mappings section matches a key to a corresponding set of named values. For example, if you want to set values based on a region, you can create a mapping that uses the region name as a key and contains the values you want to specify for each specific region. You use the `Fn::FindInMap` intrinsic function to retrieve values in a map.

- [Mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html)

This mapping specifies region, instance type, and AMI ID
- The AMI in this template (`ami-07d0cf3af28718ef8`) will pull what?

```yml
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

The following example shows a Mappings section with a map RegionMap, which contains five keys that map to name-value pairs containing single string values. The keys are region names. Each name-value pair is the AMI ID for the HVM64 AMI in the region represented by the key.

```yml
Mappings: 
  RegionMap: 
    us-east-1: 
      "HVM64": "ami-0ff8a91507f77f867"
    us-west-1: 
      "HVM64": "ami-0bdb828fd58c52235"
    eu-west-1: 
      "HVM64": "ami-047bb4163c506cd98"
    ap-southeast-1: 
      "HVM64": "ami-08569b978cc4dfa10"
    ap-northeast-1: 
      "HVM64": "ami-06cd52961ce9f0d85"
```

And later, to find in map:

```yml
Resources: 
  myEC2Instance: 
    Type: "AWS::EC2::Instance"
    Properties: 
      ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", HVM64]
      InstanceType: m1.small
```


### Resources

The required Resources section declares the AWS resources that you want to include in the stack, such as an Amazon EC2 instance or an Amazon S3 bucket.
- [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html)

```yml
Resources:
  Logical ID:
    Type: Resource type
    Properties:
      Set of properties
```

**Logical ID**: The logical ID must be alphanumeric (A-Za-z0-9) and unique within the template. Use the logical name to reference the resource in other parts of the template. 

**Resource type**: The resource type identifies the type of resource that you are declaring. For example, AWS::EC2::Instance declares an EC2 instance. [All AWS resource and property types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)

**Resource properties:** Resource properties are additional options that you can specify for a resource. 

This template will focus on creating [**EC2** Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html)

Begin defining all resources to be created by using this template when creating a stack.

Define VPC, CIDR block, and `Name` of VPC
- [EC2 VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html)
- `!Ref` will refer to another resource (or parameter name). Think "refer to value stored in variable". You'll see `!Ref`'s throughout the CF template

```yml
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
- [EC2 Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html)
- TODO: Define a key/value pair to create a `Name` for the resource

```yml
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

- [EC2 InternetGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html)

```yml
  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'
    Properties:
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
```

Attach the gateway to the VPC

- [EC2 VPCGatewayAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html)

```yml
  AttachGateway:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
```

Define a route table, attach to VPC
- [EC2 RouteTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html)

```yml
  RouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
```

IF internet gateway has been attached to VPC, add route table rule to direct external traffic through internet gateway ELSE wait (see that `DependsOn`?)

- [EC2 Route](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html)

```yml
  Route:
    Type: 'AWS::EC2::Route'
    DependsOn: AttachGateway
    Properties:
      RouteTableId: !Ref RouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
```

Associate route table with subnet
- [EC2 SubnetRouteTableAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.html)

```yml
  SubnetRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref Subnet
      RouteTableId: !Ref RouteTable
```

Reserve an Elastic IP address, associate with instance
- [EC2 EIP](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html)
- Note: this should depend on Instance being created

```yml
  UbuntuIPAddress:
    Type: 'AWS::EC2::EIP'
    DependsOn: AttachGateway
    Properties:
      Domain: vpc
      InstanceId: !Ref PublicUbuntuInstance
```

Define a Security Group, attach it to VPC
- [EC2 SecurityGroup](- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)
- Ingress = Inbound rules
- Egress = Outbound rules
  - by default, outbound traffic is not restricted.
```yml
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

What about Network ACLs?
  - Define a [Network ACL](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html)
  - Define [Network ACL Entry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#aws-resource-ec2-network-acl-entry--examples) Rules

Define an instance, use the `Mappings` settings where instance type and AMI ID were defined
- [EC2 Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)

```yml
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
Recall we are associating an EIP with the instance.  `AssociatePublicIpAddress` gets a public IP regardless of being an EIP  
[Details on each field can be found in AWS Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html)  

```yml
      NetworkInterfaces:
        - GroupSet:
            - !Ref Lab1SecurityGroup
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: !Ref Subnet
          PrivateIpAddress: 10.0.0.25
```

The [`UserData` section](https://saturncloud.io/blog/how-to-pass-user-data-in-aws-cloudformation/) is information that you can pass to an instance when it is launched. This information can be used:
- to configure the instance
- install software
- run scripts
- [grab secrets provided in Parameters on stack creation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-general.html)
- perform any other tasks that you need to do when the instance is launched

The parameters or scripts to store as user data. Any scripts in user data are run when you launch the instance. User data is limited to 16 KB.

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
```yml
apt install cowsay && \
apt install git && \
reboot
# note, there is no "next" command after reboot, thus no \
```

```yml
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

### Debugging Strategies

[AWS CloudFormation Designer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html)

Strategies for debugging the script in `UserData`:
- `ssh` to instance using the same `AMI`, run commands in script
- After `ssh`ing in to instance created by template, verify package installation / configuration commands worked as expected
    - if something **didn't work**, play with [`systemctl`](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units) to check service status and [`journalctl`](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs) to check service and installation logs.
