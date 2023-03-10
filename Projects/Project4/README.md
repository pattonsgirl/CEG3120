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

For this project you will be creating a fresh repository - the link is in Pilot under Content - Projects - Project 4. This is the repo you will be using for this project.

You will notice that each part has "Milestone" labels and dates. This project is not due until
12/2. Completion of each milestone **by the date specified for the milestone** will get you 10%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone date to the Dropbox for Project 4 in Pilot.

## Parts & Milestones

- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
  - Milestone due 3/17
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
  - Milestone due 3/24
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - All parts are due 3/27
  - No EC

## Part 1 - Dockerize it

### Tasks

- Create new GitHub repo (link to create located in Pilot in Content -> CI/CD Projects)
- In a folder named `website`, add the contents of your website
  - this can be a site you created in another class, pet project of yours, or the site in `site.tar.gz`
- Install Docker
  - You can install Docker in WSL2 or in an EC2 instance.
- Create a container image that will run a webserver and contains your "website"
  - you can use `apache2` or `nginx` as the webserver
- Create a `Dockerfile` with instructions on how to build the image
- Add site content & `Dockerfile` to repo

### Documentation

- Create `README.md` in main folder of your repo that details the following:
- Project Overview
- Run Project Locally
  - how you installed docker + dependencies (WSL2, for example)
  - how to build the container from the `Dockerfile`
  - how to run the container
  - how to view the project running in the container (open a browser...go to IP and port...)

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

## Part 3 - Diagramming

Include a diagram (or diagrams) of the continuous integration process.

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
   - `README.md`
   - `website` folder with website pages
   - `Dockerfile`
   - GitHub action `yml` file

2. In Pilot, paste the link to your project folder.