# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Semantic Versioning](#part-1---semantic-versioning)
- [Part 2 - Deployment](#Part-3---Deployment)
- [Part 3 - Diagramming](#Part-4---Diagramming)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives

- Implement semantic versioning for images using `git tag` metadata in Actions
- Use `webhook`s to keep production up to date

## Project Overview

For this project you will be continuing to use your `cicd` repo made in project 4.

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it nicely.

This project is reliant on the completion of Project 4.  If you did not perform all taskings in Project 4, you should meet with the instructor asap.

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5% of extra credit per milestone date met.  
To qualify, you must submit your project on the milestone date to the Dropbox for Project 5 in Pilot.

All parts for the project are due 12/13

- [Part 1 - Semantic Versioning](#Part-1---Semantic-Versioning)
  - Milestone due 12/2
- [Part 2 - Deployment](#Part-2---Deployment)
  - Milestone due 12/6
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - All parts are due 12/13
  - No EC
- [Part 4 - Demonstration](#Part-4---Demonstration)
  - All parts are due 12/13
  - No EC

## Part 1 - Semantic Versioning

Right now, you likely `tag` the image with `latest`.  This means versions are never kept.  The solution we will use is to use `git` `tagging`.  A GitHub Action can use the metadata to generate a set of tags for an image.

### Tasks

- Create `tag`s for your `commit`s using [semantic versioning best practices](https://semver.org/)
- Amend your GitHub Action workflow to:
  - run when a `tag` is `push`ed
  - use the `docker/metadata-action` to generate a set of tags from your repository
  - push images to DockerHub with an image tags based on your `git` `tag` version AND `latest`
  - DockerHub should receive a minimum tag set as follows, where major and minor are based on the `tag` metadata:
      - latest
      - major
      - major.minor

### Documentation

Create `README-CD.md` in main folder of your repo that details the following:

- CD Project Overview
  - (what are you doing, why, what tools)
- How to generate and push a `tag` in `git`
- Behavior of GitHub workflow
  - when does it do things
  - what does it do
- Link to Docker Hub repository

### Resources

- [GitHub - docker/metadata-action](https://github.com/docker/metadata-action)
- [Docker - Manage Tag Labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)

## Part 2 - Deployment

### Tasks

For this piece, use an EC2 instance.

- Install docker on the instance
- `pull` the container image from your DockerHub repository containing your application & dependencies from P4
- `run` a container using the image
  - Confirm it responds to requests to the bound port using localhost, its private IP, and its public IP in a browser
- Create a `bash` script on your instance that will:
  - pull the image from your DockerHub repository
  - kill and remove the previously running container
  - start a new container with the freshly pulled image
  - test that the script successfully performs its taskings
- Install [adnanh's `webhook`](https://github.com/adnanh/webhook)
- Configure and enable a hook to run the `bash` script
  - test that when a message is received, the hook runs the `bash` script
- Configure either GitHub or DockerHub to send a message to the listener / hook
- Configure a service file to start the `webhook` listener automatically when the instance starts.

### Documentation

Update `README-CD.md` in main folder of your repo to include:

- Instance information - at minimum public IP and OS
- How to install Docker to the instance given it's OS
- `bash` script
  - Purpose
  - Description of script taskings
  - Location on instance filesystem
  - LINK to your script in a folder named `deployment`
- Purpose of installing & steps to install / setup adnanh's `webhook` to the instance
  - Don't forget ports
- `webhook` / hook task definition file
  - Description of what it does
  - Location on instance filesystem
  - LINK to your hook definition file in a folder named `deployment`
- How to start the `webhook` listening (without using service)
- How to test that the listener successfully listens & triggers the script
  - include:
    - how to monitor logs from the `webhook` program
    - what to look for in `docker` process views
- How to configure GitHub OR DockerHub to message the listener 
- How to modify or create a `webhook` service file such that your `webhook` listener is listening as soon as the system is booted
  - include commands to reload the service respective to files changed (`webhook` service file versus hook definition file)
  - LINK to your `webhook` service file in a folder named `deployment`

### Resources

- [Using GitHub actions and `webhook`s](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and `webhook`s](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
- [Linux Handbook - How to Create a `systemd` Service](https://linuxhandbook.com/create-systemd-services/)

## Part 3 - Diagramming

Include a diagram (or diagrams) of the continuous deployment process in the context of tools used for this project. This diagram would probably look best near your project description.

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
7. status of `webhook` running as a service on the server
8. `webhook` logs that validate container refresh has been triggered
9. post-change state of site running on server
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


