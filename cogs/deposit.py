from variables import DEPOSIT as d, CURRENCY_SYMBOL, UNREGISTRED as u, ERRORS as e, COMMANDS as c
from essentials import get_user, update_bank, set_cash, update_cash, determine_gender
from discord.ext import commands

class Deposit(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.cash = 0

    @commands.command(name = c['deposit'])
    async def deposit(self, ctx, amount):
        if get_user(ctx):
            self.cash = get_user(ctx)['cash']
            if amount == 'wszystko':
                await ctx.send(d['success'].format(amount = CURRENCY_SYMBOL + str(self.cash)))
                update_bank(ctx, self.cash)
                set_cash(ctx, 0)
            else:
                try: amount = int(amount)
                except:
                    await ctx.send(e['number'])
                    return
                if amount > self.cash:
                    await ctx.send(e['low_cash'])
                elif amount < 0:
                    await ctx.send(e['number'])
                else:
                    update_cash(ctx, -amount)
                    update_bank(ctx, amount)
                    await ctx.send(d['success'].format(amount = CURRENCY_SYMBOL + str(amount)))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Deposit(bot))