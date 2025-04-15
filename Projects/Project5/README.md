# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Semantic Versioning](#part-1---semantic-versioning)
- [Part 2 - Continuous Deployment](#part-2---continuous-deployment)
- [Part 3 - Project Description & Diagram](#part-3---project-description--diagram)
- [Part 4 - Demonstration](#part-4---demonstration)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives

- Implement semantic versioning for images using `git tag` metadata in Actions
- Use `webhook`s to keep production up to date

## Project Overview

This project requires completion of [Project 4](../Project4/) in order to have a DockerHub repository with an image for an Angular application, establish GitHub Action workflows and be familiar with basic `docker` commands.  If you did not accomplish Project 4 you should meet with the instructor at your earliest availability.

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it to your logical preferences.

> [!WARNING]
> This project will require an EC2 instance to deploy to.

**Recommended instance specifications**
- 2 CPU Core (included in `t2.medium`)
- 4 GB RAM (included in `t2.medium`)
- 30 GB volume storage

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5% of extra credit per milestone date met.  
To qualify, you must submit your project on the milestone date to the Dropbox for Project 5 in Pilot.

All parts for the project are due 12/13

- [Part 1 - Semantic Versioning](#Part-1---Semantic-Versioning)
  - Milestone EC available
- [Part 2 - Continuous Deployment](#part-2---continuous-deployment)
  - Milestone EC available
- [Part 3 - Project Description & Diagram](#part-3---project-description--diagram)
  - Due at project due date - no milestone EC available
- [Part 4 - Demonstration](#Part-4---Demonstration)
  - Due at project due date - no milestone EC available


## Part 1 - Semantic Versioning

Up to this point, when you build a new container image, the image is tagged with `latest` - this is a default if no other tag is specified.  This means prior builds are not kept - latest is continuously overwritten and you cannot roll back to an older build.  

To this end, you will start generating `tag`s with `git` based on a `commit`.  To generate a tag for the most recent commit, you can run:
- `git tag -a v*.*.*` (ex. `git tag -a v3.8.1`)

When a new tag is pushed to GitHub, it will trigger your GitHub Action Workflow to collect metadata about the tag version, build the container image, then push the image to DockerHub with 3 tags:
- `latest` (ex. `wsukduncan/s25cats:latest`)
- `major` (ex. `wsukduncan/s25cats:3`)
- `major`.`minor` (ex. `wsukduncan/s25cats:3.8`)


### Tasks

1. Create `git` `tag`s for your `commit`s using [semantic versioning best practices](https://semver.org/)
2. Create or modify the GitHub Action workflow in your GitHub repository to:
    - trigger when a `tag` is `push` to the repository - no other triggers should be in your final version
    - use the `docker/metadata-action` to generate a set of tags from your repository
    - utilize repository secrets for login authentication to DockerHub
    - build and push container images to DockerHub with image tags based on your `tag` version AND `latest`
      - DockerHub should receive the following tags to the container image repository:
        - `latest` (ex. `wsukduncan/s25cats:latest`)
        - `major` (ex. `wsukduncan/s25cats:3`)
        - `major`.`minor` (ex. `wsukduncan/s25cats:3.8`)

### Documentation

Create `README-CD.md` in root folder of your GitHub repository that details the following:

1. Generating `tag`s 
    - How to see tags in a `git` repository
    - How to generate a `tag` in a `git` repository
    - How to push a tag in a `git` repository to GitHub
2. Semantic Versioning Container Images with GitHub Actions
    - Summary of what your workflow does and when it does it
    - Explanation of workflow steps
    - Explanation / highlight of values that need updated if used in a different repository
      - changes in workflow
      - changes in repository
    - **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - How to test that your workflow did its tasking
    - How to verify that the image in DockerHub works when a container is run using the image

### Resources

- [GitHub - docker/metadata-action](https://github.com/docker/metadata-action?tab=readme-ov-file#semver)
- [Docker - Manage Tag Labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)

## Part 2 - Continuous Deployment

Now that we have semantic versioning operational, it's time to work on deploying the image in your DockerHub repository to servers that will run the application in the container.

The server running the application in the container will be an EC2 instance.

**Recommended instance specifications**
- 2 CPU Core (included in `t2.medium`)
- 4 GB RAM (included in `t2.medium`)
- 30 GB volume storage

To this end, you will set up three major components:
1. A script that stops and removes the formerly running container, pulls the `latest` tagged image from your DockerHub repository, and runs a new container process with the pull'ed image
2. Utilize either DockerHub or GitHub to send a message to your application server when a change is detected
    - DockerHub - a newly pushed image
    - GitHub - the completion of an Action that pushes a new image
3. On the application server, you will configure a listening service to receive messages from DockerHub or GitHub
    - this listening serve will run your script if a message is delivered
    - you will need to enable some protection method to validate requests are coming from appropriate sources (GitHub or DockerHub)

### Tasks

1. Note your EC2 instance details
2. Install Docker to your EC2 instance
3. Test that your EC2 instance can run a container from your DockerHub repository image
4. Craft a bash script that will:
    -  stop and remove the formerly running container
    - pull the `latest` tagged image from your DockerHub repository
    - run a new container process with the pull'ed image
    - **ADD bash script** to folder named `deployment` in your GitHub repository
5. Install [adnanh's `webhook`](https://github.com/adnanh/webhook) to your EC2 instance
6. Create a configuration file - a hook definition - for `webhook` to load when ran.  The hook definition should:
    - Trigger your bash script to run when a payload is received
    - Validate that the payload came from a trusted source via a shared secret or by validating payload is from DockerHub or GitHub
    - **ADD hook definition** to folder named `deployment` in your GitHub repository
7. Configure DockerHub or GitHub to send a Webhook payload to your EC2 instance when an appropriate event occurs
8. Set up a service file such that the `webhook` is set to start listening as soon as the EC2 instance is on.  Enable this service and verify it triggers your bash script to run when a message is received
    - **ADD webhook service file** to folder named `deployment` in your GitHub repository

### Documentation

In `README-CD.md`, include the following details:

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
    - How to verify that the container is successfully serving the Angular application
      - validate from container side
      - validate from host side
      - validate from an external connection (your physical system)
    - Steps to manually refresh the container application if a new image is available on DockerHub
4. Scripting Container Application Refresh
    - Create a `bash` script on your instance that will:
      - pull the image from your DockerHub repository
      - kill and remove the previously running container
      - start a new container with the freshly pulled image
    - How to test that the script successfully performs its taskings
    - **LINK to bash script** in repository
5. Configuring a `webhook` Listener on EC2 Instance
    - How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the EC2 instance
    - How to verify successful installation
    - Summary of the `webhook` definition file
    - How to verify definition file was loaded by `webhook`
    - How to verify `webhook` is receiving payloads that trigger it
      - how to monitor logs from running `webhook`
      - what to look for in `docker` process views
    - **LINK to definition file** in repository
6. Configuring a Payload Sender
    - Justification for selecting GitHub or DockerHub as the payload sender
    - How to enable your selection to send payloads to the EC2 `webhook` listener
    - Explain what triggers will send a payload to the EC2 `webhook` listener
    - How to verify a successful payload delivery
7. Configure a `webhook` Service on EC2 Instance 
    - Summary of `webhook` service file contents
    - How to `enable` and `start` the `webhook` service
    - How to verify `webhook` service is capturing payloads and triggering bash script
    - **LINK to service file** in repository

### Resources

- [adnanh's `webhook`](https://github.com/adnanh/webhook)
- [Using GitHub actions and `webhook`s](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and `webhook`s](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
- [Linux Handbook - How to Create a `systemd` Service](https://linuxhandbook.com/create-systemd-services/)

## Part 3 - Project Description & Diagram

Include a diagram (or diagrams) of the continuous deployment process configured in this project.  It should (at minimum) address how the developer changing code results in a new container process running on the server running the container application.

### Documentation

In `README-CD.md`, add to the top of the document the following details:

1. Continuous Deployment Project Overview
    - What is the goal of this project
    - What tools are used in this project and what are their roles
    - Diagram of project
    - [If applicable] What is **not working** in this project
2. Resources Section
    - Note: this can be at document top, scattered within document as resources were used, or placed at bottom
    - Add resources used in the project by link.  If generative AI was used, state which platform and what prompts were given.

In `README.md` in the root folder of your GitHub repository:

1. Summarize the project contents in the repository
2. Link to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document. 

### Resources

You can use whatever tools you would like, here are some recommended tools that people use

- [Lucid Charts](https://www.lucidchart.com/pages/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
- [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
- PowerPoint and OneNote are still good choices

## Part 4 - Demonstration

Demonstration can be completed by **either** demonstrating to me in person OR by creating a *video* of the process.  If you go the video route and your file is too large for GitHub, submit it to the "Project 5 - Video of Operation" Dropbox on Pilot
  
For full credit, all of the following must be demonstrated.  Partial credit will be awarded for partial implementations if and only if your documentation states what doesn't work, and what your troubleshooting steps were.

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
    - `angular-site` folder with application
    - `Dockerfile`
    - GitHub action `yml` file in `.github/workflows`
    - `deployment` folder with:
      - `bash` script
      - `webhook` / `hook` definition file
      - `webhook` service file

2. In Pilot, paste the link to your project folder.


