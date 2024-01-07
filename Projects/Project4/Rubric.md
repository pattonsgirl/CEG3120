# Project 4 Rubric

/ 16

## Repo contents ( / 4)

- `README-CI.md`
- `website` folder with website pages
- `Dockerfile`
- GitHub action `yml` file in `.github/workflows`

## docker basics + Dockerfile ( / 5)

- CI Project Overview
- Run project locally
  - how you installed docker + dependencies (WSL2, for example)
  - how to build the container from `Dockerfile`
  - how to run the container
  - how to view the project (open a browser...go to ip and port...)

## GitHub Actions and DockerHub ( / 6)

- Create DockerHub public repo
  - process to create
- How to authenticate with DockerHub via CLI using Dockerhub credentials
  - what credentials would you recommend providing?
- How to push container image to Dockerhub (without GitHub Actions)
- **Link** to your DockerHub repository
- Configuring GitHub Secrets
  - How to set a secret
  - What secret(s) are set for this project
- Behavior of GitHub workflow
  - what does it do and when
  - variables to change (repository, etc.)

## Diagramming ( / 1)

- Logically diagrammed steps for continuous integration workflow

## Point Deductions (- / 8)

- Dockerfile does not build an image per specification
- Image never pushed to DockerHub repository
- Secrets not defined
- Workflow does not build and push image to DockerHub
