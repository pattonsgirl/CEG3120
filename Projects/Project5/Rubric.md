# Project 5 Rubric

## Project Score: / 63

## GitHub Repository Contents ( / 7)

- [ ] `README-CD.md` (and `README-CI.md` from P4)
- [ ]  `web-content` folder with application
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - [ ] `bash` script
  - [ ] `webhook` / `hook` definition file
  - [ ] `webhook` service file

## Part 4- Project Description & Diagram ( / 10)

Documentation Requirements:

1. Continuous Deployment Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram of project
        - [ ] clean layout
        - [ ] what happens in GitHub
        - [ ] what happens in DockerHub
        - [ ] what happens on AWS instance
    - [ ] [If applicable] What is **not working** in this project
2. Resources Section
    - [ ] Uses good formatting
    - [ ] Citations appropriate to project / include notes on how they were used
3. README.md in root of repository:
    - [ ] Summarizes the project contents in the repository
    - [ ] Links to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document

## Part 1 - Script a Refresh ( / 20)

Documenation Requirements:

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
    - [ ] How to run container from image 
      - Note the differences between using the `-it` flag and the `-d` flags and which you would recommend once the testing phase is complete
    - [ ] How to verify that the container is successfully serving the web applicatio
4. Scripting Container Application Refresh
    - [ ] Description of the bash script
    - [ ] How to test / verify that the script successfully performs its taskings
    - [ ] **LINK to bash script** in repository

Task Requirements - 2 pts each:

- bash script will:
  - [ ] stop and remove the formerly running container
  - [ ] pull the `latest` tagged image from your DockerHub repository
  - [ ] run a new container process with the pull'ed image

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

-  webhook service file
  - [ ] correctly formatted
  - [ ] starts webhook and loads hook definition file
- webhook hook definition file
  - [ ] successfully defines a hook
  - [ ] runs bash script when triggered

## Part 3 - Send a Payload ( / 7)

Documentation Requirements:

1. Configuring a Payload Sender
    - [ ] Justification for selecting GitHub or DockerHub as the payload sender
    - [ ] How to enable your selection to send payloads to the EC2 `webhook` listener
    - [ ] Explain what triggers will send a payload to the EC2 `webhook` listener
    - [ ] How to verify a successful payload delivery
    - [ ] How to validate that your webhook *only triggers* when requests are coming from appropriate sources (GitHub or DockerHub)

Task Requirements - 2 pts each:

- webhook hook definition file
  - [ ] only triggers from validated sources (secret or verification of sender)

## Common Point Deductions:

- [ ] (-5%) DockerHub / GitHub does not have a configured Webhook
- [ ] (-5%) webhook on instance does not trigger with payload from DockerHub or GitHub
- [ ] (-5%) hook does not use trigger rules to check for "valid" message
- [ ] (-10%) Documentation fails to address what was not implemented / implies the project is fully functional.  Always document shortcomings and note what is "research" on how the rest should be done
- [ ] (-30%) Documentation not well organized with markdown OR includes project descriptive text
- [ ] No citations of referenced material
> [!WARNING]
> May result in Academic Integrity Violation with a penalty of a 0 on the project
