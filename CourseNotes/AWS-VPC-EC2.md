# AWS - VPC & EC2

The purpose of this chunk is to:
- Play around in areas of AWS (specifically the VPC & EC2 resource menus)
- Understand resources / configurations needed to build a cloud network
- Understand resources / configurations needed to reserve & build instances

Need to remember networking 101?  Check out [some other course notes](https://github.com/pattonsgirl/CEG2410/blob/main/LectureNotes/Week03-Networking.md)

## AWS VPC

AWS [Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) allows you to launch resources to a network you define.  The VPC menu in AWS focuses on the network resources in the VPC, while the EC2 menu (discussed later) focuses on instances.

In class, we are digging into the resources reserved when you created a stack in order to understand what a working environment created.

Every VPC must have one or more [subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html), each of which contains a range of IP addresses in your VPC.

Each subnet is assigned a [routing table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#subnet-route-tables) which defines traffic rules for network traffic within the subnet.  In general, there are two rules - one for traffic internal to the VPC, and one for traffic destined for outside the VPC - in other words, what traffic needs to go through the **internet gateway**

An [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) allows communication between your VPC and the internet.  An internet gateway provides a target in your VPC route tables for internet-routable traffic. 


### Security Configurations

[Network access control lists (Network ACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) allow or deny specific inbound or outbound traffic at the **subnet** level.  Your VPC automatically comes with a modifiable default network ACL. By **default**, it **allows all inbound and outbound IPv4 traffic** and, if applicable, IPv6 traffic.

[Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) control the traffic that is allowed to reach and leave the resources that it is associated with.  When you first **create** a security group, it has **no inbound rules**. Therefore, no inbound traffic is allowed until you add inbound rules to the security group.

AWS has made a happy [chart of comparison between Security Groups & Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison)

### NAT Gateways

### IP Addressing

## AWS EC2

AWS Elastic Cloud Compute (EC2)
- instance type
- volumes
- AMI
