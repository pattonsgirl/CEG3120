# FAQ Guide for Project 7

Goal of this guide is to track errors as they crop up and recommended solutions.

# Docker

See the [Project 6 FAQ](../Project6/FAQ.md) for general Docker errors, including:

- [Permission denied while trying to connect to the Docker daemon socket](../Project6/FAQ.md#permission-denied-while-trying-to-connect-to-the-docker-daemon-socket)
- [Cannot connect to docker daemon](../Project6/FAQ.md#cannot-connect-to-docker-daemon)
- [bind for port in use](../Project6/FAQ.md#bind-for-port-in-use)

# Where to Start

The deployment is a chain.  Find the first step that did not happen, then troubleshoot that step:

1. GitHub Action run succeeded - **Actions** tab in your repository
2. New image is in DockerHub - check the modified time on the `latest` tag
3. GitHub sent a payload - **Settings** > **Webhooks** > your webhook > **Recent Deliveries**
4. `webhook` received the payload and the rules passed - `journalctl -u webhook -f`
5. Your script ran - `docker ps` shows a new container ID with a recent `CREATED` time
6. New site is served - reload the page in your browser, and use a private window if it looks unchanged

# Refresh Script

## Container name is already in use
```
docker: Error response from daemon: Conflict. The container name "/mysite" is already in use
```
### Reason
A stopped container still holds its name until it is removed.  Your script ran `docker run` before the old container was removed.

### Solution
Confirm your script runs `docker stop` and `docker rm` using the same name as `--name` in `docker run`.  View all containers, even exited containers, with:
```
docker ps -a
```

## Script stops on the first run because there is no container
```
Error response from daemon: No such container: mysite
```
### Reason
There is nothing to stop or remove the first time the script runs, or after a container was removed by hand.  If your script exits on errors, it stops here before pulling the image.

### Solution
Decide how your script handles a container that does not exist, then test your script both with and without a running container.

## Script works by hand but not from `webhook`

### Reason
`webhook` does not run from your shell.  It may run as a different user, from a different folder, and with a different environment.

### Solution
- Use the full path to your script in `execute-command`
- Use full paths to any files your script uses
- Make sure your script is executable: `chmod +x <script>`
- Start your script with a shebang line, such as `#!/bin/bash`
- Make sure the user running `webhook` can run `docker` - see the [Project 6 FAQ](../Project6/FAQ.md#permission-denied-while-trying-to-connect-to-the-docker-daemon-socket)

## `bad interpreter` or `no such file or directory` when a script exists
### Reason
The file was saved with Windows line endings.

### Solution
Check for and remove the `\r` characters:
```
file <script>
sed -i 's/\r$//' <script>
```

## Container does not come back after a reboot
### Reason
The container has no restart policy, or the `docker` service is not enabled.

### Solution
```
docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container>
systemctl is-enabled docker
```

# `webhook` Service

## Service will not start

### Solution
Read the error, then check that the path to `webhook` and the path to your hook definition file in your service file are correct.
```
systemctl status webhook
journalctl -u webhook -n 50 --no-pager
which webhook
```
Run `sudo systemctl daemon-reload` and restart the service after every edit to your service file.

## `couldn't load hooks from file!`
### Reason
Your hook definition file has invalid JSON or YAML, or the path to it is wrong.

### Solution
Check for missing commas, brackets, and quotes.  Running `webhook` by hand shows the error right away, but stop your service first so that the port is free:
```
sudo systemctl stop webhook
webhook -hooks <hook definition file> -verbose
```
A loaded hook shows `found 1 hook(s) in file` and `loaded: <your hook id>`.

## `webhook` does not show any activity
Use `-verbose` in your service file to see more detail, then follow the logs while you send a payload:
```
journalctl -u webhook -f
```

## `Hook not found.`
### Reason
The URL does not match your hook's `id`.

### Solution
The default URL format is below.  The `id` must match exactly, including capitalization.
```
http://<elastic ip>:9000/hooks/<your hook id>
```

# GitHub Webhook

## Delivery fails or times out
### Reason
GitHub cannot reach `webhook` on your instance.

### Solution
- Confirm your Payload URL uses your current Elastic IP and the correct port
- Confirm your Security Group allows the port from GitHub's `hooks` ranges at [api.github.com/meta](https://api.github.com/meta)
- Confirm your instance is running.  Learner Lab instances stop when your session ends.
- Confirm `webhook` is listening:
```
sudo ss -tlnp | grep 9000
```

## `Hook rules were not satisfied.`
### Reason
This is expected for some deliveries:

- The `ping` GitHub sends when you create a webhook is not a workflow run
- A workflow run sends a payload when it is requested, when it is in progress, and when it is completed - only a successful completed run should pass your rules

It is a problem if a **successful completed** run also shows this message.

### Solution
In **Recent Deliveries**, open that delivery and compare its payload to your rules.

- Confirm the Secret in GitHub exactly matches the secret in your hook definition file
- Confirm your signature rule uses the `X-Hub-Signature-256` header
- Confirm your webhook's Content type is `application/json`
- Confirm the names and values in your rules match the payload, including capitalization

## GitHub shows a successful delivery, but the site did not change
### Reason
A `200` response only means `webhook` received the request.  By default, `webhook` also returns `200` when your rules are not satisfied, and it does not wait for your script to finish.

### Solution
Read the response in **Recent Deliveries**, then check the `webhook` logs for what happened next.

## Testing without pushing a new tag
In **Recent Deliveries**, open a delivery and select **Redeliver** to send the same payload again.

# Container Refresh

## Script ran, but the old site is still showing
### Reason
Your script may have pulled before the new image was pushed, or it may be running something other than `latest`.

### Solution
- Confirm your webhook uses the **Workflow runs** event, not `push`
- Confirm the Action succeeded and the `latest` tag in DockerHub has a new modified time
- Confirm your script runs the same image and tag that it pulled
- Compare the image the container is running against the image pulled:
```
docker ps
docker images
```
- Reload the page without your browser's cache, or use a private window

## `no space left on device`
### Reason
Each refresh leaves the older image on your instance.

### Solution
```
docker image prune
df -h
```
