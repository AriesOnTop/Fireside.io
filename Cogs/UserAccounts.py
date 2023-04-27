import discord
import json
import yaml

from discord.ext import commands

class UserAccounts(commands.Cog):
    def __init__(self, Fireside):
        self.Fireside = Fireside

    @commands.command()
    async def load(self , ctx):
        with open(r"userConfigs\Accounts.json" , "r") as f2:
            data = json.load(f2)
        await ctx.send(data)
    

    @commands.command()
    async def profile(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = member.colour,
            title = f"Profile Statistics:"
        )
        embed.set_author(name = member , icon_url = member.avatar)
        embed.set_footer(text = f"{member.name}'s ID: {member.id}")
        embed.set_thumbnail(url = member.avatar)
        embed.add_field(name = "Staff-Member?" , value = f"`{member}`" , inline =  True)
        embed.add_field(name = "VIP-Member?" , value = f"`{member}`" , inline =  False)
        await ctx.reply(embed = embed)
        with open("Configurements\Configs.yaml" , "r") as f1:
            checker = yaml.safe_load(f1)
        if member.id in checker["SETTINGS"]["ID_LIST"]["STAFF_MEMBER"]:
            staff_member = True
        if member.id in checker["SETTINGS"]["ID_LIST"]["VIP"]:
            vip_member = True
        with open("userConfigs\Accounts.json" , "r") as f2:
            data = json.load(f2)
        if str(member.id) in data:
            embed = discord.Embed(
                colour = member.colour,
                title = f"Profile Statistics:"
            )
            embed.set_author(name = member , icon_url = member.avatar)
            embed.set_footer(text = f"{member.name}'s ID: {member.id}")
            embed.set_thumbnail(url = member.avatar)
            embed.add_field(name = "Staff-Member?" , value = f"`{staff_member}`" , inline =  True)
            embed.add_field(name = "VIP-Member?" , value = f"`{vip_member}`" , inline =  False)
            await ctx.reply(embed = embed)
        else:
            with open("userConfigs\Accounts.json" , "r") as f3:
                json.load(f3)
            data[str(member.id)] = {}
            with open("userConfigs\Accounts.json" , "w") as f4:
                json.dump(data , f4 , indent = 4)
            embed = discord.Embed(
                colour = member.colour,
                title = f"Profile Statistics:"
            )
            embed.set_author(name = member , icon_url = member.avatar)
            embed.set_footer(text = f"{member.name}'s ID: {member.id}")
            embed.set_thumbnail(url = member.avatar)
            embed.add_field(name = "Staff-Member?" , value = f"`{staff_member}`" , inline =  True)
            embed.add_field(name = "VIP-Member?" , value = f"`{vip_member}`" , inline =  False)
            await ctx.reply(embed = embed)
            return

async def setup(Fireside):
    await Fireside.add_cog(UserAccounts(Fireside))
