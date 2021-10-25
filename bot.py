#AnnieRecs bot.py file
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
load_dotenv()

#Grabs hidden token key from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

#Connects a bot to the guild
bot = commands.Bot(command_prefix='!')

#Function of !rec command
@bot.command(name='rec', help='Generates the name of a random anime reccomendation.')
async def rdm_anime_rec(ctx):
    URL = "https://api.jikan.moe/v4/random/anime" #jikan API, pulls from MAL
    result = requests.get(URL)
    
    rating = result.json()['data']['score']
    episode_count = result.json()['data']['episodes']
    synopsis = result.json()['data']['synopsis']

    #If connection is good...
    if result.status_code == 200:
        await ctx.send(result.json()['data']['title'])
        if rating != None:
            await ctx.send("\n **Rating:** ")
            await ctx.send(result.json()['data']['score'])
        if episode_count != None:
            await ctx.send("\n **Episodes:** ")
            await ctx.send(result.json()['data']['episodes'])
        if synopsis != None:
            await ctx.send("\n **Synopsis:** ")
            await ctx.send(result.json()['data']['synopsis'])
    else:
        await ctx.send(f"API Fetch encountered error {result.status_code}")
    
#Calls uptime bot
keep_alive()
bot.run(TOKEN)



