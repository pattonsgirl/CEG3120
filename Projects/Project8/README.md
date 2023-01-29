# Project 1

## Objectives:

- Protect files with secret information (in this case, an API token for a Discord bot)
- Deploy a project using basic tools (GitHub & git)
- Build projects locally, then deploy them to your AWS instance
- Explore long term solutions to serving content that do not involve being connected to the terminal 24/7

## Updates:

Package version headaches are now part of this project's scope.  Here are notes to keep in mind:
- To roll between versions of discord.py
  - `pip3 install -U discord.py==1.7.3` - this gets the version that works with the Discord API v9 (the one that works with bot.py)
  - `pip3 install -U discord.py==2.0.1` - this gets the version that works with Discord API v10, the one that needs bots to have intents.
  - 2.0.1 requires a rewrite to the code - [intentsbot.py](intentsbot.py)
- You can check which version you have installed with:
  - `pip3 show discord.py`

## The Story

A developer is handing a project off to you for deployment.  The project is a Discord Bot that he wrote.  The boss liked it, so now you need to deploy it on the company Discord server.  
The developer has left you [documentation](https://realpython.com/how-to-make-a-discord-bot-python/) of how to setup a Discord Bot and how the code works, the [core code](bot.py), and some changes to make before the project goes live.

Your job is to put the project into your repository (`WSU-kduncan/ceg3120-pattonsgirl-3`) in a folder named `Discord-Bot`. Read through the [documentation](https://realpython.com/how-to-make-a-discord-bot-python/) and figure out:

- how to generate an API token for your Bot from Discord
- where to store the API token for the project to run
- how to use OAuth2 to add/authenticate your Bot with your server
- keep the API key / secret information off GitHub
  - If you mess up, you'll need to create a new Discord API token, then tread carefully
  - See [Extra Info](#Extra-Info) for instructions on removal a file from tracking on GitHub
- configure your local environment to run the project (and later do the same on your AWS instance)
- change the bot to respond to prompts using a set of quotes of your choice
  - your changes will first be tested in a `branch`
  - once tested, your changes can then be merged with `main`

## Part 1 - Discord Bot Setup

**NOTE** You do need a Discord account with 2FA (Two factor authentication) enabled with either Authy OR Google Autheniticator. [Discord has 2FA setup instructions](https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication).  Any time you are prompted for a `6 digit authentication code`, it is a reference to the code displayed in the authenticator app.

1. Create a folder in your repository called `Discord-Bot`
2. Get the core code from [bot.py](bot.py) and copy / paste in into a `.py` file in your repo
  - Don't go getting exctied and making modifications YET - you'll be needing to put changes on a `branch`

3. [Follow this guide](https://realpython.com/how-to-make-a-discord-bot-python/) to create a Discord bot in a Discord server you control.
  - This documentation covers a lot, including:
    - Setup in the [Discord Developer Portal](https://discord.com/developers/applications) & create a key
    - The special name and file your key will go in (hint: it's a `.env`)
    - The python libraries that you need to add / install
    - How the code is working to make API calls to Discord (because it is fun to look at, and the code itself is not heavily commented)
4. Test that your bot, when running locally, can connect to your Discord server and responds to messages if they contain the right keyword

## Part 2 - Discord Bot Modifications

1. Clone your repo (which should include the Discord bot project) and run your code on the AWS instance.

2. Create a `branch` and make one of the modifications to the code listed below:

  - outputs quotes based on a command of your choice
    - note that this _must_ be a different command and set of quotes from the demo
  - outputs pictures based on a command of your choice
    - for an example, see `!corgme` in the Department server under Discussion. Please spam #cute-pets only
  - Note: you are allowed to both, or pay around beyond just these, but at minimum one of these

3. Test your changes while on the `branch`. When your changes are tested and working, `merge` your `branch` changes with `main`

## Part 3 - R&D (Research & Documentation)

1. In `Discord-Bot` folder, add a `README.md` file. Document the following:
  - Setup
    - dependencies (what packages need to be installed to run the project)
    - how to get an API token
    - where to put it to work with the code
  - Usage
    - with your changes to the code in place, describe
      - what commands you can type in your Discord server
      - what response this will provide (from your bot)
    - screenshots are welcome here
  - Research
    - you may have realized that it is lame that the bot only runs when you run the program - it turns off if you disconnect or need to switch tasks.
    - In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.
    - **Research** some possible solutions that would solve this, and discuss why you think it would work.
2. Check out the [Rubric](Rubric.md) to make sure you hit all elements

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Discord-Bot

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

## Additional Project Resources
- [Priveleged intents](https://discordpy.readthedocs.io/en/stable/intents.html)
- [Creating a bot account](https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro)
  - Note, this does not mention intent granting, may need to "enable" Message Intent for bot
- [Quickstart of chat bot](https://discordpy.readthedocs.io/en/stable/quickstart.html)
- [More examples of message content usage](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.content)
