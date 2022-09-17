# Common error log for Project 1

## 1. Not finding TOKEN
```
File "path to bot", line 45, in <module>
.
.
.
TypeError: expected token to be str, received <class 'NoneType'> instead
```
- Meaning: Your token is not in a .env file or special characters are around token
- Fix 1: Your .env file with the token needs to be in the folder with your code.  The python-dotenv library is then used to load the token from the .env file so your program can use it.  The file can only be named `.env`
- Fix 2: No special characters in token: `DISCORD_TOKEN=token_text` NOT `DISCORD_TOKEN={token_text}` or `DISCORD_TOKEN="token_text"`

## 2. No module named ___
```
Traceback (most recent call last):
  File "bot.py", line 4, in <module>
    import discord
ModuleNotFoundError: No module named 'discord'`
```
- Meaning: the module `discord` only exists if you installed `discord.py` with pip

## 3. Intents & needing discord.py v 2.0.1
```
pip cannot install discord.py 2.0.1
This is actually a giant angry message about what versions that version of pip does know about, and 2.0.1 is not one of them
```
- Meaning: pip needs updated, but this issue is a bit bigger.  You likely need a more recent version of python3 as well
- Fix: install python3.8 `sudo apt install python3.8`
  - update pip for python3.8 `python3.8 -m pip install --upgrade pip`
  - install discord.py v 2.0.1 `python3.8 -m pip install -U discord.py==2.0.1`
    - Reminder to also get the other library ;)
  - Run code in `python3.8` since it will refer to the correct pip libraries
- [Source for workaround](https://stackoverflow.com/questions/59997065/pip-python-normal-site-packages-is-not-writeable)

## 4. Privileged Intents Required
```
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.
```
- Back where you create your token, check if "Message Content Intent" is enabled (blue light is on).  
  - A fresh token may not be be required.

## 5. SSL Cert for discord.com not valid (seen on Mac)
```
ClientConnectorCertificateError(aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host discordapp.com:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1108)')]
```
- Need to manually install the cerificate?  Student solved, but we lacking good fix it documentation
- https://github.com/Rapptz/discord.py/issues/4159#issuecomment-640107584
- If Mac, need to `Install certificates.command` https://stackoverflow.com/questions/62108183/discord-py-bot-dont-have-certificate
  - recommended to just search for the file in the file explorer

# Other
There is some mad hatter YouTuber who gives "instructions" on how to get your bot token, and uses Chrome inspection tools to do it.  This is not how to generate a bot token.  This may get the token associated with **you** being signed in to Discord, as in your person's authorization token.  The RealPython page contains instructions for generating a bot token via discord.com/developers/applications


