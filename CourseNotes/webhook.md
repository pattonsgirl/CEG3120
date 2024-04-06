## webhook as a listening service

Using [adnanh's webhook](https://github.com/adnanh/webhook)

- installing
- running
- defining a hook
- protecting the hook
- consider: messages to the either (what happens once this EIP is released?)

### Installing `go` webhook module
1. Download latest `go` release: https://go.dev/dl/
2. `# tar -C /usr/local -xzf go1.22.2.linux-amd64.tar.gz`
3. Add `export PATH=$PATH:/usr/local/go/bin` to `~/.profile` or `~/.bash_profile`
4. Test successful install & add to PATH with `go version`
5. Install webhook module: `go install github.com/adnanh/webhook@latest`
6. Installs to `~/go/bin/webhook` if installed in `~` directory
7. Verify install with `~/go/bin/webhook --version`
    - is not a service by default.  Need to set up a service file.  See below section on handling reboots
    - install location is not in PATH.  Need to add to PATH (similar to `go` above)

### Installing with `apt`
1. `sudo apt-get install webhook`
2. Run `which webhook` for installation path
3. Auto-installed as a service. Use `systemctl` commands to verify `status`

## DockerHub or GitHub as server (messenger)?

- [About GitHub WebHooks](https://docs.github.com/en/webhooks-and-events/webhooks/about-webhooks)
- [Docker Docs - WebHooks](https://docs.docker.com/docker-hub/webhooks/)

## testing webhook
- [hookdeck](https://hookdeck.com/)

## handling reboots

build your own service with `systemd`
- [Linux Handbook - Create `systemd` services](https://linuxhandbook.com/create-systemd-services/)

examples of setting a hook as a service
- [analythium - shinyproxy webhook](https://hub.analythium.io/docs/shinyproxy-webhook/)
- [adnanh webhook discussion](https://github.com/adnanh/webhook/discussions/562#discussioncomment-1498404)

viewing service logs
- [](https://github.com/adnanh/webhook/discussions/569)
- Cliff notes:
    - assuming `-verbose` is in service
    - `journalctl -xfe _SYSTEMD_UNIT=webhook.service`
