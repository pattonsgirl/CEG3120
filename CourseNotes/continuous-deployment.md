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

Option 1: :x:
- Keep DockerHub open - hit refresh now and then, go `pull` new image and `run` fresh container
- Repeat for all systems that need updated

Option 2: :x:
- **poll** DockerHub for new image versions
    - servers view this like kids asking, "Are we there yet?"
- run script to `run` fresh container if new image is pulled

Option 3: :white_check_mark:
- if a new image is delivered to DockerHub, have DockerHub send a **payload** to system
- system receives message, uses it to trigger `pull` and `run` fresh container 

## Exploring WebHooks

A `webhook` (also called a web callback or HTTP push API) is a way for an app to provide other applications with real-time information. A `webhook` delivers data to other applications as it happens, meaning you get data immediately. - SendGrid

The name `webhook` is a simple combination of **web**, referring to its HTTP-based communication, and the **hook**ing programming function that allows apps to intercept calls or other events that might be of interest. - [RedHat](https://www.redhat.com/en/topics/automation/what-is-a-webhook)

### Detour - REST APIs vs WebHooks

In a REST API (Application Programming Interface), you'll commonly see HTTP requests sent by the client **to** servers to perform a service:
- GET - request info
- POST - send info (new record)
- PUT - update info (existing record)
- DELETE - remove entry

In a RESTful API, the client sends these requests to the server, and the server interprets them and performs the request.

If we used a RESTful API model for this project, every x hours / minutes / seconds, we (the client who needs info) would send a GET request to DockerHub for info about our repo, check metadata for a "last update" timeframe, then act on that info to update our running container.

**What if...**

What if we defined when we (the client) wanted to be notified?  In this way, WebHooks are also referred to as **reverse-APIs** or **event-driven APIs**, and the focus is on a POST request **from** the server.

The client defines where requests will be sent.  The server is provided with where to send requests, and after what event.  The client then parses the POST message from the server and acts on the information.

[This video compares APIs to WebHooks](https://www.youtube.com/watch?v=Zle9oe5xxZg&ab_channel=DemoHub%7CDemosForModernDataTools) by comparing getting updates for stock values.

### Server side

In this model, the server holder information about the object we want updates on.

From the focus on our project, the server is DockerHub, which hosts our images.

The server needs to know:
- trigger for when to send a POST message
- where to send POST request
    - this gets defined by client

### Client side

The client is not going to bother the server, just set a destination for where to send info when an event it cares about occurs.

Client needs:
- a service listening for POST requests
- to parse the POST request 
    - check that valid server sent it (you expected a message)
    - check metadata for actionable information
- a definition of what to do from info in POST request

Notes: 
- this service will need to be running on a port
- there should be some "secret" set to validate the message is authentic

### Resources

- [SendGrid - What's a webhook and how does it work?](https://sendgrid.com/blog/whats-webhook/)
- [Zapier - What are webhooks with invoice system example](https://zapier.com/blog/what-are-webhooks/)
- [mParticle - APIs vs webhooks](https://www.mparticle.com/blog/apis-vs-webhooks/)
- [VIDEO - Ambient Coder - Webhooks vs Websockets vs HTTP Streaming - Which Event-Driven API to use? - start to 5:14](https://www.youtube.com/watch?v=6RvlKYgRFYQ&ab_channel=AmbientCoder)

## API Analysis Tools

- [Postman](https://www.postman.com/)
- [RequestBin](https://requestbin.com/)
- [Insomnia](https://insomnia.rest/) ~~not cookies~~