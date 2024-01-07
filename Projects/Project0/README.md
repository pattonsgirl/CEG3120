# Project 0 - Basics Guide

In your repo for this course, create a folder named `basics-guide` with a file named `README.md`. 

In this file you will be creating your own documentation on the commands & tasks you will use repetitively in this course.

This document should markdown for formatting in a way that is clean for you.  If you would prefer tables, you can make tables in markdown.  [markdown.org](https://www.markdownguide.org/) has quick references to anything you'd like to do.

List resources and reference you used in the `Resources` section or by citing them as you go.  IEEE / APA style is not required here.  Links and what they covered (why you referenced them) is sufficient.

## Command line git

For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done entry looks like.  For some commands, we can visually demonstrate that you have played with them in order to brush up your skills.  For each topic that should be viewable in your repository, there will be a note added of what the demonstrated element will be that we are checking for.

Entries that are currently crossed out we will get to later in the course.  You are welcome to update your guide at later points in the course and add details.

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- log
- clone
- add
- rm
  - separately note how to remove from tracking versus fully remove a file from teh repository and working directory
- commit
  - **DEMONSTRATE** Your GitHub repo should have a commit history of more than one.  Commit messages should state changes at points in time
- push
- fetch
- merge
  - **DEMONSTRATE** A commit in your GitHub history should have a standard message that content was merged.  Sample:
    - `Merge branch 'main' of github.com:WSU-kduncan/ceg3120f23-pattonsgirl`
- pull
- branch
  - **DEMONSTRATE** Your GitHub repo should have more than the `main` branch.  We can switch to the other branch and see content that may not be synced to `main`
- tag
- checkout
- init
- remote

## git files & folders

Provide descriptions of expected contents and what these are used for

- .git folder
- .gitignore file
  - **DEMONSTRATE** Your GitHub repo should contain a `.gitignore` file that shows you are ignoring a set of files (or a folder) to prevent accidentally tracking them
- ~~.git/hooks~~

## GitHub

Provide basic how-to-use guides.  This should be short and sweet so that you can refer to it as a quick guide.

- Pull Requests
  - should include what it is & how to perform one
  - **DEMONSTRATE** Generate and complete a Pull Request in your repository in GitHub.  Pretend you are two people.
- ~~Actions~~
- ~~Releases~~

## SSH

Provide basic how-to-use guides.  This should be short and sweet so that you can refer to it as a quick guide.

- SSH authentication to repositories
- SSH authentication to an AWS instance
- Using the `config` file in the `.ssh` folder

## Resources
Other resources are welcome, just cite them (you can do lazy citations here, or use markdown to make links throughout your guide).  This one is to an online book and covers anything you'd like to do with `git`

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120f24-YOURGITHUBUSERNAME/tree/main/git-guide

## Rubric

[Link to Rubric](Rubric.md)
