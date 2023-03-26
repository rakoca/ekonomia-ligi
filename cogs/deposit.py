from variables import DEPOSIT as d, CURRENCY_SYMBOL, UNREGISTRED as u
from essentials import get_user, update_bank, set_cash, update_cash, determine_gender
from discord.ext import commands

class Deposit(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'wpłać')
    async def deposit(self, ctx, amount):
        if get_user(ctx):
            if amount == 'wszystko':
                await ctx.send(d['success'].format(amount = CURRENCY_SYMBOL + str(get_user(ctx)['cash'])))
                update_bank(ctx, get_user(ctx)['cash'])
                set_cash(ctx, 0)
            else:
                try: amount = int(amount)
                except:
                    await ctx.send(d['fail'])
                    return
                if amount > get_user(ctx)['cash']:
                    await ctx.send(d['low_cash'])
                elif amount <= 0:
                    await ctx.send(d['fail'])
                else:
                    update_cash(ctx, -amount)
                    update_bank(ctx, amount)
                    await ctx.send(d['success'].format(amount = CURRENCY_SYMBOL + str(amount)))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Deposit(bot))