# git & bash 101

The purpose of this first chunk is to refresh or learn 
- the essential set of bash commmands
- how to use ssh and how SSH works
- setting up your first AWS environment for this course
- git: from commits to pulls and merges

In order to accomplish this, we are going to set up a server as a host for a git repository.  

## Setup AWS Starter Environment

- Check out [AWS Academy Instructions](../AWSAcademy.md) for how to create your first AWS stack and instructions on connecting to an instance.  
- Other notes: 
  - Click "Start Lab" at the beginning of each work session and "End Lab" to turn things off at the end of each work session.
  - The "light" indicator next to AWS tells you if your environment is on (green) or off (red).  It must be green to interact with your AWS account.
  - Environment will turn off after 4 hours.  Select "Start Lab" to reset timer any time within those 4 hours.
  - **Never click "Reset" unless instructed.**

## SSH Essentials

SSH protocol (aka. Secure Shell)
- secure remote login from one computer to another
- protects communications security and integrity with strong encryption

SSH key pairs
- cryptographic key pair 
- public key and private key
- configure the public key on a server to authorize access and grant anyone who has a copy of the private key access to the server

Connecting to a remote system with SSH (the rules)
- the user account on the system needs a public key in their authorized_keys file
- you need a private key paired to (don't love that wording) the public key
- `ssh -i privkey remoteuser@host`
  - lookup: 
    - `-i` flag for ssh
    - abosulute verus relative pathing and what should be used here

Important files:
- located in the user's `.ssh` folder
- `known_hosts`
- `authorized_keys`
- `config`
  - the config file allows proper setup of private keys, usernames, and system names (or IPs) 
  - [linuxize - the ssh config file](https://linuxize.com/post/using-the-ssh-config-file/)

Other resources:
- [ssh official - SSH Protocol](https://www.ssh.com/academy/ssh/protocol)
- [hostinger - how does SSH work](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)
- [redhat - basics of setting up SSH on client and server](https://www.redhat.com/sysadmin/access-remote-systems-ssh)

## Command Line Essentials

Remember for this course I recommend Windows users install WSL2 + Ubuntu, and use that as their shell throughout this course.  Mac and Linux (or Linux VM users) just need to find their Terminal programs.

Know how to:
- move around a file system
- create and edit files
- move files around
- check and change file / folder permissions

Resources:
- [Linux Journey - interactive practice](https://notes.siira.io/)
- [Mozilla - Command Line crash course](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)
- [The Obin Project - Foundations of Command LIne Basics](https://www.theodinproject.com/lessons/foundations-command-line-basics)

## git Essentials

Know how to:
- add public keys to your GitHub account
- clone your repository from GitHub
- add new files, make commits of work
- create branches & switch between them
- merge branch content (and close branches)
- push to your GitHub repository
- pull to synchronize work (and what pull is)
- tagging commits and pushing tags
  - Note: this may not be covered in detail until later in the course

Resources:
- [git official docs](https://git-scm.com/docs/gittutorial)
- [git - the simple guide](https://rogerdudler.github.io/git-guide/)
- [Git Essentials - Sankalp Swami](https://dev.to/sankalpswami1122/git-essentials-4kff)
- [learn git branching - interactive tutorial](https://learngitbranching.js.org/?locale=en_US)

## GitHub Essentials

- What is GitHub, at it's core?
- How does cloning use ssh?
- How does GitHub host repositories?
- What are Pull Requests and when to use them?
- What are Issues?
- What are Actions?
  - Note: this may not be covered in detail until later in the course
