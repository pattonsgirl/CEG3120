## What is Continuous Deployment?

> Continuous deployment is a strategy in software development where code changes to an application are **released automatically** into the production environment. This automation is driven by a series of predefined tests. Once new updates pass those tests, the system pushes the updates directly to the software's users. - [IBM - Continuous Deployment](https://www.ibm.com/topics/continuous-deployment)

> Continuous delivery is a software development practice where code changes are automatically **prepared** for a release to production. A pillar of modern application development, continuous delivery expands upon continuous integration by deploying all code changes to a testing environment and/or a production environment after the build stage. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process. - [AWS - Continuous Delivery Explained](https://aws.amazon.com/devops/continuous-delivery/)

Both Continuous Deployment & Continuous Delivery use the acronym CD

![AWS - CI CD CD](https://d1.awsstatic.com/product-marketing/DevOps/continuous_delivery.4f4cddb8556e2b1a0ca0872ace4d5fe2f68bbc58.png)

### What we need to combine

- image (tagged with semantic versions) is pushed to DockerHub registry
- want our application to run on an AWS instance
    - run a container based on `latest` image in DockerHub
- want application to auto-update when new image is pushed to DockerHub registry

## CI / CD Tools

[See CI/CD Tools in continuous integration](continuous-integration.md#ci--cd-tools)

## Getting Notified

How can we decide when to update our container?

Option 1:
- Keep DockerHub open - hit refresh now and then, go `pull` new image and `run` fresh container
- Repeat for all systems that need updated

Option 2:
- **poll** DockerHub for new image versions
    - servers view this like kids asking, "Are we there yet?"
- run script to `run` fresh container if new image is pulled

Option 3: :white_check_mark:
- if a new image is delivered to DockerHub, have DockerHub send message to system
- system receives message, uses it to trigger `pull` and `run` fresh container 

## Exploring WebHooks

## API Analysis Tools

- [Postman](https://www.postman.com/)
- [RequestBin](https://requestbin.com/)
- [Insomnia](https://insomnia.rest/) ~~not cookies~~