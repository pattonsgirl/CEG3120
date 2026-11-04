# Project 7 - CD

- [Objectives](#Objectives)
- [Project Overview](#Project-Overview)
- [Part 1 - Script a Refresh](#part-1---script-a-refresh)
- [Part 2 - Listen](#part-2---listen)
- [Part 3 - Send a Payload](#part-3---send-a-payload)
- [Part 4 - Project Description & Diagram](#part-4---project-description--diagram)
- [Testing and Proof](#testing-and-proof)
- [Formatting, Task Text, and Images](#formatting-task-text-and-images)
- [Commits, Sources, and AI](#commits-sources-and-ai)
- [Submission](#Submission)
- [Rubric](Rubric.md)
- [Demonstration](Demonstration-Rubric.md)
- [Troubleshooting](FAQ.md)

## Objectives

- Script a refresh of a running container
- Use GitHub webhooks to keep production up to date
- Validate that a webhook payload came from a trusted sender
- Contrast GitHub webhooks with DockerHub webhooks

## Project Overview

Now that developers can trigger image updates through GitHub Actions, it's time to work on deploying the image in your DockerHub repository to servers that will run the application in the container.

The server running the application in the container will be an EC2 instance.

**Recommended instance specifications**
- 2 CPU Core (included in `t2.medium`)
- 4 GB RAM (included in `t2.medium`)
- 30 GB volume storage

This project requires completion of [Project 6](../Project6/). If you did not accomplish Project 6 you should meet with the instructor at your earliest availability.

Perform all work in your `ceg3120-cicd-lastname-f26` repository.

The documentation requirements are embedded in their respective parts (in order of how I would recommend setting things up). [Part 4 - Project Description & Diagram](#part-4---project-description--diagram) should be at the **top of your README-CD.md** since it is the description and diagramming requirement.

## Part 1 - Script a Refresh

On your AWS instance, build a bash script that stops and removes the formerly running container, pulls the `latest` tagged image from your DockerHub repository, and runs a new container process with the pull'ed image

### Tasks

1. Build (or use a CF-template to build) an EC2 instance
    - Assign an Elastic IP, so that the address your webhook sends to does not change
    - Configure the Security Group:
      - `ssh` from your home IP (`/32`) and the Wright State IP block (`130.108.0.0/16`)
      - the port your site runs on from any IP
      - the `webhook` port (`9000` by default) from GitHub's webhook IP ranges (the `hooks` list at [api.github.com/meta](https://api.github.com/meta)) and your home IP (`/32`) for testing
2. Install Docker to your EC2 instance
3. Test that your EC2 instance can run a container from your DockerHub repository image
4. Craft a bash script that will:
    - stop and remove the formerly running container
    - pull the `latest` tagged image from your DockerHub repository
    - run a new container process with the pull'ed image
      - run as a detached process and with flags to resume running when docker is started (on system start)
    - **copy the bash script** to folder named `deployment` in your GitHub repository

### Documentation

Create `README-CD.md` in root folder of your GitHub repository that details the following:

1. EC2 Instance Details
    - AMI information
    - Instance type 
    - Recommended volume size
    - Security Group configuration
    - Security Group configuration justification / explanation
2. Docker Setup on OS on the EC2 instance
    - How to install Docker for OS on the EC2 instance
    - Additional dependencies based on OS on the EC2 instance
    - How to confirm Docker is installed and that OS on the EC2 instance can successfully run containers
3. Testing on EC2 Instance
    - How to pull container image from DockerHub repository
    - How to run container from image 
      - Note the differences between using the `-it` flag and the `-d` flags and which you would recommend once the testing phase is complete
    - How to verify that the container is successfully serving the web application
4. Scripting Container Application Refresh
    - Description of the bash script
    - How to test / verify that the script successfully performs its taskings
    - **LINK to bash script** in repository

### Resources

## Part 2 - Listen

On the application server, you will configure a listening service to receive messages from GitHub
- this listening service will run your script if a message is delivered
- you will need to validate that requests are coming from GitHub

### Tasks

1. Install [adnanh's `webhook`](https://github.com/adnanh/webhook) to your EC2 instance
2. Create a configuration file - a hook definition - for `webhook` to load when ran.  The hook definition should:
    - Trigger your bash script to run when a payload is received
    - Validate that the payload came from GitHub by checking the signature in its `X-Hub-Signature-256` header with a shared secret
    - Only trigger when your new image is ready to pull
    - **ADD hook definition** to folder named `deployment` in your GitHub repository
      - Your webhook secret is exposed once a copy of this file is in your public repository.  In a production system, that secret would no longer be trusted.  For this project, you are not required to change it and you will not be penalized for using it.
3. Set up a service file such that the `webhook` is set to start listening as soon as the EC2 instance is on.  Enable this service and verify it triggers your bash script to run when a message is received
    - **ADD webhook service file** to folder named `deployment` in your GitHub repository

### Documentation

In `README-CD.md`, include the following details:

1. Configuring a `webhook` Listener on EC2 Instance
    - How to install [adnanh's `webhook`](https://github.com/adnanh/webhook) to the EC2 instance
    - How to verify successful installation
    - Summary of the `webhook` definition file
    - How to verify definition file was loaded by `webhook`
    - How to verify `webhook` is receiving payloads that trigger it
      - how to monitor logs from running `webhook`
      - what to look for in `docker` process views
    - **LINK to definition file** in repository
2. Configure a `webhook` Service on EC2 Instance 
    - Summary of `webhook` service file contents
    - How to `enable` and `start` the `webhook` service
    - How to verify `webhook` service is capturing payloads and triggering bash script
    - **LINK to service file** in repository

## Part 3 - Send a Payload

Utilize a GitHub webhook to send a message to your application server when your GitHub Action has finished pushing a new image.

Choose the event carefully.  Your script pulls `latest`, so a payload is only useful once the new image is in DockerHub.  Research the events GitHub offers, select the one that fits your pipeline, and defend your choice in your documentation.

### Tasks

1. Configure a webhook in your GitHub repository to send a payload to your EC2 instance
    - Payload URL using your Elastic IP, `webhook` port, and hook ID
    - Content type `application/json`
    - The same shared secret your hook definition uses
    - Only the event you chose selected
2. Validate that your webhook *only triggers* when requests are coming from GitHub
3. Research DockerHub webhooks and compare them with GitHub webhooks

### Documentation

In `README-CD.md`, include the following details:

1. Configuring a GitHub Webhook
    - How to enable GitHub to send payloads to the EC2 `webhook` listener
    - Which event you chose, what triggers it to send a payload to the EC2 `webhook` listener, and why you chose it over the other events you considered, including `push`
    - How to verify a successful payload delivery
    - How to validate that your webhook *only triggers* when requests are coming from GitHub
2. GitHub Webhooks vs. DockerHub Webhooks - contrast the two:
    - What event sends a payload, and when that happens in your pipeline
    - How the receiving server can verify who sent the payload
    - Which you would use for this deployment, and why

### Resources

- [adnanh's `webhook`](https://github.com/adnanh/webhook)
- [Using GitHub actions and `webhook`s](https://levelup.gitconnected.com/automated-deployment-using-docker-github-actions-and-webhooks-54018fc12e32)
- [Using DockerHub and `webhook`s](https://blog.devgenius.io/build-your-first-ci-cd-pipeline-using-docker-github-actions-and-webhooks-while-creating-your-own-da783110e151)
- [`webhook` - Hook Rules](https://github.com/adnanh/webhook/blob/master/docs/Hook-Rules.md)
- [GitHub - Creating webhooks](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks)
- [GitHub - Validating webhook deliveries](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries)
- [GitHub - Webhook events and payloads](https://docs.github.com/en/webhooks/webhook-events-and-payloads)
- [GitHub - Viewing webhook deliveries](https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/viewing-webhook-deliveries)
- [Docker - DockerHub webhooks](https://docs.docker.com/docker-hub/repos/manage/webhooks/)
- [Linux Handbook - How to Create a `systemd` Service](https://linuxhandbook.com/create-systemd-services/)

## Part 4 - Project Description & Diagram

Create a diagram (or diagrams) of the continuous deployment process configured in this project.  It should (at minimum) address how the GitHub Action running results in the server running a new container process - again, according to the workflow that this project enables.

Your diagram must have a clean layout and show what happens in GitHub, in DockerHub, and on your AWS instance.

### Documentation

In `README-CD.md`, **add to the top of the document** the following details:

1. Continuous Deployment Project Overview
    - What is the goal of this project
    - What tools are used in this project and what are their roles
    - Diagram of project
    - [If applicable] What is **not working** in this project
2. Resources Section
    - Note: this can be at document top, scattered within document as resources were used, or placed at bottom
    - Add resources used in the project by linking them and making a statement of how it was used.  If generative AI was used, state which platform and what prompts were given and again, a statement of how it was used.

Create a `README.md` in the root folder of your GitHub repository:

1. Summarize the project contents in the repository
2. Link to `README-CI.md` and `README-CD.md` with a brief summary about what users will find in each document. 

### Resources

You can use whatever tools you would like, here are some recommended tools that people use

- [Lucid Charts](https://lucid.co/lucidchart/)
- [Textographo](https://textografo.com/)
- [Mermaid - new markdown feature](https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/)
- [Eraser - Cloud Diagrams](https://docs.eraser.io/cloud-architecture-diagrams)
- PowerPoint and OneNote are still good choices

## Testing and Proof

Add these screenshots to an `images` folder in your repository and embed each one in `README-CD.md` **with a sentence saying what it proves**.

These are in addition to your in-person [demonstration](#demonstration).

1. **Instance and Security Group** - your EC2 instance running, and its Security Group inbound rules, including the port your `webhook` listens on.
2. **Docker on the instance** - `docker --version`, and `docker ps` running without `sudo`.
3. **Site from your image** - `docker ps` showing your DockerHub image running with its port mapping, and a browser showing your site at the instance's public IP.
4. **Refresh script** - `docker ps` before and after running your script, showing a new container ID running the `latest` image.
5. **Restart behavior** - `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container>` showing your restart policy, and `uptime` with `docker ps` after a reboot showing the container came back on its own.
6. **Hook loaded** - `webhook` log output showing your definition file was loaded and your hook is available.
7. **Service** - `systemctl status webhook` showing the service `active` and `enabled`, including after the reboot from item 5.
8. **Payload delivery** - your GitHub webhook's **Recent Deliveries** showing a successful delivery to your instance, and the `webhook` log entry for that delivery.
9. **Negative test** - send a request to your hook that does not meet your trigger rules (for example, a `curl` POST without a valid signature).  Show the response, the `webhook` log entry, and `docker ps` showing that the container ID did not change.
10. **End to end** - after pushing a new `tag` with a visible change, the site in a browser and `docker ps` before and after, showing a new container ID and your change without you logging in to the instance.

## Formatting, Task Text, and Images

- **Formatting:** your README should be easy to read on GitHub - headings, lists, code formatting for commands and file names (`` `docker ps` `` or fenced code blocks), and tables that render. Poor formatting is up to a 10% deduction, scaled by severity - 10% if the document is illegible.
- **Task text:** do not leave project or rubric task text in your documentation. It muddles what your work was versus what the assignment tasking is, and is a 5% formatting deduction. Section headings are fine; pasting the instruction bullets or prompts is not.
- **Images:** every screenshot and your diagram must be **embedded** so it displays in your README on GitHub - not just uploaded to the repo. Use relative paths (`images/delivery.png`), match the filename's capitalization exactly, and avoid spaces in filenames (or wrap the path in angle brackets: `![delivery](<images/my delivery.png>)`). After you push, open your README on GitHub and confirm every image appears. No embedded screenshots is a 5% deduction; some missing or not displaying is 2.5%.

## Commits, Sources, and AI

- **Commit as you work.** The project should be built up over **multiple small commits**, with messages that say what changed (e.g. "Add hook definition with signature rule"). One or two commits for the whole project, or messages like "update", "fixes", or "complete", lose points.
- **Cite your sources.** Cite every source you use - documentation, tutorials, forums, and AI tools - and say what you used it for. You may place citations next to the sections they relate to or in one Sources section.
   - if using generative AI, provide the tool name and the prompt(s) used
   - if using websites, provide the link and a short description of what you used on the page
   - A submission with no citations loses 10%.
- **Your work must be your own and must describe what you built.** Submissions that appear AI-generated without citation, or that describe work you didn't do, are held at 0 until you meet with the instructor.
- **Never commit secrets** - your `.pem` key or your DockerHub PAT. A committed secret is a 5% deduction. If a secret is ever committed, replace it right away - removing it from the file does not remove it from your `git` history. The webhook secret in your hook definition file is the one exception for this project - see [Part 2](#part-2---listen).

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course  
   repository.

    Your repo should contain:
    - `README.md`
    - `README-CD.md` (and `README-CI.md` from P6)
    - `web-content` folder with application
    - `Dockerfile`
    - GitHub action `yml` file in `.github/workflows`
    - `deployment` folder with:
      - `bash` script
      - `webhook` / `hook` definition file
      - `webhook` service file
    - `images` folder with your screenshots
    - diagram image(s), or a Mermaid diagram in `README-CD.md`

2. In Pilot, paste the link to your project folder.

## Rubric

[Project Rubric](Rubric.md)

## Demonstration

[Demonstration Rubric](Demonstration-Rubric.md)

## Troubleshooting

[Project FAQ](FAQ.md)
