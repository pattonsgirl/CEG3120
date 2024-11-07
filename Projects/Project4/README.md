# Project 4

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
- [Part 3 - Diagramming](#Part-3---Diagramming)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives

- Containerize an application with Docker
- Automate the project pipeline with GitHub Actions - continuous integration

## Project Overview

For this project you will be creating a fresh repository. The link is in Pilot under Content - Projects - CI -> CD. This is the repo you will be using for Projects 4 & 5.

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it to your logical preferences.

[angular-bird.zip](angular-bird.zip) is a *simple* Angular application.  It requires the following software stack to run:
- Node.js
- Angular (installed with `npm`, the node package manager)

Credit for the Angular application goes to Erik Jenkins	& Ryan Nicolai.

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone date to the Dropbox for Project 4 in Pilot.

All parts for the project are due 11/25

- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
  - Milestone due 11/15
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
  - Milestone due 11/22
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - Due with all parts 11/25

## Part 1 - Dockerize it

### Tasks

- Install Docker to your system.
- Create DockerHub account: https://hub.docker.com/
  - select Free tier if prompted
- Create Public Repository in DockerHub named YOURLASTNAME-CEG3120
- Create new GitHub repo (link to create located in Pilot in Content -> CI/CD Projects)
  - This repository will be Public (your previous repo was Private) and you will have privileges to manipulate the repository settings
- To your repo in a folder named `angular-site`, extract the contents of [angular-bird.zip](angular-bird.zip)
  - You may use an EC2 instance if your system is not Docker compatible.
- Build and configure a container that will run the `angular-site` application
- Create a `Dockerfile` in your repository that builds a container image with the following requirements:
  - utilizes an appropriate base image with the `FROM` command
  - completes installation of the application software stack with `RUN` command(s)
  - copies in the `angular-site` application with the `COPY` command
  - starts the application when a container is run from the image built with the `Dockerfile` with the `CMD` command 
    - Note: as needed according to your base  selection
  - use of the `EXPOSE` command is optional
- Push container image built by your `Dockerfile` to your DockerHub repository for container images for this project 

### Documentation

Create `README-CI.md` in main folder of your repo that details the following:

- CI Project Overview
  - (what are you doing, why, what tools)
- Containerizing your Application:
  - how to install docker + dependencies on your system's OS (or an EC2 instance)
  - how to build & configure a container (without building an image) that runs the `angular-site` application
  - summary of instructions stated in the repository `Dockerfile`
  - how to build an image from the repository `Dockerfile`
  - how to run a container from the image built by the repository `Dockerfile`
  - how to view the application running in the container 
    - (open a browser...go to IP and port...)
- Working with DockerHub:
  - how to create public repo in DockerHub
  - how to authenticate with DockerHub via CLI using DockerHub credentials
    - what credentials would you recommend providing?
  - how to push container image to DockerHub
  - **Link** to your DockerHub repository for this project

## Part 2 - GitHub Actions and DockerHub

### Tasks

- Create an Access Token with Read / Write access to your DockerHub account's repositories.
- Set GitHub Secrets named DOCKER_USERNAME and DOCKER_TOKEN containing your DockerHub username & DockerHub access token, respectively.
- Set up GitHub Actions workflow to build and push docker image to DockerHub

### Documentation

In `README-CI.md`, include the following details:

- Configuring GitHub Secrets:
  - How to set a secret for use by GitHub Actions
  - What secret(s) are set for this project
    - Note: do not copy paste your secrets into your documentation
- Behavior of GitHub workflow
  - summary of what your workflow does
  - **Link** to workflow file in your GitHub repository
  - summary of what a user would need to change or configure if using your workflow to duplicate your project
    - include workflow changes & repository changes

### Resources

- [Docker Docs - CICD with GitHub Actions](https://docs.docker.com/ci-cd/github-actions/)
- [GitHub Actions - build-push-action documentation](https://github.com/marketplace/actions/build-and-push-docker-images)
- [GitHub - publishing images to DockerHub](https://docs.github.com/en/actions/guides/publishing-docker-images#publishing-images-to-docker-hub)

## Part 3 - Diagramming

Include a diagram (or diagrams) of the continuous integration process.  A good diagram will label tools used and how things connect.  This diagram would probably look best near your project description.

### Resources

You can use whatever tools you would like, here are some recommended tools that people use

- [Lucid Charts](https://www.lucidchart.com/pages/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
- [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
- PowerPoint and OneNote are still good choices

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository.

   - Your repo should contain:
   - `README-CI.md`
   - `angular-site` folder with Angular application
   - `Dockerfile`
   - GitHub action `yml` file in `.github/workflows`
   - diagram image(s)

2. In Pilot, paste the link to your project folder.
