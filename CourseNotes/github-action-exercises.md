# Exercises for Learning GitHub Actions

[My sample workflows](https://github.com/pattonsgirl/CEG3120/tree/main/Projects/Project4/sample-workflows)

## Output a message from runner

[Victoria Lo - Create your first workflow](https://lo-victoria.com/github-actions-101-creating-your-first-workflow)  
[GitHub Actions - Quickstart](https://docs.github.com/en/actions/quickstart)

```
name: my-first-flow
on:
  push:
    branches: [main]
    workflow-dispatch:
jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello World!"
```

## List repository contents

```
name: my-first-flow
on:
  push:
    branches: [main]
    workflow-dispatch:
jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello World!"
      - uses: actions/checkout@v3
      - run: ls
      - run: echo "Goodbye!"
```

## Play with secrets

```
name: my-first-flow
on:
  push:
    branches: [main]
    workflow-dispatch:
jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        # - docker login -u wsukduncan -pass mysupersecret
        # this would "hard code" secret values and they would be publicly viewable by looking at the workflow file (== bad)
      - shell: bash
        env:
          SUPER_SECRET: ${{ secrets.DOCKERHUB_USERNAME }}
        run: |
          echo "$SUPER_SECRET"
```

GitHub will not "show" values that are encrypted secrets - you will always see the asterisks.  You can brute force it, but... why?  Keeping secrets secret is a good thing.

## Outline needs to build and push image to DockerHub

See resources in P4 for some really useful samples

1. checkout repo contents to runner (needs to access site content to copy in to image & Dockerfile of instructions)
2. use an action to login to DockerHub - put credentials (or at least pat) in Action Secrets for repository
3. use actions to set up runner to use docker
4. use action to build image and push image to DockerHub

## Use Semantic Versioning w/ `tags`

1. checkout repo contents to runner (needs to access site content to copy in to image & Dockerfile of instructions)
2. use an action to login to DockerHub - put credentials (or at least pat) in Action Secrets for repository
3. use actions to set up runner to use docker
4. define metadata from repo to generate tags (Docker metadata-action)
5. use action to build image and push image to DockerHub with set of tags

- [GitHub - docker/metadata-action](https://github.com/docker/metadata-action)
- [Docker - Manage Tag Labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)
- [Generating `latest` from `metadata-actions`](https://github.com/docker/metadata-action#latest-tag)
- [Syntax to specify multiple tags](https://stackoverflow.com/questions/70868900/github-actions-specify-multiple-tags-with-docker-build-push-actionv2)