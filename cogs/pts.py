from discord.ext import commands
from variables import COMMANDS  as c, QUASIADMINS as q, ERRORS as e, SUCCESS as s
from essentials import get_user

class Pts(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name=c['pts'])
    async def pts(self, ctx, user, amount):
        if ctx.message.author.top_role.permissions.administrator or ctx.message.author.id in q:
            try: int(amount)
            except: await ctx.send(e['number'])
            get_user([user])['pts'] += int(amount)
            await ctx.send(s)


async def setup(bot):
    await bot.add_cog(Pts(bot))