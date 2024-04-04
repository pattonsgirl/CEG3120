#! /bin/bash

# kill the old container process - stopped & then removed
docker stop flaskapp
docker remove flaskapp
# pull fresh image
docker pull wsukduncan/spring24:latest
# run new container by name, with restart automagic
docker run -d -p 80:5000 --name flaskapp --restart always wsukduncan/spring24:latest
