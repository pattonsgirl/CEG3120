# FAQ Guide for Project 6

Goal of this guide is to track errors as they crop up and recommended solutions.

# Where to Start

The pipeline is a chain.  Find the first step that did not happen, then troubleshoot that step:

1. Image builds and runs locally - `docker build`, then `docker run`
2. Workflow run started - **Actions** tab in your repository
3. Workflow run succeeded - open the run and read the first step that failed
4. New image or tags are in DockerHub - check the tags and their modified times
5. Pulled image serves the new site - `docker pull`, `docker run`, then check your browser

# Docker

## Permission denied while trying to connect to the Docker daemon socket
```
bob@Duncan-Dell:~$ docker run -it ubuntu bash
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create": dial unix /var/run/docker.sock: connect: permission denied.
```

### Reason

> The Docker daemon binds to a Unix socket, not a TCP port. By default it's the root user that owns the Unix socket, and other users can only access it using sudo. The Docker daemon always runs as the root user.

> If you don't want to preface the docker command with sudo, create a Unix group called docker and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the docker group. On some Linux distributions, the system automatically creates this group when installing Docker Engine using a package manager. In that case, there is no need for you to manually create the group.

[See all notes, including security concerns, here](https://docs.docker.com/engine/install/linux-postinstall/)

### Solution
```
 sudo usermod -aG docker $USER
```

## Cannot connect to docker daemon
```
# Error:
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```
### Reason
Usually a problem for Windows users who need to install Docker Desktop.  Docker Desktop must be running for `docker` commands
to work in WSL2

### Solution
Start Docker Desktop

## bind for port in use
Sample command:
```
docker run -d -p 80:80 --name webserver httpd
```
```
# Container error
docker: Error response from daemon: driver failed programming external connectivity on endpoint webserver 
(bd57efb73c738e3b271db180ffbee0a56cae86c8193242fbc02ea805101df21e): Error starting userland proxy: Bind for 0.0.0.0:80: 
unexpected error (Failure EADDRINUSE).
```
### Reason
Multiple containers cannot bind to the same host port.  In this case, the user ran another container that bound to host 
port 80, and running this container also with host port 80 causes the error.  An exited container will still have the host port reserved

### Solution
- View all containers, even exited containers:
  - `docker ps -a`
- Remove containers that bind to the host port you are attempting to bind to
  - `docker rm container_id_or_name`

## `denied: requested access to the resource is denied`
### Reason
Docker could not push to the repository.  You may not be logged in, the image tag may not include your DockerHub username, or your PAT may not have write access.

### Solution
- Confirm you are logged in with `docker login`
- Confirm the image is tagged as `<dockerhub username>/<repository>:<tag>`
- Confirm your PAT's permissions in DockerHub

## `COPY` file not found during `docker build`
### Reason
`COPY` paths are relative to the build context - the `.` at the end of `docker build`.

### Solution
Run `docker build` from the folder that holds your `Dockerfile` and `web-content`, and check the spelling and capitalization of the path.

## Default "It works!" page or a 403 instead of your site
### Reason
Your files did not end up in the web content folder `httpd` serves, or there is no `index.html`.

### Solution
Look at what is in the container, then compare it to the path in your `Dockerfile`:
```
docker exec <container> ls /usr/local/apache2/htdocs/
```
The file must be named `index.html`, in lowercase.

## Old site showing after a pull
### Reason
An older container may still be running on that port, the container was not recreated after the pull, or your browser cached the page.

### Solution
- Use `docker ps` to see which image and container are bound to the port
- Stop and remove the old container, then run a new one from the pulled image
- Reload the page without your browser's cache, or use a private window

# GitHub Actions

## Workflow never runs
### Reason
GitHub did not find a valid workflow for that event.

### Solution
- Confirm the file is in `.github/workflows` and ends in `.yml` or `.yaml`
- Open the file on GitHub and in the **Actions** tab to check for YAML errors
- Confirm the branch in your trigger matches your branch name - the sample workflows use `master`, and your project uses `main`

## `Username and password required`
### Reason
The login step did not receive your credentials.

### Solution
Confirm your repository secrets are named exactly `DOCKER_USERNAME` and `DOCKER_TOKEN`, and that your workflow refers to those same names.  Secrets must be set under **Secrets and variables** > **Actions** in the repository that runs the workflow.

## `Unexpected input` warning, or an action fails after updating its version
### Reason
Fields can change between versions of an action.  The sample workflows are intentionally dated.

### Solution
Read the latest documentation for that action and update your `with:` fields to match.

## Push denied inside the Action
### Reason
Login worked, but the push was not allowed.

### Solution
- Confirm your PAT has read and write access
- Confirm the image name in your workflow uses your DockerHub username and the correct repository

# Semantic Versioning

## Tag did not start a workflow run
### Reason
`git push` does not send tags by default.

### Solution
Check that the tag is on GitHub, and push it if it is not:
```
git ls-remote --tags origin
git push origin <tag>
```

## Tag ran the old version of my workflow
### Reason
A tag runs the workflow file from the commit it points to.

### Solution
Commit and push your workflow changes first, then create a new tag on that commit.

## `major` or `major`.`minor` tags are missing from DockerHub
### Reason
Your `git` tag may not be valid semantic versioning, or your build step may not be using the tags generated by `docker/metadata-action`.

### Solution
- Use a full version, such as `v1.2.0`
- Read the `docker/metadata-action` step in your workflow log to see which tags it generated
- Confirm your build step uses that step's output

## Reusing a tag
Create a new version instead of moving an existing tag.  A version should always point to the same build, which is what makes rolling back possible.

# Expected Behavior

## No workflow run on another branch or on a commit without a tag
This is correct if your trigger is set up for that part of the project.  These are the negative tests in [Testing and Proof](README.md#testing-and-proof) - you do not need to fix them.

---

> **Note:** These were identified by Claude as common troubleshooting points. As always, do your own research to verify your error and cite your sources!
