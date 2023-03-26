from variables import UNREGISTRED as u, WITHDRAW as w, NUMBER_ERROR_REPLY, CURRENCY_SYMBOL
from essentials import get_user, determine_gender, set_bank, update_cash, update_bank
from discord.ext import commands

class Withdraw(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'wypłać')
    async def withdraw(self, ctx, amount):
        if get_user(ctx):
            bank = get_user(ctx)['bank']
            if amount == 'wszystko':
                await ctx.send(w['success'].format(amount = CURRENCY_SYMBOL + str(bank)))
                update_cash(ctx, bank)
                set_bank(ctx, 0)
            else:
                try:
                    amount = int(amount)
                except:
                    await ctx.send(NUMBER_ERROR_REPLY)
                    return
                if amount < 0:
                    await ctx.send(NUMBER_ERROR_REPLY)
                elif amount > bank:
                    await ctx.send(w['low_bank'])
                else:
                    update_bank(ctx, -amount)
                    update_cash(ctx, amount)
                    await ctx.send(w['success'].format(amount = CURRENCY_SYMBOL + str(amount)))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Withdraw(bot))