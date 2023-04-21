## APIs

REST API (Application Programming Interface), you'll commonly see HTTP requests sent by the client **to** servers to perform a service:
- GET - request info
- POST - send info (new record)
- PUT - update info (existing record)
- DELETE - remove entry

In a RESTful API, the client sends these requests to the server, and the server interprets them and performs the request.

CRUD APIs are another common term:
- C = Create
- R = Read
- U = Update
- D = Delete

This [guide by programming historian](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask) has a great APIs 101 overview.

Are there other types of APIs?  You bet!

[This video has an overview of the most common APIs](https://www.youtube.com/watch?v=hkXzsB8D_mo&ab_channel=AmbientCoder).  This article also does a good dive into [understanding RPC, REST, and GraphQL APIs](https://apisyouwonthate.com/blog/understanding-rpc-rest-and-graphql/)

### GET / Read

- [Python + Flask - GET / Read](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)

### POST

- USES PYTHON2 - [Key differences](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)
    - [Python + Flask - POST with a webform (login)](https://pythonbasics.org/flask-http-methods/)
    - [Flask + SQLite](https://pythonbasics.org/flask-sqlite/)

### DELETE

## Databases

## Bonus: Python tricks

### Tools to make `requirements.txt`

```
# install
pip3 install pipreqs

# Run in current directory
python3 -m  pipreqs.pipreqs .
# OR (--force overwrites old file)
pipreqs --force .
```

## Deploying a Flask App

- [Flask - Deploying to Production](https://flask.palletsprojects.com/en/2.2.x/deploying/)

Sample using `waitress`
```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
```

## Securing APIs

- [Web API Security | Basic Auth, OAuth, OpenID Connect, Scopes & Refresh Tokens](https://www.youtube.com/watch?v=x6jUDfpESmA&ab_channel=AmbientCoder)
- [Modern Guide to OAuth](https://fusionauth.io/learn/expert-advice/oauth/modern-guide-to-oauth)

## Tools for testing APIs

- [HURL](https://github.com/Orange-OpenSource/hurl)
- [insomnia](https://docs.insomnia.rest/insomnia/send-your-first-request)
- [postman](https://www.postman.com/)
    - [link to download Postman](https://www.postman.com/downloads/)

## Work Along Objectives

1. Setup a read-only flask app (GET)
    - use a Python list
    - use a database
2. Enable record writing (POST)
3. Enable record deletion (DELETE)
4. Containerize that app
5. Play with load balancers
    - host site
    - host API
6. Secure API?
7. Break out database?
8. API documentation with Doxygen? https://www.doxygen.nl/
9. API testing?

### Offline Docker & Containers

- https://docs.docker.com/engine/install/binaries/
    - https://download.docker.com/linux/static/stable/x86_64/
- https://github.com/Shopify/docker/blob/master/docs/installation/binaries.md
    - Recommended systemd files: https://github.com/moby/moby/tree/master/contrib/init/systemd
    - Remembering how to enable systemd files: https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
- docker copy / save: https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository
