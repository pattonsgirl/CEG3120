## PROJECT 6 - Placeholder

## Automate Deployment

Here's the deal. DockerHub and GitHub and many other things offer these things called "webhooks". Think very basic triggers that can notify when actions happen (actions in the lowercase sense, GitHub Actions are their own thing). The goal is to automate deploying updates. I am including some resources that may (or may not) be good directions to check out. I will accept either of the following strategies:

1. Use a GitHub webhook to trigger an update script to pull changes on the server
   - [How to Automatically Deploy from GitHub to server using webhook](https://betterprogramming.pub/how-to-automatically-deploy-from-github-to-server-using-webhook-79f837dcc4f4)
2. Use DockerHub webhooks to pull an updated image
   - [Build CI/CD Pipelines Using Docker](https://circleci.com/blog/build-cicd-piplines-using-docker/)
   - [docker hook - GitHub repo](https://github.com/schickling/docker-hook)
   - [docker image puller - GitHub repo](https://github.com/tuxity/docker-image-puller)

The [Webhook](https://github.com/adnanh/webhook) package has the most potential usefulness.

## Rise of the Discord Bot

- Dockerize your python bot. Place in repo in folder named `Discord-Bot`. Include the following:
  - the docker bot code & api
  - the Dockerfile that builds the image
  - a `README.md` file that contains documentation on how the project works
- The hard part here is dealing with the secret. It shouldn't exist in the image we send around - then anyone would have it. It should only exist on servers we trust running the container.
- My recommended method here will be to create a folder that we share with the running container - this is known as a mount or a volume.
