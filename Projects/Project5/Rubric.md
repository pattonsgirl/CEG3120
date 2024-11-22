# Project 5 Rubric

/ 20

## Repo contents ( / 6)

- `README-CD.md` (and `README-CI.md` from P4)
- `website` folder with website pages
- `Dockerfile`
- GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - container restart script
  - `hook` definition file
  - webhook service file

## Semantic Versioning ( / 3)

- CD Project Overview
  - (what are you doing, why, what tools)
- How to generate a `tag` in `git` / GitHub
- Behavior of GitHub workflow
  - what does it do and when
- Link to Docker Hub repository (as additional proof)

## Deployment ( / 7)

- How to install Docker to your instance
- Container restart script
  - Justification & description of what it does
  - Where it should be on server
- Setting up a `webhook` listener on the instance
  - How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the instance
- `webhook` task definition file
  - Description of what it does
  - Where it should be on the instance (if someone were to use your setup)
- How to start the `webhook`
- How to modify/ create a webhook service file such that your webhook listener is listening as soon as the system is booted
    - include commands to reload the service respective to files changed (webhook service file versus hook definition file)
- How to configure GitHub OR DockerHub to message the listener

## Demonstration ( / 3)

- Either in-person demonstration OR video file showing full CI / CD workflow in action 

## Diagramming ( / 1)

- Logically diagrammed steps for continuous deployment workflow

## Point Deductions: (- / 6)

- Action does not push image(s) to DockerHub or images are do not use semantic versions in tagging
- Web hook does not trigger with payload from DockerHub or GitHub
- Markdown (README) does not use good formatting practice
