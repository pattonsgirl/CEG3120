# Project 1 - Basics Guide

**Due:** See Pilot, 11:59 PM. Late policy: 2-hour grace period, then -10% per day for up to 3 days. Work committed after that is not graded.

## Where your work goes

In your **basics** course repository (`ceg3120-basics-lastname-f26`) - not a personal repository - create a folder named exactly `basics-guide` containing a file named exactly `README.md`. (Not `basicsguide/`, not the repository's root `README.md`, not `Project1.md`.)

In this file you will be creating your own documentation on the commands & tasks you will use repetitively in this course. Write it for yourself, in your own words - this is a reference you'll use all semester.

## Formatting

This document should use markdown for formatting in a way that is clean and easy to read on GitHub. If you would prefer tables, you can make tables in markdown. [markdownguide.org](https://www.markdownguide.org/) has quick references to anything you'd like to do.

- Use headings for each section, and lists for each command.
- Put commands in code formatting - inline (`` `git status` ``) or in fenced code blocks (three backticks on their own line before and after). Don't write commands as headings.
- Close everything you open: every `**` and every ` ``` ` fence needs a matching close.
- Use markdown, not HTML lists (`<ul>`, `<li>`) - markdown inside HTML doesn't render.
- After you push, open your guide on GitHub and confirm it renders the way you expect.

Poor formatting is up to a 10% deduction, scaled by severity - 10% if the guide is illegible (plain text with no structure).

**Do not leave assignment text in your guide** - the instructions, the `DEMONSTRATE` notes, or the Submission / Rubric sections. The rubric is a checklist for grading, not a template to fill out; work from these instructions. Leaving task text in is a 5% formatting deduction.

## Resources

List the resources and references you used in a `Resources` section at the end of your guide (or cite them as you go). IEEE / APA style is not required here. Links and what they covered (why you referenced them) is sufficient.

- If you used an AI tool, name it and say what you asked it and how it helped.
- No Resources section / no sources cited anywhere is a 10% deduction. A partial Resources section (e.g. only an AI-use note, with sources missing for the rest) is a 5% deduction.

## Command line git

For each `git` command, include:
- a brief definition of **what it does**, in your own words
- a **sample of how to use it, with real arguments** - e.g. `git checkout my-branch`, not just `git checkout`. Commands that need arguments need an example that includes them.

`status` has a sample of what a well done entry looks like.

Some bullets will include an additional note to include in your guide additional information OR elements that will be checked in your repository - these are the **DEMONSTRATE** notes - the graders will be checking your repository contains these things as additional proof that you have been practicing your git / GitHub knowledge.

Entries that are currently crossed out we will get to later in the course.  You are welcome to update your guide at later points in the course and add details.

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder that are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- log
- clone
- remote
- add
- rm
  - separately explain **both**: how to stop tracking a file but keep it in your working directory (`--cached`), **and** how to remove a file from both the repository and your working directory
- commit
  - **DEMONSTRATE** Your GitHub repo should have a commit history of more than one commit, with messages that state the change you made at that point in time (e.g. "Add docker run and exec entries"). GitHub's default messages ("Update README.md") don't describe your change and earn half credit.
- push
- pull
- branch
  - **DEMONSTRATE** Your GitHub repo should have more than the `main` branch.  We can switch to the other branch and see content that may not be synced to `main`. **Keep the branch** on GitHub after you merge it.
- checkout
- fetch
- merge
  - **DEMONSTRATE** Your commit history should contain a real **merge commit** from a different branch. A fast-forward merge does not create one - use `git merge --no-ff <branch>` or merge a pull request on GitHub, and check `git log --graph` to see it. A normal commit with "merge" in its message does not count.
- init
  - separately explain **both**: initializing an existing folder as a repository **and** creating a bare repository (`--bare`) - and what a bare repository is used for

## git files & folders

Provide descriptions of expected contents and what these are used for

- .git folder
  - explain the overall purpose of the folder and an overview of the purpose of each item in the folder's contents
- .gitignore file
  - explain its purpose and **where it must be located** to apply to the whole repository
  - **DEMONSTRATE** Your GitHub repo should contain a `.gitignore` file **in the repository's root folder**, named exactly `.gitignore`, that ignores a set of files (or a folder) to prevent accidentally tracking them.
    - A `.gitignore` in a subfolder only applies to that subfolder.
    - `.gitignore` doesn't affect files git already tracks - add a pattern *before* committing the file, or untrack it with `git rm --cached <file>`.
    - Test it: create a file that matches your pattern and confirm `git status` doesn't list it.

## Command Line Docker

For each `docker` command, include a brief definition of **what it does AND a sample of how to use it, with real arguments** (a container or image name, a port, etc.). Use professional names in your examples.

- ps
  - include viewing active containers **and** viewing all containers (`-a`)
- images
- run
  - include the following flags: `-it`, `-p`, `--name`
- start
- stop
- exec
- attach
- import
- export
  - note what is exported: a **container's** filesystem (not an image)
- inspect
- logs
- kill
- rm
  - include removing a container (`docker rm`) versus removing an image (`docker rmi`)

## SSH

Provide basic how-to-use guides.  This should be short and sweet so that you can refer to it as a quick guide - but complete enough that following it actually works. Write out each command you would run.

- Setting up SSH authentication to GitHub repositories
  - creating a key pair (`ssh-keygen`)
  - where to add the public key on GitHub (Settings → SSH and GPG keys)
  - where to find a repository's SSH clone URL (the **Code** button → **SSH** tab) and a sample `git clone` with it
- Setting up SSH authentication and using SSH to connect to an AWS instance
  - where to get the private key (e.g. Learner Lab → AWS Details)
  - the permissions the private key needs (`chmod 400` on Linux / macOS; note what Windows needs, if anything)
  - where to find the instance's public IP (instance details in the EC2 console)
  - a full `ssh` command with the key, user, and IP
- Using the `config` file in the `.ssh` folder
  - a sample config entry block (`Host`, `HostName`, `User`, `IdentityFile`)
  - the command to connect using the entry (`ssh <alias>`)

## Your work must be your own

Write your guide in your own words, cite what you used, and make sure your examples do what you say they do. Submissions that appear AI-generated, or that describe work not done, are held at 0 until you meet with the instructor.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-basics-lastname-f26

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-basics-lastname-f26/tree/main/basics-guide

## Rubric

[Link to Rubric](Rubric.md)
