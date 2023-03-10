# Project 5

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- Require git tagging?
- [Part 2 - Deployment](#Part-3---Deployment)
- [Part 3 - Diagramming](#Part-4---Diagramming)
- [Submission](#Submission)
- [Extra Credit - By Proxy](#Extra-Credit---By-Proxy)
- [Rubric](Rubric.md)

## Objectives

- Containerize an application with Docker
- Use webhooks to keep production up to date - continuous deployment

## Project Overview

For this project you will be continuing to use your CICD repo made in project 4.

You will notice that each part has "Milestone" labels and dates. This project is not due until
12/2. Completion of each milestone **by the date specified for the milestone** will get you 10%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone data to the Dropbox for Project 5 in Pilot.

## Parts & Milestones

- Tagging images?
  - Milestone due 3/31
- [Part 2 - Deployment](#Part-2---Deployment)
  - Milestone due 4/7
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - All parts are due 4/10
  - No EC

## Part 1 - Tagging

## Part 2 - Deployment

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

## Part 3 - Diagramming

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

## Extra Credit - By Proxy

Worth 10%

Create a file, `ExtraCredit.md` in your project repository.

You now have a whole workflow, assuming an instance with a public IP (and Elastic IP). Revisit your load balancing project (project 3) and create a continuous deployment workflow for your backend hosts.

Document your continuous deployment solution for your load balancer in `ExtraCredit.md`.
