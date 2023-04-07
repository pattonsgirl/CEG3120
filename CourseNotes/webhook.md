## restarting a container

## webhook 

Using [adnanh's webhook](https://github.com/adnanh/webhook)

- installing
- running
- defining a hook
- protecting the hook
- consider: messages to the either (what happens once this EIP is released?)

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