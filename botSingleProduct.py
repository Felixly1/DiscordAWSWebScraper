from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import GetProductAvailability

url = "https://www.canadacomputers.com/en/powered-by-intel/266476/asrock-intel-arc-b580-steel-legend-12gb-gddr6-oc-battlemage-gpu-b580-sl-12go.html"

load_dotenv()
TOKEN: Final[str] = os.environ.get('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
USER_ID: Final[int] = os.environ.get('USER_ID')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    periodic_task.start() 
    
        
@bot.command()
async def checkSearchStock(ctx):
    if (output := GetProductAvailability.getInStockON(url)):
        await ctx.send(f'Listing In-Stock Intel b580: {output}')
    else:
        await ctx.send("No Intel b580 In-Stock at the moment")

@tasks.loop(seconds=10)
async def periodic_task():
    print("Task started")
    channel = bot.get_channel(CHANNEL_ID)
    print(channel)
    if channel:
        user_mention = f'<@{USER_ID}>'  # Replace USER_ID with your Discord user ID
        if (output := GetProductAvailability.getInStockON(url)):
            await channel.send(f'{user_mention} 🎉 Listing In-Stock Intel b580: 🎉{output}')
        else: 
            await channel.send(f'❌ No Intel B580 Currently In Stock')


bot.run(TOKEN)
