# Project 5 Rubric

/ 21

## Repo contents ( / 6)

- `README.md`
- `website` folder with website pages
- `Dockerfile`
- GitHub action yml file in `.github/workflows`
- webhook related config files
  - container restart script
  - webhook definition file

## docker basics + Dockerfile ( / 5)

- Project Overview
- Run project locally
  - how you installed docker + dependencies (WSL2, for example)
  - how to build the container
  - how to run the container
  - how to view the project (open a browser...go to ip and port...)

## GitHub Actions and DockerHub ( / 4)

- Create DockerHub public repo
  - process to create
- How to authenticate with DockerHub via CLI using Dockhub credentials
  - what credentials would you recommend providing?
- Configuring GitHub Secrets
  - what credentials are needed - DockerHub credentials (do not state your credentials)
  - set secrets and secret names
- Behavior of GitHub workflow
  - what does it do and when
  - variables to change (repository, etc.)

## Deployment ( / 4)

- Container restart script
  - what it does
- Webhook task definition file
  - what it does
- Setting up a webhook on the server
  - How you created you own listener
  - How you installed and are running the [webhook on GitHub](https://github.com/adnanh/webhook)
- Setting up a notifier in GitHub or DockerHub

## Diagramming ( / 2)

- Locigically diagrammed steps for continuous integration workflow
- Locigically diagrammed steps for continuous deployment workflow
