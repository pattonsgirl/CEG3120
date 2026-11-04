# Project 6 Rubric

## Project Score: / 65

Grading notes:
- 1 point per box unless noted.
- Research-only notes for an unfinished step (clearly labeled as research) earn up to half of that item's points.
- Documented values (image names, tags, links) must match your repository and DockerHub.

## GitHub Repository Contents ( / 4)

- [ ] `README-CI.md`
- [ ] `web-content` folder with web application (at least two `.html` files, including `index`, and one `.css` file)
- [ ] `Dockerfile`
- [ ] GitHub action `yml` file in `.github/workflows`

## Part 4 - Project Description & Diagram ( / 8)

Documentation Requirements:

1. Continuous Integration Project Overview
    - [ ] What is the goal of this project
    - [ ] What tools are used in this project and what are their roles
    - Diagram of project
        - [ ] clean layout
        - [ ] what happens in cloned repo
        - [ ] what happens in GitHub
        - [ ] what happens in DockerHub
    - [If applicable] What is **not working** in this project - scored with the Incomplete work deduction
2. Resources Section
    - [ ] Uses good formatting
    - [ ] Citations appropriate to project / include notes on how they were used.

## Part 1 - Create a Docker container image ( / 9)

Documentation Requirements:

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
- [ ] **Public** DockerHub image repository shows at least one tagged image

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
    - [ ] **Link** to the Part 2 workflow file using a commit permalink
3. Testing & Validating
    - [ ] How to test that your workflow did its tasking
    - [ ] How to verify that the image in DockerHub works when a container is run using the image
    - [ ] **Link** to your DockerHub repository 

Task Requirements - 2 pts each:

- [ ] Secrets `DOCKER_USERNAME` and `DOCKER_TOKEN` set in repository
- [ ] Part 2 workflow triggers on push to `main` only, uses repository secrets, and uses official actions (not `run` commands) at their latest versions
- [ ] GitHub Action has successfully run the workflow at least once

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

- [ ] Workflow triggers on push of tags only, uses `docker/metadata-action`, and uses repository secrets
- [ ] GitHub Action has successfully run the workflow at least once with a tag as the event
- [ ] DockerHub shows `latest`, `major`, and `major`.`minor` tags from the GitHub Action

## Testing & Proof ( / 10)

Screenshots embedded in `README-CI.md`, each with a sentence saying what it proves.

- [ ] Local run - `docker ps` and a browser showing both pages with the CSS applied
- [ ] Repository secrets - Actions secrets page showing both secret names
- [ ] Main trigger - successful workflow run from a push to `main`, with the commit SHA visible
- [ ] Branch negative test - a commit on another branch and no workflow run
- [ ] Change to image - a visible site change pushed to `main`, then the new image pulled and run showing the change
- [ ] Tag trigger - `git tag -l` output and a successful workflow run with a tag as its event
- [ ] Tag negative test - a commit pushed without a tag and no workflow run
- [ ] Tag set - DockerHub showing `latest`, `major`, and `major`.`minor`
- [ ] Two releases - DockerHub tags and digests showing `major` and `latest` moved to the new image while the prior `major`.`minor` stayed on the old image
- [ ] Rollback - containers run from two `major`.`minor` tags, each serving its version of the site

## Point Deductions - Penalty Total: 

- Incomplete work - the `Dockerfile` or workflow has apparent issues, or no successful workflow run pushed an image to DockerHub. Apply **one** tier, based on how `README-CI.md` documents it:
   - [ ] 10% penalty - README indicates the work is complete
   - [ ] 5% penalty - README notes the areas where blockers were hit
   - [ ] 2% penalty - README notes the blockers, the things tried, and clearly delineates next steps that have not been tested; the `Dockerfile` and workflow are in line with what the README describes
- [ ] Secret committed to the repository (such as a DockerHub PAT) - 5% penalty
- [ ] images not included in markdown documentation - 5% penalty (no screenshots embedded); 2.5% penalty (some screenshots missing or not displaying) - the diagram is scored under Part 4
- [ ] poor markdown formatting - up to 10% penalty, scaled by severity (10% = illegible)
    - includes project / rubric tasking text left in the documentation - 5% penalty
- [ ] Single or mass commit - project not built up over multiple small, descriptive commits - 5% penalty
- [ ] No citations - sources (including AI tools, with the prompts used) not cited - 10% penalty
- [ ] Late submission - 10% per day, up to 3 days
- [ ] Submission appears AI-generated without citation or describes work not done - score held at 0 pending an instructor meeting

Percentage deductions are taken from the total possible (e.g. 10% of 65 = 6.5).
