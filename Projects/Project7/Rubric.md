# Project 7 Rubric

## Project Score: / 75

Grading notes:
- 1 point per box unless noted.
- Research-only notes for an unfinished step (clearly labeled as research) earn up to half of that item's points.
- Documented values (IPs, ports, image names, links) must match your repository and your running instance.
- The in-person demonstration is scored separately with the [Demonstration Rubric](Demonstration-Rubric.md).

## GitHub Repository Contents ( / 7)

- [ ] `README-CD.md` (and `README-CI.md` from P6)
- [ ] `web-content` folder with application
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - [ ] `bash` script
  - [ ] `webhook` / `hook` definition file
  - [ ] `webhook` service file

## Part 4 - Project Description & Diagram ( / 10)

Documentation Requirements:

1. Continuous Deployment Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram of project
        - [ ] clean layout
        - [ ] what happens in GitHub
        - [ ] what happens in DockerHub
        - [ ] what happens on AWS instance
    - [If applicable] What is **not working** in this project - scored with the Incomplete work deduction
2. Resources Section
    - [ ] Uses good formatting
    - [ ] Citations appropriate to project / include notes on how they were used
3. README.md in root of repository:
    - [ ] Summarizes the project contents in the repository
    - [ ] Links to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document

## Part 1 - Script a Refresh ( / 20)

Documentation Requirements:

1. EC2 Instance Details
    - [ ] AMI information
    - [ ] Instance type 
    - [ ] Recommended volume size
    - [ ] Security Group configuration
    - [ ] Security Group configuration justification / explanation
2. Docker Setup on OS on the EC2 instance
    - [ ] How to install Docker for OS on the EC2 instance
    - [ ] Additional dependencies based on OS on the EC2 instance
    - [ ] How to confirm Docker is installed and that OS on the EC2 instance can successfully run containers
3. Testing on EC2 Instance
    - [ ] How to pull container image from DockerHub repository
    - [ ] How to run container from image, including the differences between the `-it` and `-d` flags and which you would recommend once the testing phase is complete
    - [ ] How to verify that the container is successfully serving the web application
4. Scripting Container Application Refresh
    - [ ] Description of the bash script
    - [ ] How to test / verify that the script successfully performs its taskings
    - [ ] **LINK to bash script** in repository

Task Requirements - 2 pts each:

- bash script will:
  - [ ] stop and remove the formerly running container
  - [ ] pull the `latest` tagged image from your DockerHub repository
  - [ ] run a new container process with the pull'ed image, detached and with a restart policy

## Part 2 - Listen ( / 19)

Documentation Requirements:

1. Configuring a `webhook` Listener on EC2 Instance
    - [ ] How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the EC2 instance
    - [ ] How to verify successful installation
    - [ ] Summary of the `webhook` definition file
    - [ ] How to verify definition file was loaded by `webhook`
    - How to verify `webhook` is receiving payloads that trigger it
      - [ ] how to monitor logs from running `webhook`
      - [ ] what to look for in `docker` process views
    - [ ] **LINK to definition file** in repository
2. Configure a `webhook` Service on EC2 Instance 
    - [ ] Summary of `webhook` service file contents
    - [ ] How to `enable` and `start` the `webhook` service
    - [ ] How to verify `webhook` service is capturing payloads and triggering bash script
    - [ ] **LINK to service file** in repository

Task Requirements - 2 pts each: 

- webhook service file
  - [ ] correctly formatted
  - [ ] starts webhook, loads hook definition file, and is enabled to start with the instance
- webhook hook definition file
  - [ ] successfully defines a hook
  - [ ] runs bash script when triggered

## Part 3 - Send a Payload ( / 9)

Documentation Requirements:

1. Configuring a GitHub Webhook
    - [ ] How to enable GitHub to send payloads to the EC2 `webhook` listener
    - [ ] Explain what triggers will send a payload to the EC2 `webhook` listener, and why that event is used instead of `push`
    - [ ] How to verify a successful payload delivery
    - [ ] How to validate that your webhook *only triggers* when requests are coming from GitHub
2. GitHub Webhooks vs. DockerHub Webhooks
    - [ ] Contrasts the two: what sends a payload and when, how the receiver can verify the sender, and which you would use for this deployment and why

Task Requirements - 2 pts each:

- [ ] GitHub webhook configured for the **Workflow runs** event, with successful deliveries to the instance
- webhook hook definition file
  - [ ] only triggers on a valid GitHub signature (shared secret) and a successful completed workflow run

## Testing & Proof ( / 10)

Screenshots embedded in `README-CD.md`, each with a sentence saying what it proves.

- [ ] Instance and Security Group - instance running and inbound rules, including the `webhook` port
- [ ] Docker on the instance - `docker --version`, and `docker ps` without `sudo`
- [ ] Site from your image - `docker ps` with the port mapping, and a browser showing the site at the instance's public IP
- [ ] Refresh script - `docker ps` before and after running the script, showing a new container ID running the `latest` image
- [ ] Restart behavior - restart policy from `docker inspect`, and `uptime` with `docker ps` after a reboot
- [ ] Hook loaded - `webhook` log output showing the definition file loaded and the hook available
- [ ] Service - `systemctl status webhook` showing `active` and `enabled`, including after the reboot
- [ ] Payload delivery - successful delivery in GitHub's **Recent Deliveries**, and the matching `webhook` log entry
- [ ] Negative test - a request that fails the trigger rules, with the response, the `webhook` log entry, and an unchanged container ID
- [ ] End to end - site and `docker ps` before and after a new `tag`, showing a new container ID and the change

## Point Deductions - Penalty Total: 

- Incomplete work - the script, `webhook`, or GitHub webhook has apparent issues, or a GitHub payload does not trigger a container refresh. Apply **one** tier, based on how `README-CD.md` documents it:
   - [ ] 10% penalty - README indicates the work is complete
   - [ ] 5% penalty - README notes the areas where blockers were hit
   - [ ] 2% penalty - README notes the blockers, the things tried, and clearly delineates next steps that have not been tested; the files in `deployment` are in line with what the README describes
- [ ] Security Group has additional rules that make it too open - 1 point penalty per rule
- [ ] Secret committed to the repository (such as a `.pem` key or DockerHub PAT) - 5% penalty; the webhook secret in the hook definition file is not penalized
- [ ] images not included in markdown documentation - 5% penalty (no screenshots embedded); 2.5% penalty (some screenshots missing or not displaying) - the diagram is scored under Part 4
- [ ] poor markdown formatting - up to 10% penalty, scaled by severity (10% = illegible)
    - includes project / rubric tasking text left in the documentation - 5% penalty
- [ ] Single or mass commit - project not built up over multiple small, descriptive commits - 5% penalty
- [ ] No citations - sources (including AI tools, with the prompts used) not cited - 10% penalty
- [ ] Late submission - 10% per day, up to 3 days
- [ ] Submission appears AI-generated without citation or describes work not done - score held at 0 pending an instructor meeting

Percentage deductions are taken from the total possible (e.g. 10% of 75 = 7.5).
