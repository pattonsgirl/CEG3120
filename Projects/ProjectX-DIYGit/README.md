# Project 1

## Objectives:

- Create a git server of your own on your AWS instance
- Understand the background actions involved with git
- Work more with ssh keys and understanding files for key based authentication
- Create documentation with markdown

## The Goal

Create your own git server from which you can create, clone, push, and pull repositories.  To drive the objectives home, you are going to make something that is organized like what you are used to on GitHub.  You will use the instance your spun up on AWS to create a host for repositories.

A successful project will be able to use:
```
git clone git@AWS_IP:project_creator/repo_name.git
```
- `AWS_IP` = the public IP address of your AWS instance
    - **NOTE:** `AWS_IP` can either be your IP to your AWS instance OR a `Host` name reference set up in `~/.ssh/config`
- `project_creator` = project creator is used organizationally to have repositories clustered with their project owners
- `repo_name` = the folder name of your repository that was initialized on the server

We can compare this to the URL GitHub provides when we clone with SSH authentication:
```
git@github.com:WSU-kduncan/ceg3120-pattonsgirl-1.git
```
- `git` - the username we are authenticating as
- `github.com` - the pretty name for GitHub.  This gets translated to an IP address by DNS (remember, we don't have DNS)
- `WSU-kduncan` - the project owner's name
- `ceg3120-pattonsgirl-1.git` - the project repository


## The Requirements

- Use your AWS instance to configure one or more git repositories
- Have it behave similar to GitHub, in that the URL format: `git@AWS_IP:project_creator/repo_name.git` works
    - **NOTE:** `Linux_AWS_IP` can either be your IP to your AWS instance OR a `Host` name reference set up in `~/.ssh/config`
- Setup SSH authentication to the `git` user on the AWS instance
- In the GitHub repo for the course, create a new folder called `Project1`.  
- In the folder, create a `README.md` file that provides documentation of:
    - Setup: how to initialize a repo and all other setup steps (users, permissions, keys)
    - Usage: how to clone, add, commit, and push from a given system to the repo hosted on the AWS instance
    - Proof: include screenshots of the repo 
        - existing on the AWS instance
        - being cloned to your local system

## Guided Questions

You don't need to answer these as part of your project.  They serve as hints to figure out the project.

1. On your AWS instance, create a new folder in the ubuntu user's `home` directory.  Write an SSH command that will connect you straight to that folder (without using `cd` once you are connected)
2. What user are you authenticating as?  Focus on what is before the @ symbol when you use `ssh` or `git clone`
3. The answer to number 2 also provides insight to what needs to happen with respect to SSH authentication.  Where does your public key need to be?
4. Investigate `git init --bare` versus `git init`
    - Look at the difference between the two after creating a repo and after a clone

## Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder.  Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project1