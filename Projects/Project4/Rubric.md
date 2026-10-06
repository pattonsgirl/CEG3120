# Project 4 Rubric

## Project Score: / 35

## Required Documents ( / 1)
- [ ] `AWS-CF/README.md` (0.5 pt)
- [ ] `AWS-CF/` CloudFormation template (0.5 pt)

## Modifications to CF Template ( / 22)

- [ ] Template description revised to describe what the template builds (no `TODO`, no base-template text)
- [ ] AMI changed from the base template's AMI
- [ ] VPC range `192.168.0.0/23`
- [ ] Subnet range `192.168.0.0/24`
- `Name` tag `LASTNAME-CF-<resource type>` on each resource (0.25 pt / each)
    - [ ] VPC
    - [ ] Subnet
    - [ ] Route Table
    - [ ] Internet Gateway
    - [ ] Elastic IP
    - [ ] Security Group
    - [ ] Network ACL
    - [ ] Instance
- [ ] Security Group inbound SSH **and** ICMP from the VPC (`192.168.0.0/23`)
- [ ] Security Group inbound SSH **and** ICMP from home (`/32`, no `0.0.0.0/0` default)
- [ ] Security Group inbound SSH **and** ICMP from WSU (`130.108.0.0/16`)
- [ ] Security Group inbound HTTP port 80 from any IP
- [ ] Security Group inbound HTTP port 8080 from any IP
- [ ] Network ACL denies inbound SSH (TCP 22) from `107.23.4.178`, numbered before an allow-all rule
- [ ] Network ACL denies outbound traffic to wttr.in's `/32`, numbered before an allow-all rule
- [ ] Instance private IP in the subnet range

Instance `UserData` script:

- [ ] Changes hostname to `LASTNAME-AMI` so it persists after reboot
- [ ] Installs `wamerican`, `git`, `python3`, `pip3` with the AMI's package names (0.25 pt / each)
- [ ] Installs `apache2` and `docker`, enabled and started as needed for the AMI (0.5 pt / each)
- [ ] Copies `wordle.sh` (course raw URL) to the default user's home - owned by that user and executable
- [ ] Copies `index.html` (course raw URL or another downloaded page) to the web root
- Docker container `wsukduncan/cheatsheet`
    - [ ] runs detached
    - [ ] restarts automatically (`always` or `unless-stopped`)
    - [ ] host port 8080 bound to container port 80

## Testing & Proof ( / 8)

Screenshots embedded in the README, each with a sentence saying what it proves.

- [ ] Stack status `CREATE_COMPLETE` in the CloudFormation console
- [ ] SSH to the Elastic IP with the new hostname in the prompt
- [ ] Installed software versions (git, python3, pip3, apache2, docker, word list)
- [ ] `wordle.sh` owned by the default user, executable, and running without `sudo`
- [ ] `docker ps` showing the cheatsheet container on `8080->80` (without `sudo`) and its restart policy
- [ ] Both websites in a browser: port 80 (`index.html`) and port 8080 (cheatsheet)
- [ ] Security group: an allowed test (home/campus) **and** a blocked test (network not in the rules)
- [ ] Network ACL: `curl wttr.in` times out while `curl example.com` succeeds

## README Documentation ( / 4)

- [ ] Description of what the template builds - matches the template
- [ ] Companion notes that explain the diagram, including what the NACL and SG rules do and why
- [ ] Diagram embedded and renders on GitHub
- [ ] Diagram shows AWS resources and how traffic flows between them (not the template's sections)

## Point Deductions - Penalty Total: 

- [ ] CF Template does not build a successful stack (fails validation, or no `CREATE_COMPLETE` proof) - 2 point penalty
- [ ] Security Group has additional rules that make it too open - 1 point penalty per rule
- [ ] Bad NACL rule order (allow-all evaluated before a deny) - 1 point penalty
- [ ] Single or mass commit - project not built up over multiple small, descriptive commits - 5% penalty
- [ ] No citations - sources (including AI tools) not cited in the README - 10% penalty
- [ ] Late submission - 10% per day, up to 3 days
- [ ] Submission appears AI-generated or describes work not in the template - score held at 0 pending an instructor meeting
