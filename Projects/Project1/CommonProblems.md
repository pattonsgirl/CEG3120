# Common error log for Project 1

```
File "path to bot", line 45, in <module>
.
.
.
TypeError: expected token to be str, received <class 'NoneType'> instead
```
- Meaning: Your token is not in a .env file or special characters are around token
- Fix 1: Your .env file with the token needs to be in the folder with your code.  The python-dotenv library is then used to load the token from the .env file so your program can use it.
- Fix 2: No special characters in token: `DISCORD_TOKEN=token_text` NOT `DISCORD_TOKEN={token_text}` or `DISCORD_TOKEN="token_text"`

```
Traceback (most recent call last):
  File "bot.py", line 4, in <module>
    import discord
ModuleNotFoundError: No module named 'discord'`
```
- Meaning: the module `discord` only exists if you installed `discord.py` with pip

```
pip cannot install discord.py 2.0.1
This is actually a giant angry message about what versions that version of pip does know about, and 2.0.1 is not one of them
```
- Meaning: pip needs updated, but this issue is a bit bigger.  You likely need a more recent version of python3 as well
- Fix: install python3.8 `sudo apt install python3.8`
  - update pip for python3.8 `python3.8 -m pip install --upgrade pip`
  - install discord.py v 2.0.1 `python3.8 -m pip install -U discord.py==2.0.1`
  - Run code in `python3.8` since it will refer to the correct pip libraries
- [Source for workaround](https://stackoverflow.com/questions/59997065/pip-python-normal-site-packages-is-not-writeable)
