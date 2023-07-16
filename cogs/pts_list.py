from discord.ext import commands
from variables import COMMANDS as c, QUASIADMINS as q, users

class PtsList(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.list = ''

    @commands.command(name=c['pts_list'])
    async def pts_list(self, ctx):
        if ctx.message.author.top_role.permissions.administrator or ctx.message.author.id in q:
            for id in users:
                self.list += '<@' + id + '>: ' + str(users[id].get('pts')) + '\n'
            await ctx.send(self.list)
            self.list = ''

async def setup(bot):
    await bot.add_cog(PtsList(bot))