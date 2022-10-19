from distutils.cmd import Command
import discord
import asyncio
import json
import os
import platform
import random
import sys
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context

from discord.ext import commands
from discord.utils import get

from discord import member




"""	
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents
Default Intents:
"""

intents = discord.Intents.default()

intents.bans = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
intents.guild_typing = True
intents.guilds = True
intents.integrations = True
intents.invites = True
intents.messages = True # `message_content` is required to get the content of the messages
intents.reactions = True
intents.typing = True
intents.voice_states = True
intents.webhooks = True


intents.members = True
intents.message_content = True
intents.presences = True


if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

bot = Bot(command_prefix=commands.when_mentioned_or(
    config["prefix"]), intents=intents, help_command=None)

bot.config = config


@bot.event
async def on_ready() -> None:
    """
    The code in this even is executed when the bot is ready
    """
    print(f"Logged in as {bot.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")




@bot.command(pass_context=True)
@commands.has_role("Academy Staff") 
async def passp1(ctx, user: discord.Member, reason):
    role = discord.utils.get(user.guild.roles, name="Phase 1 ✓")
    channel = bot.get_channel(1032275540004053062)
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.mention}, {user.mention} has been ranked to {role.name}.")
    await channel.send(f"{ctx.author.mention} has promoted {user.mention}. {reason}")
    await ctx.message.delete()


@bot.command(pass_context=True)
@commands.has_role("Academy Staff") 
async def passp2(ctx, user: discord.Member, reason):
    role = discord.utils.get(user.guild.roles, name="Phase 2 ✓")
    channel = bot.get_channel(1032275540004053062)
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.mention}, {user.mention} has been ranked to {role.name}.")
    await channel.send(f"{ctx.author.mention} has promoted {user.mention}. {reason}")
    await ctx.message.delete()

@bot.hybrid_command(pass_context=True)
@commands.has_role("RCD | High Command") 
async def promote(ctx, user: discord.Member, role: discord.Role, reason):
    logs = discord.utils.get(user.guild.channels, id="1032275540004053062")
    channel = bot.get_channel(1032275540004053062)
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.mention}, {user.mention} has been ranked to {role.name}.")
    await channel.send(f"{ctx.author.mention} has promoted {user.mention}. {reason}")
    await ctx.message.delete()



@bot.hybrid_command(pass_context=True)
@commands.has_role("RCD | High Command") 
async def induct(ctx, user: discord.Member):
    channel2 = bot.get_channel(1032275540004053062)
    role = discord.utils.get(user.guild.roles, name="In training")
    await user.add_roles(role)
    await user.send(f"Hola {user.mention}, I am from Realistic Communication Dispatch and I am here to inform you have moved on from filtering and is now inducted into our Dispatch Academy. I suggest you read <#1007596836040744990> for information on our course.")
    await channel2.send(f"{ctx.author.mention} has inducted {user.mention}.")
    await ctx.message.delete()






bot.run(config["token"])
