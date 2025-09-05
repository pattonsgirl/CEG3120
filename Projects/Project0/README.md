# Project 0 - Basics Guide

In your repo for this course, create a folder named `basics-guide` with a file named `README.md`. 

In this file you will be creating your own documentation on the commands & tasks you will use repetitively in this course.

This document should markdown for formatting in a way that is clean for you.  If you would prefer tables, you can make tables in markdown.  [markdown.org](https://www.markdownguide.org/) has quick references to anything you'd like to do.

List resources and reference you used in a `Resources` section on your page or by citing them as you go.  IEEE / APA style is not required here.  Links and what they covered (why you referenced them) is sufficient.

## Command line git

For each `git` command, include a brief definition of **what it does and a sample of how to use it**. 

`status` has a sample of what a well done entry looks like.

Some bullets will include an additional note to include in your guide additional information OR elements that will be checked in your repository - these are the **DEMONSTRATE** notes - the graders will be checking your repository contains these things as additional proof that you have been practicing your git / GitHub knowledge.

Entries that are currently crossed out we will get to later in the course.  You are welcome to update your guide at later points in the course and add details.

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- log
- clone
- remote
- add
- rm
  - separately note how to remove from tracking versus fully remove a file from teh repository and working directory
- commit
  - **DEMONSTRATE** Your GitHub repo should have a commit history of more than one.  Commit messages should state changes at points in time
- push
- pull
- branch
  - **DEMONSTRATE** Your GitHub repo should have more than the `main` branch.  We can switch to the other branch and see content that may not be synced to `main`
- checkout
- fetch
- merge
  - **DEMONSTRATE** Your commit history should reflect a point where a merge was made from a different branch. Make sure the commit message contains some indication that the merge happened in the given commit
- init
  - separately note how to initializing and existing folder versus create a bare repository

## git files & folders

Provide descriptions of expected contents and what these are used for

- .git folder
  - explain the overall purpose of the folder and an overview of the purpose each item in the folder's contents
- .gitignore file
  - **DEMONSTRATE** Your GitHub repo should contain a `.gitignore` file that shows you are ignoring a set of files (or a folder) to prevent accidentally tracking them

## Command Line Docker

For each `docker` command, include a brief definition of **what it does AND a sample of how to use it**. 

- ps
  - include active and ability to view all
- images
- run
  - include the following flags: `-it`, `-p`, `--name`
- start
- stop
- exec
- import
- export
- kill
- rm
  - include removing a container versus removing an image

## SSH

Provide basic how-to-use guides.  This should be short and sweet so that you can refer to it as a quick guide.

- Setting up SSH authentication to GitHub repositories
- Setting up SSH authentication and using SSH to connect to an AWS instance
- Using the `config` file in the `.ssh` folder

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBUSERNAME/tree/main/git-guide

## Rubric

[Link to Rubric - TODO - NEEDS UPDATED FOR P0 FALL 2025](Rubric.md)
