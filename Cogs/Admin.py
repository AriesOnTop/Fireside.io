from discord.ext import commands
from discord.ext.commands import guild_only , has_guild_permissions

class Admin(commands.Cog):
    def __init__(self, Fireside):
        self.Fireside = Fireside

    @guild_only()
    @has_guild_permissions(manage_guild = True)
    @commands.command(aliases = ["cr"])
    async def yes(self , ctx):
        pass

async def setup(Fireside):
    await Fireside.add_cog(Admin(Fireside))
