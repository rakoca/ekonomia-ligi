from variables import ERRORS as e, CURRENCY_SYMBOL, UNREGISTRED as u, GIVE as g, COMMANDS as c
from essentials import update_bank, get_user, get_user_id
from discord.ext import commands

class Give(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = c['give'])
    async def give(self, ctx, user: str, amount: str):
        if ctx.message.author.top_role.permissions.administrator:
            try:
                update_bank(user, amount)
            except ValueError:
                await ctx.send(e['number'])
                return
            except KeyError:
                await ctx.send(u['friend'])
                return
            await ctx.send(g['success'].format(user = user, amount = CURRENCY_SYMBOL + str(get_user(ctx)['bank'])))
        elif user[2:-1] == get_user_id(ctx):
            await ctx.send(g['error_self'])
        else:
            await ctx.send(g['error_friend'])

async def setup(bot):
    await bot.add_cog(Give(bot))