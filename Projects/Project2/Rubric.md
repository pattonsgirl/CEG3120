# Project 2 Rubric

Common feedback:

To communicate over Port 22 in the VPC, You need a security group rule like allow 10.0.0.0/24 + port 22

Once photos are in a folder, as you have, then you can add them to your documentation with ![photo description](Images/imagename.PNG)

192.168 is your internal network IP, not the public IP your ISP is translating you to.  `curl ipinfo.io` to see the public IP you use

/ 15

## Part 1 ( / 5)

1. VPC created & configured & role described
2. Subnet created & configured & role described
3. Internet gateway created & configured & role described
4. Route table created and configured & role described
5. Security group created and configured & role described

## Part 2 ( / 10)

1. Instance details
   - AMI selected
     - default username of the instance type selected
   - Instance type selected
2. How to attach instance to VPC
3. Public IP address auto-assign - yay or nay and why?
4. How to create and attach storage volume to instance
5. How to tag instance with "Name" of "YOURLASTNAME-instance"
6. How to associate VPC security group (your security group) with your instance
7. How to create / reserve and associate and Elastic IP address with your instance
8. Screenshot with instance details
9. How to change hostname via commands on instance
10. Screenshot of successful SSH connection to instance (with your new hostname instead of ip-##-##-##-##)
