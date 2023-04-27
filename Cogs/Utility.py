import discord

from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, Fireside):
        self.Fireside = Fireside

    @commands.command(aliases = ["av"])
    async def avatar(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(
            colour = member.colour,
            title = f"{member.display_name}'s display avatar:"
        )
        embed.set_footer(text = f"{member.name}'s ID: {member.id}")
        embed.set_image(url = member.display_avatar)
        await ctx.reply(embed = embed)

    @commands.command(aliases = ["ui" , "whois"])
    async def userinfo(self , ctx , member : discord.Member = None):
        if member is None:
            member = ctx.author
        if member == member.guild.owner:
            is_Owner = True
        else:
            is_Owner = False
        if member.premium_since is not None:
            Boosting = True
        else:
            Boosting = False
        for role in member.roles:
            x = role.id
        
        ## PUBLIC FLAGS:

        if member.public_flags.active_developer == True:
            active_developer = True
        else:
            active_developer = False
        
        if member.public_flags.staff:
            staff_member = True
        else:
            staff_member = False

        if member.public_flags.bug_hunter:
            bug_hunter = True
        else:
            bug_hunter = False

        if member.public_flags.early_verified_bot_developer == True:
            EVBD = True
        else:
            EVBD = False

        if member.public_flags.verified_bot_developer == True:
            VBD = True
        else:
            VBD = False

        if member.public_flags.verified_bot == True:
            verified_bot = True
        else:
            verified_bot = False

        embed = discord.Embed(
            colour = member.colour,
            title = f"{member.display_name}'s information:"
        )
        embed.set_thumbnail(url = member.display_avatar)
        embed.set_author(name = member , icon_url= member.avatar)
        embed.set_footer(text = f"{member.display_name}'s ID: {member.id}")
        embed.add_field(name = "Username:" , value = f"`{member.name}`" , inline = True)
        embed.add_field(name = "Display Username:" , value = f"`{member.display_name}`" , inline = True)
        embed.add_field(name = "Discriminator:" , value = f"`#{member.discriminator}`" , inline = True)
        embed.add_field(name = "Base Avatar:" , value = f"[Avatar]({member.avatar})" , inline = True)
        embed.add_field(name = "Display Avatar:" , value = f"[Display Avatar]({member.display_avatar})" , inline = True)
        embed.add_field(name = "Default Avatar:" , value = f"[Default Avatar]({member.default_avatar})" , inline = True)
        embed.add_field(name = f"Is a bot:" , value = f"`{member.bot}`" , inline = True)
        embed.add_field(name = "Creation Date:" , value = f"`{member.created_at.strftime('%d-%m-%y | %H:%M:%S')}`" , inline = True)
        embed.add_field(name = "Join Date:" , value = f"`{member.joined_at.strftime('%d-%m-%y | %H:%M:%S')}`" , inline = True)
        embed.add_field(name = f"Highest Role:" , value = f"<@&{x}>" , inline = True)
        embed.add_field(name = "Is Owner:" , value = f"`{is_Owner}`" , inline = True)
        embed.add_field(name = "Is Booster:" , value = f"`{Boosting}`" , inline = True)
        embed.add_field(name = "Active Developer:" , value = f"`{active_developer}`" , inline = True)
        embed.add_field(name = "Staff Member:" , value = f"`{staff_member}`" , inline = True)
        embed.add_field(name = "Bug Hunter:" , value = f"`{bug_hunter}`" , inline = True)
        embed.add_field(name = "Early Verified Dev:" , value = f"`{EVBD}`" , inline = True)
        embed.add_field(name = "Verified Dev:" , value = f"`{VBD}`" , inline = True)
        embed.add_field(name = "Verified Bot:" , value = f"`{verified_bot}`" , inline = True)
        await ctx.reply(embed = embed)

async def setup(Fireside):
    await Fireside.add_cog(Utility(Fireside))
