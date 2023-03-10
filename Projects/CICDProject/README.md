# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
- [Part 3 - Deployment](#Part-3---Deployment)
- [Part 4 - Diagramming](#Part-4---Diagramming)
- [Submission](#Submission)
- [Extra Credit - BYOP](#Extra-Credit---BYOP)
- [Extra Credit - By Proxy](#Extra-Credit---By-Proxy)
- [Rubric](Rubric.md)

## Objectives

- Containerize an application with Docker
- Automate the project pipeline with GitHub Actions - continuous integration
- Use webhooks to keep production up to date - continuous deployment

## Project Overview

For this project you will be creating a fresh repository - the link is in Pilot under Content - Projects - Project 5. This is the repo you will be using for this project.

You will notice that each part has "Milestone" labels and dates. This project is not due until
12/2. Completion of each milestone **by the date specified for the milestone** will get you 10%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone
data to the Dropbox for Project 5 in Pilot.

## Parts & Milestones

- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
  - Milestone due 11/14
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
  - Milestone due 11/21
- [Part 3 - Deployment](#Part-3---Deployment)
  - Milestone due 11/28
- [Part 4 - Diagramming](#Part-4---Diagramming)
  - All parts are due 12/2 - Friday, December 2nd.
  - No EC

## Part 1 - Dockerize it

### Tasks

- Create new GitHub repo (link to create located in Pilot in Content -> Project 5)
- In a folder named `website`, add the contents of your website
  - this can be a site you created in another class, pet project of yours, or just a vanilla html file
- Install Docker
  - You can install Docker in WSL2 or in an EC2 instance. You'll need your Project 5 repo on wherever you are working
- Create a container image that will run a webserver and contains your "website"
  - you can use apache2 or nginx as the webserver
- Create a Dockerfile with instructions on how to build the image
- Add site content & Dockerfile to repo

### Documentation

- Create `README.md` in main folder of your repo that details the following:
- Project Overview
- Run Project Locally
  - how you installed docker + dependencies (WSL2, for example)
  - how to build the container from the Dockerfile
  - how to run the container
  - how to view the project running in the container (open a browser...go to ip and port...)

## Part 2 - GitHub Actions and DockerHub

### Tasks

- Create DockerHub account: https://hub.docker.com/
  - select Free tier if prompted
- Create Public Repository in DockerHub
- Set GitHub Secrets named DOCKER_USERNAME and DOCKER_PASSWORD with your respective information filled out.
- Set up GitHub Actions workflow to build and push docker image to DockerHub
  - Use workflow templated here: https://docs.github.com/en/actions/guides/publishing-docker-images#publishing-images-to-docker-hub

### Documentation

- Update `README.md` in main folder of your repo to include:

- Process to create public repo in DockerHub
- How to authenticate with DockerHub via CLI using Dockerhub credentials
  - what credentials would you recommend providing?
- How to push container to Dockerhub
- Configuring GitHub Secrets
  - What secrets were set based on what info
- Behavior of GitHub workflow
  - what does it do and when
  - what variables in workflow are custom to your project
    - think may need to be changed if someone else is going to use it or you reuse it

### Resources

- [GitHub Actions - Docker Docs](https://docs.docker.com/ci-cd/github-actions/)

## Part 3 - Deployment

### Tasks

- For this piece, use an EC2 instance.
- Install docker on the instance
- Create a webhook set up to automatically deploy updates to the container image - see Resources for this part

### Documentation

- Update `README.md` in main folder of your repo to include:

- Description of container restart script
- Setting up a webhook on the server
  - How you created you own listener
  - How you installed the [webhook on GitHub](https://github.com/adnanh/webhook)
  - How to keep the webhook running if the instance is on
- Description of Webhook task definition file
- Steps to set up a notifier in GitHub or DockerHub

### Resources

Note: the challenging part here is getting the webhook receiver running and happy on the server. You can lean on lectures and notes left in the PowerPoint slides, but make sure you add your own notes to your documentation

- [Using GitHub actions and webhooks](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and webhooks](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
  - Note: this has been the method focused on in lecture

## Part 4 - Diagramming

Include a diagram (or diagrams) of your entire workflow. Meaning it should start with a project change / update, the steps that happen in between, and end with the updated version when the server is queried (web page is accessed)

### Resources

You can use whatever tools you would like, here are some recommended tools that people use

- [Lucid Charts](https://www.lucidchart.com/pages/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
- [Eraser - Cloud Diagrams](https://docs.tryeraser.com/docs/cloud-diagrams)
- PowerPoint and OneNote are still good choices

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course  
   repository.

   - Your repo should contain:
   - `README.md`
   - `website` folder with website pages
   - `Dockerfile`
   - GitHub action yml file
   - webhook related config files
     - container restart script
     - webhook definition file

2. In Pilot, paste the link to your project folder.

## Extra Credit - BYOP

BYOP = Bring Your Own Project

Containerize a web based application of your own. Needs to be way cooler than
a single `index.html` file.

## Extra Credit - By Proxy

Worth 10%

Create a file, `ExtraCredit.md` in your project repository.

You now have a whole workflow, assuming an instance with a public IP (and Elastic IP). Revisit your load balancing project (project 4) and create a continuous deployment workflow for your backend hosts.

Document your continuous deployment solution for your load balancer in `ExtraCredit.md`.
