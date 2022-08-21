# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
- [Part 3 - Deployment](#Part-3---Deployment)
- [Part 4 - Diagramming](#Part-4---Diagramming)
- [Submission](#Submission)
- [Extra Credit - DIY](#Extra-Credit---DIY)
- [Rubric](Rubric.md)

## Objectives

- Containerize an application with Docker
- Automate the project pipeline with GitHub Actions
- Explore usage of webhooks to keep production up to date

## Project Overview

For this project you will be creating a fresh repository - the link is in Pilot under Content - Projects - Project 5. This is the repo you will be using for this project.

You will notice that each part has "Milestone" labels and dates. This project is not due until 4/22. Completion of each milestone **by the date specificied for the milestone** will get you 10% of extra credit per milestone date met. To qualify, you must submit your project to the Dropbox for Project 5 in Pilot.

## Part 1 - Dockerize it

- **Milestone Participation due 3/30**

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
  - how to build the container
  - how to run the container
  - how to view the project (open a browser...go to ip and port...)

## Part 2 - GitHub Actions and DockerHub

- **Milestone Participation due 4/8**

### Tasks

- Create DockerHub account: https://hub.docker.com/ (select Free tier if prompted)
- Create Public Repository in DockerHub
- Set GitHub Secrets named DOCKER_USERNAME and DOCKER_PASSWORD with your respective information filled out.
- Set up GitHub Actions workflow to build and push docker image to DockerHub
  - Use workflow templated here: https://docs.github.com/en/actions/guides/publishing-docker-images#publishing-images-to-docker-hub

### Documentation

- Update `README.md` in main folder of your repo to include:

- Create DockerHub public repo
  - process to create
- How to authenticate with DockerHub via CLI using Dockhub credentials
  - what credentials would you recommend providing?
- Configuring GitHub Secrets
  - what credentials are needed
  - set secrets and secret names
- Behavior of GitHub workflow
  - what does it do and when
  - variables to change (repository, etc.)

### Resources

- [GitHub Actions - Docker Docs](https://docs.docker.com/ci-cd/github-actions/)

## Part 3 - Deployment

- **Milestone Participation due 4/20**

### Tasks

- For this piece, use an EC2 instance.
- Install docker on the instance
- Create a webhook set up to automatically deploy updates to the container image

### Documentation

- Update `README.md` in main folder of your repo to include:

- Container restart script
  - what it does
- Webhook task definition file
  - what it does
- Setting up a webhook on the server
  - How you created you own listener
  - How you installed and are running the [webhook on GitHub](https://github.com/adnanh/webhook)
- Setting up a notifier in GitHub or DockerHub

### Resources

Note: the challenging part here is getting the webhook reciever running and happy on the server. You can lean on lectures and notes left in the PowerPoint slides, but make sure you add your own notes to your documentation

- [Using GitHub actions and webhooks](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and webhooks](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
  - Note: this has been the method focused on in lecture

## Part 4 - Diagramming

Include a diagram (or diagrams) of your entire workflow. Meaning it should start with a project change / update, the steps that happen in between, and end with the updated version when the server is queried (web page is accessed)

### Resources

You can use whatever tools you would like, here are some recommend tools that people use

- [Lucid Charts](https://www.lucidchart.com/pages/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
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

## Extra Credit - DIY

Worth 10%

Pick a project of yours or that you are interested in, and create a docker container of your project.

- Database
- Java program
- php site
- something else?

Document and include:

- Dockerfile that builds your project and environment
- Image with your project (link from DockerHub) / `docker pull` command
- Instructions to run container from image
