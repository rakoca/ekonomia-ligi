from discord.ext import commands
from essentials import get_user, determine_gender, update_bank
from variables import UNREGISTRED as u, ERRORS as e, TRANSFER as t, CURRENCY_SYMBOL, COMMANDS as c


class Transfer(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.amount = 0
    
    @commands.command(name = c['transfer'])
    async def transfer(self, ctx, user, amount):
        if get_user(ctx):
            if get_user(user):
                try:
                    self.amount = int(amount)
                except:
                    await ctx.send(e['number'])
                    return
                if self.amount < 0:
                    await ctx.send(e['number'])
                elif self.amount > get_user(ctx)['bank']:
                    await ctx.send(e['low_bank'])
                else:
                    update_bank(user, self.amount)
                    update_bank(ctx, -self.amount)
                    await ctx.send(t['success'].format(amount = CURRENCY_SYMBOL + str(self.amount), user = user))
            else:
                await ctx.send(u['friend'])
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Transfer(bot))