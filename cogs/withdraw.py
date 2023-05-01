from variables import UNREGISTRED as u, WITHDRAW as w, ERRORS as e, CURRENCY_SYMBOL, COMMANDS as c
from essentials import get_user, determine_gender, set_bank, update_cash, update_bank
from discord.ext import commands

class Withdraw(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.bank = 0
        self.amount = 0

    @commands.command(name = c['withdraw'])
    async def withdraw(self, ctx, amount):
        if get_user(ctx):
            self.bank = get_user(ctx)['bank']
            if amount == 'wszystko':
                await ctx.send(w['success'].format(amount = CURRENCY_SYMBOL + str(self.bank)))
                update_cash(ctx, self.bank)
                set_bank(ctx, 0)
            else:
                try:
                    self.amount = int(amount)
                except:
                    await ctx.send(e['number'])
                    return
                if self.amount < 0:
                    await ctx.send(e['number'])
                elif self.amount > self.bank:
                    await ctx.send(e['low_bank'])
                else:
                    update_bank(ctx, -self.amount)
                    update_cash(ctx, self.amount)
                    await ctx.send(w['success'].format(amount = CURRENCY_SYMBOL + str(self.amount)))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Withdraw(bot))