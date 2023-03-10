# Project Overview

- what is the point of this project and what tools are used
- Part 4 - Diagramming goes here
  - Include a diagram (or diagrams) of your entire workflow. Meaning it should start with a project change / update, the steps that happen in between, and end with the updated version when the server is queried (web page is accessed)

# Run Project Locally

- how you installed docker + dependencies (WSL2, for example)
- how to build the container
- how to run the container
- how to view the project running in the container (open a browser...go to ip and port...)

# DockerHub

- Process to create public repo in DockerHub
- How to authenticate with DockerHub via CLI using Dockerhub credentials
  - what credentials would you recommend providing?
- How to push container to Dockerhub

# GitHub Actions

- Configuring GitHub Secrets
  - What secrets were set based on what info
- Behavior of GitHub workflow
  - what does it do and when
  - what variables in workflow are custom to your project

# Deployment

- Description of container restart script
- Setting up a webhook on the server
  - How you created you own listener
  - How you installed the [webhook on GitHub](https://github.com/adnanh/webhook)
  - How to keep the webhook running if the instance is on
- Description of Webhook task definition file
- Steps to set up a notifier in GitHub or DockerHub
