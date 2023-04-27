import discord
import random

from discord.ext import commands
from discord.ext.commands import guild_only , has_guild_permissions

class Fun(commands.Cog):
    def __init__(self, Fireside):
        self.Fireside = Fireside

    @commands.command()
    async def gayrate(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = 0xffff00,
            title = "Gay Rating!"
        )
        embed.add_field(name = "" , value = f"🌈 <@{member.id}> is {random.randint(1 , 100)}% gay!" , inline = True)
        await ctx.reply(embed = embed)

    @commands.command()
    async def smartrate(self , ctx , member : discord.Member):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = 0xffff00,
            title = "Smart Rating!"
        )
        embed.add_field(name = "" , value = f"🤔 <@{member.id}> is {random.randint(1 , 100)}% smart!" , inline = True)
        await ctx.reply(embed = embed)

    @commands.command()
    async def kinkyrate(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = 0xffff00,
            title = "Kinky Rating!"
        )
        embed.add_field(name = "" , value = f"⛓️ <@{member.id}> is {random.randint(1 , 100)}% kinky!" , inline = True)
        await ctx.reply(embed = embed)

    @commands.command()
    async def cockrate(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = 0xffff00,
            title = "Cock Rating!"
        )
        embed.add_field(name = "" , value = f"🍆 <@{member.id}>'s cock is a **{random.randint(1 , 10)}/10** at a length of **{random.randint(1 , 32)}** inches!" , inline = True)
        await ctx.reply(embed = embed)

    @commands.command()
    async def coinflip(self , ctx):
        List = ["Heads" , "Tails"]
        embed = discord.Embed(
            colour = 0xffff00,
            title = "Coin Flip!"
        )
        embed.add_field(name = "" , value = f"🪙 <@{ctx.author.id}> landed **{random.choice(List)}**!" , inline = True)
        await ctx.reply(embed = embed)

    @commands.command(aliases=["rr"])
    async def russianroulette(self, ctx, * member: discord.Member):
        if len(member) < 2:
            embed = discord.Embed(
                colour = 0xFF9494,
                title = "More users required!"
            )
            embed.add_field(name = "", value="❌ Not enough users were mentioned, mention 2 or users!", inline=True)
            await ctx.reply(embed = embed)
            return
        else:
            winner = random.choice([m.id for m in member])
            embed = discord.Embed(
                colour = 0xffff00,
                title = "Russian Roulette!"
            )
            embed.add_field(name = "", value = f"🤯 <@{winner}> has won this round! The other {len(member)-1} people died!", inline=True)
            await ctx.reply(embed = embed)

async def setup(Fireside):
    await Fireside.add_cog(Fun(Fireside))
