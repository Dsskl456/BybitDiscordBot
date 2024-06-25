from discord.ext import commands, tasks
import Bybitcollect
import discord
import asyncio

CHANNEL_ID = 1254509633373081671
BOT_TOKEN = ""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello, im ready to work!")
    chceck_rsi.start()

@tasks.loop(seconds=1)
async def chceck_rsi():
    rsi = Bybitcollect.calculate_rsi()
    if(rsi > 70 or rsi < 30):
        text = "SOL/USDT RSI = " + str(rsi)
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(text)
        await asyncio.sleep(3600)

bot.run(BOT_TOKEN)