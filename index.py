import asyncio
import discord
import os
import tracemalloc
import traceback
import yaml

with open("Configurements\Configs.yaml" , "r") as f:
    config = yaml.safe_load(f)

Token = config["Fireside_Configs"]["Token"]

tracemalloc.start()

from discord.ext import commands

Intents = discord.Intents().all()

Fireside = commands.Bot(command_prefix="f.", intents=Intents)

@Fireside.command()
async def eval(ctx, * , code):
    try:
        Result = await exec(f"```{code}```")
        await ctx.send(Result)
    except Exception as Except: await ctx.send(f"```{Except}```")
    

async def setup():
    async with Fireside:
        for Fireside_file in os.listdir("Events"):
            if Fireside_file.endswith(".py"):
                try:
                    Fireside_extension = Fireside_file[:-3]
                    await Fireside.load_extension(f"Events.{Fireside_extension}")
                except:
                    traceback.print_exc()

        for Fireside_file in os.listdir("Cogs"):
            if Fireside_file.endswith(".py"):
                try:
                    Fireside_extension = Fireside_file[:-3]
                    await Fireside.load_extension(f"Cogs.{Fireside_extension}")
                except:
                    traceback.print_exc()

        await Fireside.start(Token)

asyncio.run(setup())