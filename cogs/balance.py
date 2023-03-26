from variables import CURRENCY_SYMBOL, BALANCE as b, UNREGISTRED as u
from essentials import get_user_by_id, get_user, determine_gender
from discord.ext import commands

class Balance(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'majątek')
    async def balance(self, ctx, *user: str):
        if user:
            if get_user_by_id(user):
                await ctx.send(b['friend'].format(
                    cash = CURRENCY_SYMBOL + str(get_user_by_id(user)['cash']),
                    bank = CURRENCY_SYMBOL + str(get_user_by_id(user)['bank']),
                    total = CURRENCY_SYMBOL + str(get_user_by_id(user)['cash'] + get_user_by_id(user)['bank'])
                    )
                )
            else: await ctx.send(u['friend'])
        else:
            if get_user(ctx):
                await ctx.send(b['self'].format(
                    cash = CURRENCY_SYMBOL + str(get_user(ctx)['cash']),
                    bank = CURRENCY_SYMBOL + str(get_user(ctx)['bank']),
                    total = CURRENCY_SYMBOL + str(get_user(ctx)['cash'] + get_user(ctx)['bank'])
                    )
                )
            else:
                await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Balance(bot))