# Project 4 Rubric

/ 30

## Repo contents ( / 4)

- `README-CI.md`
    - if your documentation does not use good organization with markdown, it may receive 0 credit.
- `angular-site` folder with Angular application
- `Dockerfile`
- GitHub action `yml` file in `.github/workflows`

## Part 1 - Docker-ize it ( / 11)

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
  - how to push container image to DockerHub
  - **Link** to your DockerHub repository for this project

## Part 2 - GitHub Actions and DockerHub ( / 5)

- Configuring GitHub Secrets:
  - How to set a secret for use by GitHub Actions
  - What secret(s) are set for this project
- Behavior of GitHub workflow
  - summary of what your workflow does
  - **Link** to workflow file in your GitHub repository
  - summary of what a user would need to change or configure if using your workflow to duplicate your project

## Part 3 - Diagram ( / 2)

- Logically diagrammed steps for this project's continuous integration workflow

## `Dockerfile` ( / 4)
- builds from logical container image on DockerHub
- installs required dependencies
- copies application into container
- starts application when container is run using built image

## GitHub Action Workflow ( / 4)
- Secrets defined in repository settings
- triggers on logical action in repository
- build an image based on your `Dockerfile`
- pushes image to your DockerHub repository