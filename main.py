import os

import discord
from discord import app_commands
from discord.ext import tasks


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync()

@tree.command(name="version",description="URLを標準します")
async def cmd_version(ctx:discord.Interaction):
    msg="URLを標準しました(何もしていない)"
    await ctx.response.send_message(msg)

client.run(os.environ["DISCORD_TOKEN"])
