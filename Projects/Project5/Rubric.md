# Project 5 Rubric

/ 18

## Repo contents ( / 6)

- `README-CD.md` (and `README-CI.md` from P4)
- `website` folder with website pages
- `Dockerfile`
- GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - container restart script
  - `hook` definition file

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
- Setting up a `webhook` on the server
  - How to install adnanh's `webhook` to server
  - How to start the `webhook`
    - since our instance's reboot, we need to handle this
- `webhook` task definition file
  - Description of what it does
  - Where it should be on server
- How to configure GitHub OR DockerHub to message the listener

## Demonstration ( / 1)

- Either in-person demonstration OR video file showing full CI / CD workflow in action 

## Diagramming ( / 1)

- Logically diagrammed steps for continuous deployment workflow

## Point Deductions: (- / 6)

- Action does not push image(s) to DockerHub or images are do not use semantic versions in tagging
- Web hook does not trigger with payload from DockerHub or GitHub
- Markdown (README) does not use good formatting practice