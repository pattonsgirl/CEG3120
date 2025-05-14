## Module 1
- DIY git server in container
- Docker starters: `busybox`?, pull, run, start, stop, exec
- Cheatsheet now contains:
  - SSH
  - git
  - docker

## Module 2
- Manual build of AWS env
  - Network ACLs
  - Security Groups
- export / import container filesystem

## Module 3
- CF Template
- User data script
  - installs docker
  - pull nginx image
  - clones website repo (repo is public & provided - may fork it)
  - runs containers (with flags to start on system boot)
 
## Module 4
- Load balancer with HAProxy
- Dockerfile to build image with website using nginx
- CF Template to build 1 haproxy instance, 3 webserver instances
- AWS NAT Gateway
- EC: containerize haproxy

## Module 5
- Continuous Integration w/ GitHub Actions
- Changes to website codebase == new container in DockerHub
- Require use of .gitignore / restrictive conditions to trigger builds
- Keep Angular app?

## Module 6
- Continuous Deployment w/ Webhooks
- Payload from GH Webhook or Dockerhub Webhook
- Continue using Adnanh's webhook for listener - containerize it?
- Require hook match-triggers
- Tie back to hosts on load balancer

## Module 7
- Docker compose
