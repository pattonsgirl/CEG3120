# Project 4 Rubric

## Project Score: / 60

## Milestone Extra Credits

- [ ] Milestone 1 = Part 1 - +5% = 3 pts
- [ ] Milestone 2 = Part 1 + 2 - +5% = 3 pts

## GitHub Repository Contents ( / 4)

- [ ] `README-CI.md`
- [ ] `angular-site` folder with Angular application
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`

## Part 1 - Docker-ize it ( / 21)

1. Docker Setup
    - [ ] How to install Docker for your OS
    - [ ] Additional dependencies based on your OS
    - [ ] How to confirm Docker is installed and your system can successfully run containers
2. Manually Setting up a Container
    - [ ] How to run a container to test the Angular application
      - [ ] Include explanation of flags / arguments used
    - [ ] Commands needed internal to the container to get additional dependencies
    - [ ] Commands needed internal to the container to run the application
    - [ ] How to verify that the container is successfully serving the Angular application
      - [ ] validate from container side
      - [ ] validate from host side
3. `Dockerfile` & Building Images
    - [ ] Summary / explanation of instructions written in the `Dockerfile`
    - [ ] How to build an image from the repository `Dockerfile`
    - [ ] How to run a container that will serve the Angular application from the image built by the `Dockerfile`
    - [ ] How to verify that the container is successfully serving the Angular application
      - [ ] validate from container side
      - [ ] validate from host side
5. Working with your DockerHub Repository
    - [ ] How to create a public repo in DockerHub
    - [ ] How to create a PAT for authentication (note recommended scope for this task)
    - [ ] How to authenticate with DockerHub via CLI using DockerHub credentials
    - [ ] How to push container image to your DockerHub repository
    - [ ] **Link** to your DockerHub repository for this project

## Part 2 - GitHub Actions and DockerHub ( / 11)

1. Configuring GitHub Repository Secrets:
    - [ ] How to create a PAT for authentication (note recommended scope for this task)
    - [ ] How to set repository Secrets for use by GitHub Actions
    - [ ] Describe the Secrets set for this project
2. CI with GitHub Actions
    - [ ] Summary of what your workflow does and when it does it
    - [ ] Explanation of workflow steps
    - [ ] Explanation / highlight of values that need updated if used in a different repository
      - [ ] changes in workflow
      - [ ] changes in repository
    - [ ] **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - [ ] How to test that your workflow did its tasking
    - [ ] How to verify that the image in DockerHub works when a container is run using the image

## Part 3 - Project Description & Diagram ( / 8)

1. Continuous Integration Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram
      - [ ] cleanly presented
      - Explains the project workflow in terms of:
        - [ ] developer role
        - [ ] GitHub role
        - [ ] Docker Hub role
    - [ ] [If applicable] What is **not working** in this project
2. Resources Section
    - [ ] included (embedded at relevant points or in stand alone section)
    - [ ] well formatted

## `Dockerfile` ( / 8)
2 pts / task

- [ ] builds from logical container image on DockerHub
- [ ] installs required dependencies
- [ ] copies application into container
- [ ] starts application when container is run using built image

## GitHub Action Workflow ( / 8)
2 pts / task

- [ ] Secrets defined in repository settings
- [ ] triggers on push to main
- [ ] builds an image based on your `Dockerfile`
- [ ] pushes image to your DockerHub repository

## Common Point Deductions:

- [ ] (-30% = 18 pts) Documentation not well organized with markdown OR includes project descriptive text
- [ ] (-10% = 6 pts) Documentation fails to address what was not implemented / implies the project is fully functional.  Always document shortcomings and note what is "research" on how the rest should be done
- [ ] No citations of referenced material
> [!WARNING]
> May result in Academic Integrity Violation with a penalty of a 0 on the project
