# Project 1

## Objectives:

- Protect files with secret information (in this case, an API key)
- Deploy a project using basic tools (GitHub & git)
- Build projects locally, then deploy them to your AWS instance
- Explore long term solutions to serving content that don't involve being connected to the terminal 24/7

## The Story

A developer is handing a project off to you for deployment. He has left you [documentation](https://realpython.com/how-to-make-a-discord-bot-python/) of how it works, the [core code](bot.py), and some changes to make before the project goes live.

Your job is to put the code into your repository (in GitHub classrooms) in a folder named `Discord-Bot`. Read through the documentation and figure out:

- how to generate an API key from Discord
- where to store the API key for the project to run
- keep the API key / secret information off GitHub
  - If you mess up, you'll need to create a new Discord API key, then tread carefully
  - See [Extra Info](#Extra-Info) for instructions on removal a file from tracking on GitHub
- install the python packages needed to run the project
  Run the project locally (your system, perhaps), first. Next, clone it (your GitHub classrooms repo) to your AWS instance and run the project from there.

For the changes, you'll be customizing the bot to output your set of messages when a command of your choice is written on your Discord server. To do this, you are going to create a `branch`, make your changes, test them, and then `merge` your changes with `main`

## Part 1 - Discord Bot Setup

1. Create a folder in your repository called `Discord-Bot`
2. Get the core code from [bot.py](bot.py) and copy / paste in into a `.py` file in your repo

- Don't go getting exctied and making modifications YET - you'll be needing to put changes on a `branch`

3. [Follow this guide](https://realpython.com/how-to-make-a-discord-bot-python/) to create a Discord bot in a Discord server you control.

- This documentation covers a lot, including:
  - Setup in the [Discord Developer Portal](https://discord.com/developers/applications) & create a key
  - The special name and file your key will go in (hint: it's a `.env`)
  - The python libraries that you need to add / install
  - How the code is working (because it is fun to look at, and the code itself is not heavily commented)

## Part 2 - Discord Bot Modifications

1. Clone your repo and run your code on the AWS instance.

2. Create a `branch` and make one of the modifications to the code listed below:

- outputs quotes based on a command of your choice
  - note that this _must_ be a different command and set of quotes from the demo
- outputs pictures based on a command of your choice
  - for an example, see `!corgme` in the Department server under Discussion. Please spam #cute-pets only
- Note: you are allowed to both, or pay around beyond just these, but at minimum one of these

3. Test your changes while on the `branch`. When your changes are tested and working, `merge` your `branch` changes with `main`

## Part 3 - R&D (Research & Documentation)

- In `Discord-Bot` folder, add a `README.md` file. Document the following:
  - Setup
    - how to get an API token
    - where to put it to work with the code
    - dependencies (what packages need to be installed to run the code)
  - Usage
    - with your changes to the code in place, describe
    - what commands you can type in your Discord server
    - what response this will provide (from your bot)
  - Research
    - you may have realized that it is lame that it only runs when you run the program.
    - In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.
    - Research some possible solutions that would solve this, and discuss why you think it would work.

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project1

## Rubric

[Link to Rubric](Rubric.md)

## Extra Info

### Create a Discord server

You are welcome to use any Discord server you are an admin of. Otherwise you can create a new server:

- Open Discord
- In your list of servers (those icons on the sidebar), click the "+" button to "Add a server"
- Click "Create My Own", then "For me and my friends"
- Give your server a name

### Get a file off `git` / GitHub tracking

Mistakes happen. If you made your API key public (up to GitHub), Discord killed it. Make a new key in the Discord Developer Portal, eat some ice cream (as needed), and deal with untracking a tracked file, below.

- The command you need is `git rm --cached filename`
- Check your `git status` output.
- Make sure you add it to `.gitignore` to prevent this in the future
- `push` your changes to GitHub - you should see the file disappear

Resources:

- [How to remove a file from git tracking](https://www.codegrepper.com/code-examples/shell/how+to+remove+a+file+from+git+tracking)
- [git rm documentation](https://git-scm.com/docs/git-rm)
