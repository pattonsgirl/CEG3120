# Project 5 Rubric

## Project Score: / XX

## Milestone Extra Credits

- [ ] Milestone 1 = Part 1 - +5% = X pts
- [ ] Milestone 2 = Part 1 + 2 - +5% = X pts

## GitHub Repository Contents ( / 4)

- `README-CD.md` (and `README-CI.md` from P4)
- `angular-site` folder with application
- `Dockerfile`
- GitHub action `yml` file in `.github/workflows`
- `deployment` folder with:
  - `bash` script
  - `webhook` / `hook` definition file
  - `webhook` service file

## Part 1 - Semantic Versioning ( / 5)

- CD Project Overview
  - (what are you doing, why, what tools)
- How to generate and push a `tag` in `git`
- Behavior of GitHub workflow
  - when does it do things
  - what does it do
- Link to Docker Hub repository

## Part 2 - Deployment ( / 16)

- Instance information - at minimum public IP and OS
- How to install Docker to the instance given it's OS
- `bash` script
  - Purpose
  - Description of script taskings
  - Location on instance filesystem
  - LINK to your script in a folder named `deployment`
- Purpose of installing & steps to install / setup adnanh's `webhook` to the instance
- `webhook` / hook task definition file
  - Description of what it does
  - Location on instance filesystem
  - LINK to your hook definition file in a folder named `deployment`
- How to start the `webhook` listening (without using service)
- How to test that the listener successfully listens & triggers the script
  - include:
    - how to monitor logs from the `webhook` program
    - what to look for in `docker` process views
- How to configure GitHub OR DockerHub to message the listener 
- How to modify or create a `webhook` service file such that your `webhook` listener is listening as soon as the system is booted
  - include commands to reload the service respective to files changed (`webhook` service file versus hook definition file)
  - LINK to your `webhook` service file in a folder named `deployment`

## Diagramming ( / 2)

- Logically diagrammed steps for continuous deployment workflow

## Demonstration ( / 10)

1. current state of site running on server, before making a change
    - show the page in the browser
    - show the docker status
2. making a change to the project file (from your local system)
3. `commit` and `push` of the change (from your local system)
4. `tag` the `commit` and `push` the `tag` (from your local system)
5. the GitHub Action triggering, relevant logs that it worked
6. DockerHub receiving a new set of tagged images (modified time should be visible)
7. status of `webhook` running as a service on the server
8. `webhook` logs that validate container refresh has been triggered
9. post-change state of site running on server
    - show the page in the browser
    - show the docker status

## Point Deductions:

- `Dockerfile` does not build viable container image to run application (-5%)
- Action does not push image(s) to DockerHub  (-5%)
- Images in DockerHub do not use semantic versions in tagging (-5%)
- Web hook does not trigger with payload from DockerHub or GitHub (-5%)
- Markdown (README) does not use good formatting practice (-10%)
- Documentation misleads completion of work (-10%)
  - You may document what should be done / happen, but you must also document what is not working  
  and your troubleshooting so far
- No citations of referenced material (-10%)
  - May result in Academic Integrity Violation with a penalty of a 0 on the project
