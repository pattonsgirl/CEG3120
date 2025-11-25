# Project 4 Rubric

## Project Score: / 55

## GitHub Repository Contents ( / 4)

- [ ] `README-CI.md`
- [ ] `web-content` folder with web application
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`

## Part 4- Project Description & Diagram ( / 8)

Documentation Requirements:

1. Continuous Integration Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram of project
        - [ ] clean layout
        - [ ] what happens in cloned repo
        - [ ] what happens in GitHub
        - [ ] what happens in DockerHub
    - [ ] [If applicable] What is **not working** in this project
2. Resources Section
    - [ ] Uses good formatting
    - [ ] Citations appropriate to project / include notes on how they were used.

## Part 1 - Create a Docker container image ( / 9)

Documenation Requirements:

1. `Dockerfile` & Building Images
    - [ ] Explanation and links to web site content
    - [ ] Explanation of and link to `Dockerfile`
    - [ ] How to build an image from the repository `Dockerfile`
      - [ ] Include tagging requirements when planning to use DockerHub for a container image repository
    - [ ] How to run a container that will serve the web application from the image built by the `Dockerfile`

Task Requirements:

- Dockerfile
    - [ ] Builds from `httpd:2.4`
    - [ ] Copies all content in `web-content` into the container filesystem in the default web content directory for `httpd`
- [ ] provides working application when container is run using built image
- [ ] DockerHub image repository shows at least one tagged image

## Part 2 - GitHub Actions and DockerHub ( / 17)

Documentation Requirements:
1. Configuring GitHub Repository Secrets:
    - [ ] How to create a PAT for authentication (**and** recommended PAT scope for this project)
    - [ ] How to set repository Secrets for use by GitHub Actions
    - [ ] Describe the Secrets set for this project
2. CI with GitHub Actions
    - [ ] Explanation of workflow trigger
    - [ ] Explanation of workflow steps
    - Explanation / highlight of values that need updated if used in a different repository
      - [ ] changes in workflow
      - [ ] changes in repository
    - [ ] **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - [ ] How to test that your workflow did its tasking
    - [ ] How to verify that the image in DockerHub works when a container is run using the image
    - [ ] **Link** to your DockerHub repository 

Task Requirements - 2 pts each:

- [ ] Secrets set in repository
- [ ] Workflow defined, triggers on push to main
- [ ] GitHub Action has run workflow at least once

## Part 3 - Semantic Versioning ( / 17)

Documentation Requirements:

1. Generating `tag`s 
    - [ ] How to see tags in a `git` repository
    - [ ] How to generate a `tag` in a `git` repository
    - [ ] How to push a tag in a `git` repository to GitHub
2. Semantic Versioning Container Images with GitHub Actions
    - [ ] Explanation of workflow trigger
    - [ ] Explanation of workflow steps
    - Explanation / highlight of values that need updated if used in a different repository
      - [ ] changes in workflow
      - [ ] changes in repository
    - [ ] **Link** to workflow file in your GitHub repository
3. Testing & Validating
    - [ ] How to test that your workflow did its tasking
    - [ ] How to verify that the image in DockerHub works when a container is run using the image
    - [ ] **Link** to your DockerHub repository with evidence of the tag set

Task Requirements - 2 pts each:

- [ ] Workflow defined, trigger on push of tags
- [ ] GitHub Action has run workflow at least once with tag being the event
- [ ] DockerHub shows semantically tagged versions from GH Action

## Common Point Deductions:

- [ ] (-30% = 18 pts) Documentation not well organized with markdown OR includes project descriptive text
- [ ] (-10% = 6 pts) Documentation fails to address what was not implemented / implies the project is fully functional.  Always document shortcomings and note what is "research" on how the rest should be done
- [ ] No citations of referenced material
> [!WARNING]
> May result in Academic Integrity Violation with a penalty of a 0 on the project
