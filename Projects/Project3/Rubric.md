# Project 3 Rubric

## Project Score: / 44

Research-only notes for an unfinished step (clearly labeled as research) earn up to half of that item's points.

## Part 1 - Build a VPC ( / 23)

1. VPC
   - [ ] description
   - [ ] screenshot w/ proof of configuration (Name, `192.168.0.0/23`)
2. Subnet 
   - [ ] description
   - [ ] prompt responses - reserved block **and** remaining block(s) in CIDR notation
   - [ ] screenshot w/ proof of configuration (Name, `192.168.0.0/24`, VPC)
3. Internet Gateway 
   - [ ] description
   - [ ] screenshot w/ proof of configuration (Name, attached to the VPC)
4. Route Table 
   - [ ] description
   - [ ] screenshot w/ proof of configuration (route to the IGW and subnet association)
5. Security Group 
   - [ ] description
   - screenshot w/ proof of configuration (Source column visible):
      - [ ] SSH and ICMP (All ICMP - IPv4) rules exist, none open to `0.0.0.0/0`
      - SSH **and** ICMP allowed from:
         - [ ] WSU block (`130.108.0.0/16`)
         - [ ] VPC block (`192.168.0.0/23`)
         - [ ] Home IP (`/32`)
      - [ ] HTTP from anywhere
6. Network ACL 
   - [ ] description
   - [ ] Screenshot, associated with the subnet, with Inbound Deny SSH (TCP 22) from `107.23.4.178` numbered before the allow-all rule
   - [ ] Screenshot with Outbound Deny on any port to wttr.in's IP numbered before the allow-all rule
7. Key Pair 
   - [ ] description of what a key pair is for
   - [ ] prompt responses - how the public and private keys are stored and used
   - [ ] screenshot of the key pair in the EC2 console
8. Elastic IP 
   - [ ] description + prompt response - difference from a public IP (stop / start behavior)
   - [ ] screenshot w/ proof of configuration (address and Name tag)

## Part 2 - EC2 Instance Creation ( / 12)

1. Instance details documents
   - [ ] description of an instance
   - how-to instance launch process guide includes steps to:
      - [ ] Attach the instance to the desired subnet
      - [ ] Use the security group designed for the instance
      - [ ] Attach a volume to the instance
      - [ ] Tag the instance with a Name value
   - [ ] AMI selected - AMI ID & OS w/ version (actual values, matching the instance)
   - [ ] default username of the instance type selected
   - [ ] instance type selected (matching the instance)
   - [ ] keypair selected (by name, matching the instance)
   - [ ] justification of why a keypair must be selected
2. [ ] Steps to associate the EIP with the instance
3. [ ] Screenshot with instance details that validates configuration (Name, type, VPC, subnet, private IP, Elastic IP)

## Part 3 - Instance Configuration ( / 9)

1. [ ] Steps performed to `ssh` to instance (actual command)
2. [ ] Steps performed to change hostname of instance (persistent, e.g. `hostnamectl`)
3. [ ] Screenshot of `ssh` connection with hostname changed in CLI prompt
4. Security testing (command, where it ran from, result, and what it proves):
   - [ ] Security Group allowed test - `ping` / `ssh` from home or campus succeed
   - [ ] Security Group blocked test - `ping` from a network not in the rules times out
   - [ ] Security Group HTTP test - request from your computer returns `200 OK` from a server on the instance
   - [ ] Network ACL outbound test - `curl wttr.in` times out while `curl example.com` succeeds
5. Docker setup:
   - [ ] Steps to install docker accurate to the selected AMI, including adding the user to the `docker` group
   - [ ] Proof that docker engine is running & that user can run container processes without `sudo` (`docker run hello-world` output)

## Point Deductions - Penalty total: 

- [ ] images not included in markdown documentation - 5% penalty (no screenshots embedded); 2.5% penalty (some screenshots missing or not displaying)
- [ ] poor markdown formatting - up to 10% penalty, scaled by severity (10% = illegible)
    - includes project tasking text left in the documentation (pasted instruction bullets or prompts) - 5% penalty
- [ ] Single or mass commit - project not built up over multiple small, descriptive commits - 5% penalty
- [ ] No citations - sources (including AI tools) not cited in the README - 10% penalty
- [ ] Late submission - 10% per day, up to 3 days
- [ ] Submission appears AI-generated or describes work not done - score held at 0 pending an instructor meeting
