
import discord, asyncio, aiohttp, json
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), case_insensitive=True)

@bot.event
async def on_ready():
    print("=========\nReady for use!\n=========\n")

@bot.event
async def on_message(message):
    print(message)

    report = {}
    report["value1"] = f"New message"
    report["value2"] = f"please check discord"
    async with aiohttp.ClientSession() as session:
        await session.post("https://maker.ifttt.com/trigger/" + config["eventName"] +"/with/key/" + config["IFTTTkey"], data=report)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"**:no_entry: {error}**")

if __name__ == '__main__':

    bot.run(config["discordToken"])
