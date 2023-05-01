from json import dumps
from variables import users, JSON_UPDATED, COMMANDS as c
from discord.ext import commands

class UpdateJson(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.file = None

    @commands.command(name = c['update_json'])
    async def update_json(self, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            self.file = open('./users.json', 'w')
            self.file.write(dumps(users))
            self.file.close()
            await ctx.send(JSON_UPDATED)

async def setup(bot):
    await bot.add_cog(UpdateJson(bot))