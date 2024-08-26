# git & bash 101

The purpose of this first chunk is to refresh or learn 
- the essential set of bash commands
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
- [The Odin Project - Foundations of Command Line Basics](https://www.theodinproject.com/lessons/foundations-command-line-basics)
- [Oh My Bash!](https://github.com/ohmybash/oh-my-bash/tree/master)

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
- [Git How-To](https://githowto.com/) & it's companion, [Git Immersion - Ruby focused](https://gitimmersion.com/lab_01.html)
- [Git Essentials - Sankalp Swami](https://dev.to/sankalpswami1122/git-essentials-4kff)
- [DZone - Top 20 git commands with examples](https://dzone.com/articles/top-20-git-commands-with-examples)
- [learn git branching - interactive tutorial](https://learngitbranching.js.org/?locale=en_US)
- [Anatomy of a git commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html)
- [git commands you do not need](https://myme.no/posts/2023-01-22-git-commands-you-do-not-need.html)
- git-sim - neat tool to visualize your own commits
  - [dependencies](https://docs.manim.community/en/stable/installation/linux.html)
  - [git-sim github repo](https://github.com/initialcommit-com/git-sim)
  - [blog on git-sim](https://initialcommit.com/blog/git-sim)
- [Oh My Git!](https://ohmygit.org/)
- [Git Murder Mystery](https://github.com/nivbend/gitstery)
- Understanding git in the weeds:
  - [The Pragmatic Git - How Does Git Store Files?](https://blog.git-init.com/how-does-git-store-files/)
  - [How to Dev - How git Stores Data](https://how-to.dev/how-git-stores-data)
  - [Thought RAM - The anatomy of a Git commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html)

## GitHub Essentials

- What is GitHub, at it's core?
- How does cloning use ssh?
- How does GitHub host repositories?
- What are Pull Requests and when to use them?
- What are Issues?
- What are Actions?
  - Note: this may not be covered in detail until later in the course
