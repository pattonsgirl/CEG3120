Fall 2021 game plan

Server setup:

    Project 1:
    Use linux system on AWS for hosting git repositories.  Share ssh keys appropriately so authentication occurs over SSH
        Repository URL should be in format git@server_name:/username/repository
        Files to investigate:
        /etc/hosts
        ~/.ssh/config
        ~/.ssh/authorized_keys
    Write a guide on how to create a git server
        Include how to set up a new repository
    Write a guide guide that covers:
        clone
        init
        Flag to create a bare repository and definition of a bare repository
        add
        commit
        push
        pull

APIs and protecting secrets

    Project 2: 
    Work with .gitignore
    Set up an API key, create basic bot to confirm working connection
    Guide: (https://realpython.com/how-to-make-a-discord-bot-python/)
        Bot challenge: create something unique
    Create a branch
    Customize the bot to output you own lookup table of messages
    Merge the branch with main
    Step one - have it run on your machine
    Step two - get it to an machine on AWS
    Step three - research methods that would let this run after you disconnect

Intro to setting up the cloud

    Project 3:
    Manually create a VPC, subnet, and security group.  Add an EC2 instance to the VPC with an Ubuntu AMI.
    Create a cloud formation template that automates this process.
        Note: use AMI in template, use specific port list, open to public & "home" ip

Deploying a Flask App

    https://flask.palletsprojects.com/en/2.0.x/server/
    https://flask.palletsprojects.com/en/2.0.x/deploying/
    https://flask.palletsprojects.com/en/2.0.x/deploying/mod_wsgi/
    https://newbedev.com/flask-at-first-run-do-not-use-the-development-server-in-a-production-environment


Playing with Load Balancing & deploying config files
    Project 4:
    Cloud formation w/ 3 servers
        1 proxy + install haproxy
        2 webservers + install apache2
    Require use of HTTPS this term?
    Add config files to git repo, have CF insert them into respective servers

Continuous integration / deployment
    Project 5:
    (In class play with hooks - maybe just a quiz?)
    Use webhooks to let GitHub notify servers there's been a change (use webpage idea to play with this for now?)
    https://dzone.com/articles/github-continuous-deployment-to-a-raspberry-pi

    Project 6:
    Containerize Discord bot - trick: figure out how to protect and deploy API key

https://cli.github.com/
Maybe instead of AWS CLI?

adding text
Discord bot (https://realpython.com/how-to-make-a-discord-bot-python/):

    Project 1:
    Set up an API key, create basic bot to confirm working connection
    Bot challenge: create something unique
        Objective: learn to use an example to craft your own flair

    Project ?:
    Branch to make additions to python code
        Create an error handler, send log somewhere?

Cloud Knowledge base:

    Project 2:
    Manually create a VPC, subnet, and security group.  Add an EC2 instance to the VPC with an Ubuntu AMI.
    Create a cloud formation that automates this process.
        Note: use AMI in template, use specific port list, open to public & "home" ip

    Project 3 (MAKE REPO PUBLIC):
    Cloud formation w/ 3 servers
        1 proxy + install haproxy
        2 webservers + install apache2
    Add config files to git repo, have CF insert them into respective servers

Continuous Integration

    Project 4 (add in to cloud kb):
    Use original linux system on AWS to host website git repo.
    Write a hook that updates to web servers in project 3 when push is made to main branch
        Check security groups, update ssh permissions to allow linux system connection
        Investigate `scp` or `rsync`
