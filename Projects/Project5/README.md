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

- Track versions using `git tag` in Actions
- Use webhooks to keep production up to date

## Project Overview

For this project you will be continuing to use your `cicd` repo made in project 4.

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it nicely.

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5%
of extra credit per milestone date met. To qualify, you must submit your project on the milestone date to the Dropbox for Project 4 in Pilot.

All parts for the project are due 4/12

- [Part 1 - Versions](#Part-1---Versions)
  - Milestone due 4/3
- [Part 2 - Deployment](#Part-2---Deployment)
  - Milestone due 4/10
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - All parts are due 4/12
  - No EC

## Part 1 - Versions

### Tasks

- git tag
- adjust action to use tag

### Documentation

Create `README-CD.md` in main folder of your repo that details the following:

- CD Project Overview
  - (what are you doing, why, what tools)


## Part 2 - Deployment

### Tasks

- For this piece, use an EC2 instance.
- Install docker on the instance
- Create a webhook set up to automatically deploy updates to the container image - see Resources for this part

### Documentation

- Update `README-CD.md` in main folder of your repo to include:

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

Include a diagram (or diagrams) of the continuous deployment process.  A good diagram will label tools used and how things connect.  This diagram would probably look best near your project description.

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
   - `README-CD.md` (and `README-CI.md` from P4)
   - `website` folder with website pages
   - `Dockerfile`
   - GitHub action `yml` file in `.github/workflows`
   - webhook related config files
     - container restart script
     - webhook definition file

2. In Pilot, paste the link to your project folder.


