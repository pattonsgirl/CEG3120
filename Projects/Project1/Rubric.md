# Project 1 Rubric

## Project Score: / 34

## Part 1 - Build a VPC ( / 16)

1. VPC
   - [ ] description
   - [ ] screenshot w/ proof of configuration per project requirements
2. Subnet 
   - [ ] description
   - [ ] prompt responses
   - [ ] screenshot w/ proof of configuration per project requirements
3. Internet Gateway 
   - [ ] description
   - [ ] screenshot w/ proof of configuration per project requirements
4. Route Table 
   - [ ] description
   - [ ] screenshot w/ proof of configuration per project requirements
5. Security Group 
   - [ ] description
   - [ ] screenshot w/ proof of configuration per project requirements
      - image should capture capture details for all 3 rules 
         - [ ] (-1) point per rule not included
6. Network ACL 
   - [ ] description
   - [ ] screenshot w/ proof of configuration per project requirements
7. Key Pair 
   - [ ] description
   - [ ] prompt responses
   - [ ] screenshot w/ proof of configuration per project requirements
8. Elastic IP 
   - [ ] description + prompt responses
   - [ ] screenshot w/ proof of configuration per project requirements

## Part 2 - EC2 Instance Creation ( / 12)

1. Instance details documents
   - [ ] description of an instance
   - how-to instance launch process guide includes:
      - [ ] Attach the instance to desired subnet
      - [ ] Using the security group designed for the instance
      - [ ] Attach volume to the instance
      - [ ] Tagging the instance with a Name value
   - [ ] AMI selected - AMI ID & OS w/ version
   - [ ] default username of the instance type selected
   - [ ] instance type selected 
   - [ ] keypair selected
   - [ ] justification of why or why not a keypair must be selected
2. [ ] How to associate the EIP with the instance
3. [ ] Screenshot with instance details that validates configuration per project requirements

## Part 3 - Instance Configuration ( / 6)

1. [ ] Steps performed to `ssh` to instance
2. [ ] Steps performed to change hostname of instance
3. [ ] Screenshot of `ssh` connection with hostname changed in CLI prompt
4. Security settings:
   - [ ] Proof that Security Group is applying to instance per project requirements
   - [ ] Proof that Network ACL is applying to instance subnet per project requirements
5. [ ] Steps to install docker accurate to selected AMI

## Point Deductions - Penalty total: 

- [ ] images not included in markdown documentation - 3 point penalty
- [ ] poor markdown formatting - 3 point penalty
- [ ] project tasking text in documentation - 3 point penalty