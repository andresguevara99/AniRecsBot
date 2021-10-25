# AniRecsBot
Anime Recommendations Bot for Discord

## Background
My friends on discord were having trouble finding new anime to watch so I coded a Discord bot to give them anime reccomendations

The Bot utilizes the [discord.py] (https://discordpy.readthedocs.io/en/stable/#) Discord pythonic API wrapper and the public [jikan](https://jikan.docs.apiary.io/#introduction/information) API that is used to access a massive dataset of old and new anime from MyAnimeList

### Installation
This bot utilizes a **Replit** HTTP web server (using **Flask**) with an uptime bot from [uptimerobot](https://uptimerobot.com/) in order to continously run in the background 

If you want to do it this way, and not pay for your own web server follow the directions:

After downloading the code you're going to want to go to [discord dev](https://discord.com/developers/docs/intro) and register your own bot. Once you do this you can get your own token which can then be stored as the variable `DISCORD_TOKEN` in an .env file

Secondly, within the repl workspace you want to run your code and retrieve the flask URL. This URL will be the one you ping on **uptimerobot** 

Once this is setup, and you can see the individual pings from *uptimerobot* you want to add your bot to a discord guild within the developer portal

### How to use the bot
Currently, the only command the bot has is `!rec` which will return the name, rating (out of 10), episode count, and synopsis (if available) of a randomly chosen anime.


More features to come!

![anirecsbot](https://github.com/andresguevara99/AniRecsBot/tree/master/AniRecs.png "Picture of !rec functionality")
