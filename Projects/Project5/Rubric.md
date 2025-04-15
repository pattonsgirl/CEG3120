# Project 5 Rubric

## Project Score: / XX

## Milestone Extra Credits

- [ ] Milestone 1 = Part 1 - +5% = X pts
  - [ ] Partial Credit for M1
- [ ] Milestone 2 = Part 1 + 2 - +5% = X pts
  - [ ] Partial Credit for M2

## GitHub Repository Contents ( / 7)

- [ ] `README-CD.md` (and `README-CI.md` from P4)
- [ ] `angular-site` folder with application
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - [ ] `bash` script
  - [ ] `webhook` / `hook` definition file
  - [ ] `webhook` service file

## Part 1 - Semantic Versioning ( / 11)

1. Generating `tag`s 
    - [ ] How to see tags in a `git` repository
    - [ ] How to generate a `tag` in a `git` repository
    - [ ] How to push a tag in a `git` repository to GitHub
2. CI with GitHub Actions
    - [ ] Summary of what your workflow does and when it does it
    - [ ] Explanation of workflow steps
    - [ ] Explanation / highlight of values that need updated if used in a different repository
      - [ ] changes in workflow
      - [ ] changes in repository
    - [ ] **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - [ ] How to test that your workflow did its tasking
    - [ ] How to verify that the image in DockerHub works when a container is run using the image

## Part 2 - Deployment ( / 36)

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
      - [ ] Note the differences between using the `-it` flag and the `-d` flags and which you would recommend once the testing phase is complete
    - How to verify that the container is successfully serving the Angular application
      - [ ] validate from container side
      - [ ] validate from host side
      - [ ] validate from an external connection (your physical system)
    - [ ] Steps to manually refresh the container application if a new image is available on DockerHub
4. Scripting Container Application Refresh
    - Create a `bash` script on your instance that will:
      - [ ] kill and remove the previously running container
      - [ ] pull the image from your DockerHub repository
      - [ ] start a new container with the freshly pulled image
    - [ ] How to test that the script successfully performs its taskings
    - [ ] **LINK to bash script** in repository
5. Configuring a `webhook` Listener on EC2 Instance
    - [ ] How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the EC2 instance
    - [ ] How to verify successful installation
    - [ ] Summary of the `webhook` definition file
    - [ ] How to verify definition file was loaded by `webhook`
    - [ ] How to verify `webhook` is receiving payloads that trigger it
      - [ ] how to monitor logs from running `webhook`
      - [ ] what to look for in `docker` process views
    - [ ] **LINK to definition file** in repository
6. Configuring a Payload Sender
    - [ ] Justification for selecting GitHub or DockerHub as the payload sender
    - [ ] How to enable your selection to send payloads to the EC2 `webhook` listener
    - [ ] Explain what triggers will send a payload to the EC2 `webhook` listener
    - [ ] How to verify a successful payload delivery
7. Configure a `webhook` Service on EC2 Instance 
    - [ ] Summary of `webhook` service file contents
    - [ ] How to `enable` and `start` the `webhook` service
    - [ ] How to verify `webhook` service is capturing payloads and triggering bash script
    - [ ] **LINK to service file** in repository

## Part 3 - Project Description & Diagram ( / 8)

1. Continuous Deployment Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram
      - [ ] cleanly presented
      - Explains the project workflow in terms of:
        - [ ] developer role
        - [ ] GitHub role(s)
        - [ ] Docker Hub role(s)
        - [ ] EC2 instance role
          - [ ] delineates `webhook` listener vs container application
    - [ ] [If applicable] What is **not working** in this project
2. Resources Section
    - [ ] included (embedded at relevant points or in stand alone section)
    - [ ] well formatted
3. README.md in root of repository:
    - [ ] Summarizes the project contents in the repository
    - [ ] Links to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document

## Demonstration ( / 10)

1. [ ] current state of site running on server, before making a change
    - show the page in the browser
    - show the docker status
2. [ ] making a change to the project file (from your local system)
3. [ ] `commit` and `push` of the change (from your local system)
4. [ ] `tag` the `commit` and `push` the `tag` (from your local system)
5. [ ] the GitHub Action triggering, relevant logs that it worked
6. [ ] DockerHub receiving a new set of tagged images (modified time should be visible)
7. [ ] Payload sent log from DockerHub or GitHub
8. [ ] status of `webhook` running as a service on the server
9. [ ] `webhook` logs that validate container refresh has been triggered
10. [ ] post-change state of site running on server
    - show the page in the browser
    - show the docker status

## Point Deductions:

- `Dockerfile` does not build viable container image to run application (-5%)
- Action does not push image(s) to DockerHub  (-5%)
- Images in DockerHub do not use semantic versions in tagging (-5%)
- Web hook does not trigger with payload from DockerHub or GitHub (-5%)
- Markdown (README) does not use good formatting practice (-10%)
- Documentation misleads completion of work (-10%)
  - You may document what should be done / happen, but you must also document what is not working  
  and your troubleshooting so far
- No citations of referenced material (-10%)
  - May result in Academic Integrity Violation with a penalty of a 0 on the project
