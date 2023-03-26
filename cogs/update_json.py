from json import dumps
from variables import users, JSON_UPDATED
from discord.ext import commands

class UpdateJson(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'zaktualizuj_json')
    async def update_json(self, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            file = open('users.json', 'w')
            file.write(dumps(users))
            file.close()
            await ctx.send(JSON_UPDATED)

async def setup(bot):
    await bot.add_cog(UpdateJson(bot))