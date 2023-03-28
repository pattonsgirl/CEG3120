# GitHub Actions 101

> GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.  
GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.  
GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure. - [GitHub Docs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)

## Workflows

A workflow is a configurable automated process that will run one or more jobs

- Workflow is written in `YAML` files located in `.github/workflows`
- will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule
- multiple workflows can exist in a repository

There are existing templates for:
- Automation
    - Think automation of GitHub repo - auto messages and issue creation
- CI
    - Code-scanning
    - Run security scanners on codebase
    - Linters
- CD 
    - push code places

### events / triggers

An event is a specific activity in a repository that triggers a workflow run.

[All events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) are listed here, but let's scope it down to what we will play with.

Run a workflow when you [**`push`**](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#push) a `tag` or `commit`
```
# Any ol' push
on:
  push
# Specifically `main` or on `release`
on:
  push:
    branches:
      - 'main'
      - 'releases/**'
    paths-ignore:
      - '.github/workflows'
    # why do this?
    tags:        
      - v2
      - v1.*
```

The **schedule** event allows you to trigger a workflow at a scheduled time.
```
  on:
    schedule:
      # * is a special character in YAML so you have to quote this string
      - cron:  '30 5,17 * * *'
```

To **manually trigger a workflow** in GitHub Actions, use the workflow_dispatch event.

```
on: workflow_dispatch
```

Runs your workflow **when activity on a pull request** in the workflow's repository occurs.
- [pull request event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request)

### jobs

A workflow run is made up of one or more jobs, which run in parallel by default.  You can set job dependencies [if one job needs to be complete before another can start](https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow).  A job is a set of steps in a workflow that is executed on the same runner.
```
# on
jobs:
  job-name:
    # runs-on:
    # steps:
```

### runners

The jobs defined in the workflow require an environment where they can be executed. Runners are servers that allows these steps to be executed in a virtual environment. It can be GitHub-hosted or self-hosted.

[Available GitHub hosted runners](https://docs.github.com/en/actions/using-jobs/choosing-the-runner-for-a-job)

```
jobs:
  job-name:
    runs-on: ubuntu-latest
    # steps:
```

### steps

Steps are tasks within the job.  `run` steps execute commands.  `uses` steps use actions (basically scripts that do tasks)

```
jobs:
  # This workflow contains a single job called "say_hello"
  say_hello:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Runs a single command using the runners shell
      - name: Say Hello
        run: echo Hello World!

      # Runs a set of commands using the runners shell
      - name: Say Goodbye
        run: |
          echo Job Finished.
          echo Goodbye!
       # action to checkout repo to runner
      - uses: actions/checkout@v2
```

### actions

An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task.

[Check out the GitHub Marketplace](https://github.com/marketplace?type=actions) for community shared actions.

[You can create your own actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions) in `.github/actions`

### Debugging / viewing a workflow

To view your workflows, go to GitHub repo -> Actions 
- Click workflow name
- Click the run you want to see
- Click the job you want to see 
- View the results of each step

## git tags & GitHub Releases

Branches allow you to code features or fix bugs without impacting the main code branch

Tags are essential for marking a point in time in your code, such as a new release of your application.

A Release is a GitHub concept - it is created from an existing tag and exposes release notes and links to download the software or source code from GitHub.

- [Circle CI - tags vs branches](https://circleci.com/blog/git-tags-vs-branches/)
- [CodeBerg - tags and releases](https://docs.codeberg.org/git/using-tags/)
  - Note: this doc uses a GitHub clone named CodeBerg, but covers the essence really well.

### tags

[git-scm - tagging basics](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

```
$ git commit -am “changes”
$ git tag -a v1.6.1
# optional -m "tag info"
$ git show v1.6.1
# Docker requires semantic versioning
# [Major version].[minor version].[patch]
$ git push origin v1.6.1
```

> A lightweight tag (no `-a`) is very much like a branch that doesn’t change — it’s just a pointer to a specific commit. - [Git SCM](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

> Annotated tags (with `-a`) are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). It’s generally recommended that you create annotated tags so you can have all this information; but if you want a temporary tag or for some reason don’t want to keep the other information, lightweight tags are available too. - [Git SCM](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

### tags + Actions

- [GitHub - docker/metadata-action](https://github.com/docker/metadata-action)
- [Docker - Manage Tag Labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/)

### Releases

Creates a `.tar.gz` of repo at given point

Why is this useful?
- Could use `ADD` in `Dockerfile` and provide release URL
  - [Docker - ADD vs COPY](https://docs.docker.com/develop/develop-images/dockerfile_best-practices)
- Could trigger a workflow if a release occurs (great for software packages)

## Secrets

[GitHub Docs - Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

Environment Secrets
- Secrets for your environments? Environment secrets help secure automation related to specific deployment environments. Example: secrets specific to development versus production and systems you may have unique accounts for.
- [Adam the Automater - Environment Secrets](https://adamtheautomator.com/github-actions-secrets/#Creating_Secrets_For_an_Environment)

- [Forcing the viewing of secrets... even though you shouldn't](https://stackoverflow.com/questions/63003669/how-can-i-see-my-git-secrets-unencrypted)

## Semantic Versioning

[The full rule set of semantic versioning](https://semver.org/)

Given a version number MAJOR.MINOR.PATCH, increment the:
1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backwards compatible manner
3. PATCH version when you make backwards compatible bug fixes

## `latest` tag

- [Generating `latest` from `metadata-actions`](https://github.com/docker/metadata-action#latest-tag)
- [Syntax to specify multiple tags](https://stackoverflow.com/questions/70868900/github-actions-specify-multiple-tags-with-docker-build-push-actionv2)

## Workflow Status Badge

[Get your own status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) on how your workflows are going