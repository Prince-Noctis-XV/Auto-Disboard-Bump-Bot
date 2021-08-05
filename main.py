#import modules

print('[INFO] Importing MODULES')
import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import os
import time
import datetime

time.sleep(0.5) 


print('[INFO] Loading DATA')
with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]
    prefix = info["prefix"]



time.sleep(0.5) 

print('[INFO] LOADING BOT')
client = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)


@client.command(pass_context=True)
async def start(ctx):
  await ctx.message.delete()
  msg = await ctx.send('Auto Bump is Now **enabled.**')
  time.sleep(3)
  await msg.delete()
  global bump
  bump = True
  while bump:
      await ctx.send('!d bump')
      time.sleep(7200) #waits for 2 hours before sending it again.



@client.command()
async def stop(ctx):
  await ctx.message.delete()
  msg = await ctx.send('Auto Bump is Now **disabled.**')
  time.sleep(3)
  await msg.delete()
  global bump
  bump = False


time.sleep(0.5) 


print('[INFO] LOADING EVENTS')
@client.event
async def on_ready():
    activity = discord.Game(name="discord.gg/devscafe", type=4)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("[CONNECTED]")
   
time.sleep(0.5) 


print('[INFO] CONNECTING TO API')

client.run(token, bot=False)
