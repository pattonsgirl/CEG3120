# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Script a Refresh](#part-1---script-a-refresh)
- [Part 2 - Listen](#part-2---listen)
- [Part 3 - Send a Payload](#part-3---send-a-payload)
- [Part 4 - Project Description & Diagram](#part-4---project-description--diagram)
- [Part 5 - Demonstration](#part-5---demonstration)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives

- Implement semantic versioning for images using `git tag` metadata in Actions
- Use `webhook`s to keep production up to date

## Project Overview

Now that developers can trigger image updates through GitHub Actions, it's time to work on deploying the image in your DockerHub repository to servers that will run the application in the container.

The server running the application in the container will be an EC2 instance.

**Recommended instance specifications**
- 2 CPU Core (included in `t2.medium`)
- 4 GB RAM (included in `t2.medium`)
- 30 GB volume storage

This project requires completion of [Project 4](../Project4/). If you did not accomplish Project 4 you should meet with the instructor at your earliest availability.

The documentation requirements are embedded in their respective parts (in order of how I would recommend setting things up). [Part 4 - Project Description & Diagram](#part-4---project-description--diagram) should be at the **top of your README-CD.md** since it is the description and diagramming requirement.

## Part 1 - Script a Refresh

On your AWS instance, build a bash script that stops and removes the formerly running container, pulls the `latest` tagged image from your DockerHub repository, and runs a new container process with the pull'ed image

### Tasks

1. Build (or use a CF-template to build) an EC2 instance
2. Install Docker to your EC2 instance
3. Test that your EC2 instance can run a container from your DockerHub repository image
4. Craft a bash script that will:
    - stop and remove the formerly running container
    - pull the `latest` tagged image from your DockerHub repository
    - run a new container process with the pull'ed image
      - run as a detached process and with flags to resume running when docker is started (on system start)
    - **copy the bash script** to folder named `deployment` in your GitHub repository

### Documentation

Create `README-CD.md` in root folder of your GitHub repository that details the following:

1. EC2 Instance Details
    - AMI information
    - Instance type 
    - Recommended volume size
    - Security Group configuration
    - Security Group configuration justification / explanation
2. Docker Setup on OS on the EC2 instance
    - How to install Docker for OS on the EC2 instance
    - Additional dependencies based on OS on the EC2 instance
    - How to confirm Docker is installed and that OS on the EC2 instance can successfully run containers
3. Testing on EC2 Instance
    - How to pull container image from DockerHub repository
    - How to run container from image 
      - Note the differences between using the `-it` flag and the `-d` flags and which you would recommend once the testing phase is complete
    - How to verify that the container is successfully serving the web application
4. Scripting Container Application Refresh
    - Description of the bash script
    - How to test / verify that the script successfully performs its taskings
    - **LINK to bash script** in repository

### Resources

## Part 2 - Listen

On the application server, you will configure a listening service to receive messages from DockerHub or GitHub
- this listening serve will run your script if a message is delivered
- you will need to enable some protection method to validate requests are coming from appropriate sources (GitHub or DockerHub)

### Tasks

1. Install [adnanh's `webhook`](https://github.com/adnanh/webhook) to your EC2 instance
2. Create a configuration file - a hook definition - for `webhook` to load when ran.  The hook definition should:
    - Trigger your bash script to run when a payload is received
    - Validate that the payload came from a trusted source via a shared secret or by validating payload is from DockerHub or GitHub
    - **ADD hook definition** to folder named `deployment` in your GitHub repository
3. Set up a service file such that the `webhook` is set to start listening as soon as the EC2 instance is on.  Enable this service and verify it triggers your bash script to run when a message is received
    - **ADD webhook service file** to folder named `deployment` in your GitHub repository

### Documenation

In `README-CD.md`, include the following details:

1. Configuring a `webhook` Listener on EC2 Instance
    - How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the EC2 instance
    - How to verify successful installation
    - Summary of the `webhook` definition file
    - How to verify definition file was loaded by `webhook`
    - How to verify `webhook` is receiving payloads that trigger it
      - how to monitor logs from running `webhook`
      - what to look for in `docker` process views
    - **LINK to definition file** in repository
2. Configure a `webhook` Service on EC2 Instance 
    - Summary of `webhook` service file contents
    - How to `enable` and `start` the `webhook` service
    - How to verify `webhook` service is capturing payloads and triggering bash script
    - **LINK to service file** in repository

## Part 3 - Send a Payload

Utilize either DockerHub or GitHub to send a message to your application server when a change is detected
- DockerHub - a newly pushed image
- GitHub - the completion of an Action that pushes a new image

### Tasks

1. Configure DockerHub or GitHub to send a Webhook payload to your EC2 instance when an appropriate event occurs
2. Validate that your webhook *only triggers* when requests are coming from appropriate sources (GitHub or DockerHub)

### Documentation

In `README-CD.md`, include the following details:

1. Configuring a Payload Sender
    - Justification for selecting GitHub or DockerHub as the payload sender
    - How to enable your selection to send payloads to the EC2 `webhook` listener
    - Explain what triggers will send a payload to the EC2 `webhook` listener
    - How to verify a successful payload delivery
    - How to validate that your webhook *only triggers* when requests are coming from appropriate sources (GitHub or DockerHub)

### Resources

- [adnanh's `webhook`](https://github.com/adnanh/webhook)
- [Using GitHub actions and `webhook`s](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and `webhook`s](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
- [Linux Handbook - How to Create a `systemd` Service](https://linuxhandbook.com/create-systemd-services/)

## Part 4 - Project Description & Diagram

Create a diagram (or diagrams) of the continuous deployment process configured in this project.  It should (at minimum) address how the GitHub Action running results the server running a new container process - again, according to the workflow that this project enables.

### Documentation

In `README-CI.md`, **add to the top of the document** the following details:

1. Continuous Deployment Project Overview
    - What is the goal of this project
    - What tools are used in this project and what are their roles
    - Diagram of project
    - [If applicable] What is **not working** in this project
2. Resources Section
    - Note: this can be at document top, scattered within document as resources were used, or placed at bottom
    - Add resources used in the project by linking them and making a statement of how it was used.  If generative AI was used, state which platform and what prompts were given and again, a statement of how it was used.

Create a `README.md` in the root folder of your GitHub repository:

1. Summarize the project contents in the repository
2. Link to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document. 

### Resources

You can use whatever tools you would like, here are some recommended tools that people use

- [Lucid Charts](https://www.lucidchart.com/pages/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
- [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
- PowerPoint and OneNote are still good choices

## Part 5 - Demonstration

You must demonstration your project implementation **in person**. A booking link will be provided with my available times.

For full credit, all of the following must be demonstrated. Partial credit will be evaluated based on your understanding of the issue and amount of time needed to debug / fix.

1. current state of site running on server, before making a change
    - show the page in the browser
    - show the docker status
2. making a change to the project file (from your local system)
3. `commit` and `push` of the change (from your local system)
4. `tag` the `commit` and `push` the `tag` (from your local system)
5. the GitHub Action triggering, relevant logs that it worked
6. DockerHub receiving a new set of tagged images (modified time should be visible)
7. Payload sent log from DockerHub or GitHub
8. status of `webhook` running as a service on the server
9. `webhook` logs that validate container refresh has been triggered
10. post-change state of site running on server
    - show the page in the browser
    - show the docker status

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course  
   repository.

    Your repo should contain:
    - `README-CD.md` (and `README-CI.md` from P4)
    - `web-content` folder with application
    - `Dockerfile`
    - GitHub action `yml` file in `.github/workflows`
    - `deployment` folder with:
      - `bash` script
      - `webhook` / `hook` definition file
      - `webhook` service file

2. In Pilot, paste the link to your project folder.

## Rubric

[Project Rubric](Rubric.md)

