import asyncio
import json
import time
import discord

from discord.ext import commands
from discord.ext.commands import guild_only , has_guild_permissions

class Moderation(commands.Cog):
    def __init__(self, Fireside):
               
        self.Fireside = Fireside

    @guild_only()
    @has_guild_permissions(kick_members = True)
    @commands.command()
    async def kick(self , ctx , member : discord.Member , * , reason = None):
        for role in member.roles:
            x = role.id
        if reason is None:
            reason = "No reason was provided."
        Time = time.localtime()
        currentTime = time.strftime("%H:%M:%S" , Time)
        embed = discord.Embed(
            colour = member.colour,
            title = f"{member.name} was kicked from {member.guild.name}!"
        )
        embed.set_thumbnail(url = member.avatar)
        embed.set_footer(text = f"Offenders ID: {member.id} | Time: {currentTime}")
        embed.add_field(name = "Kicked By:" , value = f"<@{ctx.author.id}>" , inline = True)
        embed.add_field(name = "Reason:" , value = f"***{reason}***" , inline = False)
        embed.add_field(name = "Highest Role:" , value = f"<@&{x}>" , inline = False)
        await ctx.reply(embed = embed)
        await member.kick(reason = reason)

    @guild_only()
    @has_guild_permissions(ban_members = True)
    @commands.command()
    async def ban(self , ctx , member : discord.Member , * , reason = None):
        for role in member.roles:
            x = role.id
        if reason is None:
            reason = "No reason was provided."
        Time = time.localtime()
        currentTime = time.strftime("%H:%M:%S" , Time)
        embed = discord.Embed(
            colour = member.colour,
            title = f"{member.name} was banned from {member.guild.name}!"
        )
        embed.set_thumbnail(url = member.avatar)
        embed.set_footer(text = f"Offenders ID: {member.id} | Time: {currentTime}")
        embed.add_field(name = "Banned By:" , value = f"<@{ctx.author.id}>" , inline = True)
        embed.add_field(name = "Reason:" , value = f"***{reason}***" , inline = False)
        embed.add_field(name = "Highest Role:" , value = f"<@&{x}>" , inline = False)
        await ctx.reply(embed = embed)
        await member.ban(reason = reason)

    @guild_only()
    @has_guild_permissions(manage_channels = True)
    @commands.command(aliases = ["slow"])
    async def slowmode(self , ctx , slowtime : int):
        await ctx.channel.edit(slowmode_delay = slowtime)
        embed = discord.Embed(
            colour = 0x4BB543
        )
        embed.add_field(name = "" , value = f"✅ ***<#{ctx.channel.id}> now has a slowmode of 1 message / {slowtime} seconds.***" , inline = True)
        await ctx.reply(embed = embed)

    @guild_only()
    @has_guild_permissions(kick_members = True)
    @commands.command()
    async def mute(self , ctx , member : discord.Member , duration = None , reason = None):
        if reason is None:
            reason = "No reason given."
        seconds = 0
        if duration is None:
            duration = float("inf")
        elif duration.endswith("s"):
            seconds = int(duration[:-1])
        elif duration.endswith("m"):
            seconds = int(duration[:-1]) * 60
        elif duration.endswith("h"):
            seconds = int(duration[:-1]) * 60 * 60
        elif duration.endswith("d"):
            seconds = int(duration[:-1]) * 60 * 60 * 24
        else:
            embed = discord.Embed(
                colour = 0xFF9494
            )
            embed.add_field(name = "Invalid duration format" , value = "❌ Accepted Values: ***s (seconds)*** , ***m (minutes)*** , ***h (hours)*** or ***d (days)***" , inline = True)
            await ctx.reply(embed = embed)
            return
        muteRole = discord.utils.get(ctx.guild.roles, name='muted')
        if muteRole is None:
            perms = discord.Permissions(send_messages=False, add_reactions=False)
            muteRole = await ctx.guild.create_role(name='muted', permissions=perms)
            for channel in ctx.guild.channels:
                await channel.set_permissions(muteRole, send_messages=False)
        await member.add_roles(muteRole)
        embed = discord.Embed(
            colour = 0x4BB543
        )
        embed.add_field(name = "" , value = f"✅ ***{member.name}*** has been muted for ***{duration}***! Reason: {reason}" , inline = True)
        await ctx.reply(embed = embed)
        await asyncio.sleep(seconds)
        await member.remove_roles(muteRole)

    @guild_only()
    @has_guild_permissions(manage_messages = True)
    @commands.command()
    async def purge(self , ctx , messages : int):
        if messages > 100:
            embed = discord.Embed(
                colour = 0xFF9494
            )
            embed.add_field(name = "" , value = "❌ You cannot delete more than 100 messages at once!" , inline = True)
            await ctx.reply(embed = embed)
            return
        await ctx.channel.purge(limit = messages)
        embed = discord.Embed(
            colour = 0x4BB543,
        )
        embed.add_field(name = "" , value = f"✅ I have succcessfully deleted ***{messages}*** messages!" , inline = True)
        x = await ctx.send(embed = embed)
        time.selep(10)
        await x.delete()
        return

async def setup(Fireside):
    await Fireside.add_cog(Moderation(Fireside))