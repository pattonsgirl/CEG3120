# FAQ Guide for Project 5

Goal of this guide is to track errors as they crop up and recommended solutions.

# Docker
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

# GitHub Actions

# Webhooks
