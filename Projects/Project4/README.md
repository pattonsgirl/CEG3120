# Project 4

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Docker-ize it](#Part-1---Docker-ize-it)
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
- [Part 3 - Diagramming](#Part-3---Diagramming)
- [Submission](#Submission)
- [Rubric](Rubric.md)

## Objectives

- Containerize an application with Docker
- Automate the project pipeline with GitHub Actions - continuous integration

## Project Overview

For this project you will be creating a fresh repository in order to have a public repo . The link is in Pilot under Content - Projects - CI -> CD. This is the repo you will be using for Projects 4 & 5.

The documentation bullet points are written linearly.  As long as the information can be found, I am okay with you organizing it to your logical preferences.

### The Application

[angular-bird.zip](angular-bird.zip) is a *simple* Angular application.  It requires the following software stack to run:
- Node.js version 18
- Angular version 15.0.3 (installed with `npm`, the node package manager)

#### Helpful Hints
- `node:18-bullseye` is the recommended container image to utilize from Docker Hub
- `npm install -g @angular/cli` - Install angular with `npm`, the Node.js package manager
- *when run from the project folder* `ng serve --host 0.0.0.0` - "compiles" and starts the Angular app, binds to any IP (`0.0.0.0`)
  - By default, `ng serve` binds to `localhost` - which is only accessible inside the container
  - [Stack Overflow - How to allow access outside localhost](https://stackoverflow.com/questions/43492354/how-to-allow-access-outside-localhost)
- the Angular app will run over the "default" port - `4200`

Credit for the Angular application goes to Erik Jenkins	& Ryan Nicolai.

## Parts & Milestones

Completion of each milestone **by the date specified for the milestone** will get you 5% of extra credit per milestone date met. To qualify, you must submit your project on the milestone date to the Dropbox for Project 4 in Pilot.

See Pilot for Milestone dates & project due date.

- [Part 1 - Docker-ize it](#Part-1---Docker-ize-it)
  - Milestone EC available
- [Part 2 - GitHub Actions and DockerHub](#Part-2---GitHub-Actions-and-DockerHub)
  - Milestone EC available
- [Part 3 - Diagramming](#Part-3---Diagramming)
  - Due at project due date - no milestone EC available

## Part 1 - Docker-ize it

### Tasks

1. Install Docker to your system.
    - You may use an EC2 instance if your system is not Docker compatible.
2. Create DockerHub account: https://hub.docker.com/
    - select Free tier if prompted
3. Create a Public Repository in your DockerHub account named `YOURLASTNAME-CEG3120`
4. Create new GitHub repo (link to create located in Pilot in Content -> CI/CD Projects)
    - This repository will be Public (your previous repo was Private) and you will have privileges to manipulate the repository settings (needed later)
5. To your GitHub repository, in a folder named `angular-site`, extract the contents of [angular-bird.zip](angular-bird.zip)
6. Run a container with the `node:18-bullesye` container image and configure it to run and server the Angular application in `angular-site`
    - See [Project Overview](#project-overview) for very useful hints
7. Create a `Dockerfile` in your GitHub repository that builds a container image with the following requirements:
    - utilizes an appropriate base image with the `FROM` command
    - completes installation of the application software stack with `RUN` command(s)
    - copies the `angular-site` application to the container with the `COPY` command
    - starts the Angular application when a container is run from the image built with the `Dockerfile` with the `CMD` command 
      - Note: as needed according to your base  selection
    - use of the `EXPOSE` command is optional
    - [Relevant article from dev.to](https://dev.to/rodrigokamada/creating-and-running-an-angular-application-in-a-docker-container-40mk)
8. Build a container image using your `Dockerfile`.  Confirm that a container run using your container image will successfully start and run the Angular application.
9. Log in to Docker Hub from the command line using an appropriately scoped Personal Access Token (not your account password) 
10. Push the container image built by your `Dockerfile` to your DockerHub repository named `YOURLASTNAME-CEG3120` 

### Documentation

Create `README-CI.md` in root folder of your GitHub repository that details the following:

1. Docker Setup
    - How to install Docker for your OS
    - Additional dependencies based on your OS
      - Ex. Windows systems need WSL2
    - How to confirm Docker is installed and your system can successfully run containers
2. Manually Setting up a Container
    - How to run a container to test the Angular application
      - Include explanation of flags / arguments used
    - Commands needed internal to the container to get additional dependencies
    - Commands needed internal to the container to run the application
    - How to verify that the container is successfully serving the Angular application
      - validate from container side
      - validate from host side
3. `Dockerfile` & Building Images
    - Summary / explanation of instructions written in the `Dockerfile`
    - How to build an image from the repository `Dockerfile`
    - How to run a container that will serve the Angular application from the image built by the `Dockerfile`
    - How to verify that the container is successfully serving the Angular application
      - validate from container side
      - validate from host side
5. Working with your DockerHub Repository
    - How to create a public repo in DockerHub
    - How to create a PAT for authentication (note recommended scope for this task)
      - **DO NOT** add your DockerHub PAT to your documentation 
    - How to authenticate with DockerHub via CLI using DockerHub credentials
      - **DO NOT** add your DockerHub PAT to your documentation 
    - How to push container image to your DockerHub repository
    - **Link** to your DockerHub repository for this project

## Part 2 - GitHub Actions and DockerHub

### Tasks

1. Create an appropriately scoped Personal Access Token for GitHub Actions to use to access your DockerHub repository
2. In your GitHub repository, configure GitHub Action Secrets named `DOCKER_USERNAME` and `DOCKER_TOKEN` containing your DockerHub username & DockerHub access token, respectively.
3. Set up a GitHub Actions workflow to build and push container images to your DockerHub repository
    - workflow should trigger when a commit is pushed to the main branch
    - workflow should utilize repository secrets for authentication
    - workflow should utilize actions as opposed to run commands

### Documentation

In `README-CI.md`, include the following details:

1. Configuring GitHub Repository Secrets:
    - How to create a PAT for authentication (note recommended scope for this task)
    - How to set repository Secrets for use by GitHub Actions
    - Describe the Secrets set for this project
2. CI with GitHub Actions
    - Summary of what your workflow does and when it does it
    - Explanation of workflow steps
    - Explanation / highlight of values that need updated if used in a different repository
      - changes in workflow
      - changes in repository
    - **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - How to test that your workflow did its tasking
    - How to verify that the image in DockerHub works when a container is run using the image


### Resources

- [Docker Docs - CICD with GitHub Actions](https://docs.docker.com/ci-cd/github-actions/)
- [GitHub Actions - build-push-action documentation](https://github.com/marketplace/actions/build-and-push-docker-images)
- [GitHub - publishing images to DockerHub](https://docs.github.com/en/actions/guides/publishing-docker-images#publishing-images-to-docker-hub)

## Part 3 - Diagramming

Include a diagram (or diagrams) of the continuous integration process configured in this project.  It should (at minimum) address how the developer changing code results in a new image available in a DockerHub repository.

### Documentation

In `README-CI.md`, add to the top of the document the following details:

1. Continuous Integration Project Overview
    - What is the goal of this project
    - What tools are used in this project and what are their roles
    - Diagram of project
    - [If applicable] What is **not working** in this project
2. Resources Section
    - Note: this can be at document top, scattered within document as resources were used, or placed at bottom
    - Add resources used in the project by link.  If generative AI was used, state which platform and what prompts were given.

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

## Rubric

[View Project Rubric](Rubric.md)
