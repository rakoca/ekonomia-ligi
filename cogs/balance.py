from variables import CURRENCY_SYMBOL, BALANCE as b, UNREGISTRED as u, COMMANDS as c
from essentials import  get_user, determine_gender
from discord.ext import commands

class Balance(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = c['balance'])
    async def balance(self, ctx, *user: str):
        if user:
            if get_user(user):
                await ctx.send(b['friend'].format(
                    cash = CURRENCY_SYMBOL + str(get_user(user)['cash']),
                    bank = CURRENCY_SYMBOL + str(get_user(user)['bank']),
                    total = CURRENCY_SYMBOL + str(get_user(user)['cash'] + get_user(user)['bank']),
                    pts = str(get_user(user)['pts'])
                    )
                )
            else: await ctx.send(u['friend'])
        else:
            if get_user(ctx):
                await ctx.send(b['self'].format(
                    cash = CURRENCY_SYMBOL + str(get_user(ctx)['cash']),
                    bank = CURRENCY_SYMBOL + str(get_user(ctx)['bank']),
                    total = CURRENCY_SYMBOL + str(get_user(ctx)['cash'] + get_user(ctx)['bank']),
                    pts = str(get_user(ctx)['pts'])
                    )
                )
            else:
                await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Balance(bot))