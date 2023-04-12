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

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it nicely.

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone date to the Dropbox for Project 4 in Pilot.

All parts for the project are due 3/29

- [Part 1 - Dockerize it](#Part-1---Dockerize-it)
  - Milestone due 3/20
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
  - Milestone due 3/27
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - All parts are due 3/29
  - No EC

## Part 1 - Dockerize it

### Tasks

- Create new GitHub repo (link to create located in Pilot in Content -> CI/CD Projects)
- To your repo in a folder named `website`, add the contents of your website
  - this can be a site you created in another class, pet project of yours, or the site in `site.tar.gz`
  - if using `site.tar.gz` put your own flair / text in `index.html` (#makegradingfunagain)
- Install Docker
  - You can install Docker in WSL2 or in an EC2 instance.
- Create a container image that will run a webserver and contains your website
  - you can use `apache2` or `nginx` as the webserver
- Create a `Dockerfile` and use it to build an image with your website files and dependencies
- Add site content & `Dockerfile` to your repo

### Documentation

Create `README-CI.md` in main folder of your repo that details the following:

- CI Project Overview
  - (what are you doing, why, what tools)
- Run Project Locally
  - how to install docker + dependencies (WSL2, for example)
  - how to build an image from the `Dockerfile`
  - how to run the container
  - how to view the project running in the container (open a browser...go to IP and port...)

## Part 2 - GitHub Actions and DockerHub

### Tasks

- Create DockerHub account: https://hub.docker.com/
  - select Free tier if prompted
- Create Public Repository in DockerHub
- Set GitHub Secrets named DOCKER_USERNAME and DOCKER_PASSWORD with your respective information filled out.
- Set up GitHub Actions workflow to build and push docker image to DockerHub

### Documentation

- Add to `README-CI.md` to include:

- Process to create public repo in DockerHub
- How to authenticate with DockerHub via CLI using Dockerhub credentials
  - what credentials would you recommend providing?
- How to push container image to Dockerhub (without GitHub Actions)
- Configuring GitHub Secrets
  - How to set a secret
  - What secret(s) are set for this project
    - Note: do not copy paste your secrets into your documentation
- Behavior of GitHub workflow
  - what does it do and when
  - what variables in workflow are custom to your project
    - think may need to be changed if someone else is going to use it or you reuse it

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
   - `website` folder with website pages
   - `Dockerfile`
   - GitHub action `yml` file in `.github/workflows`
   - diagram image(s)

2. In Pilot, paste the link to your project folder.