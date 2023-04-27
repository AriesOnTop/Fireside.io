import discord
import time

from colorama import Fore
from discord.ext import commands

class onReady(commands.Cog):

    def __init__(self , Fireside):

        self.Fireside = Fireside

    @commands.Cog.listener()
    async def on_ready(self):

        Time = time.localtime()

        currentTime = time.strftime("%H:%M:%S" , Time)
        
        print(Fore.GREEN + f"Fireside is online | Time -> {currentTime}")

        await self.Fireside.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name=("https://ariez.xyz")))

async def setup(Fireside):

    await Fireside.add_cog(onReady(Fireside))