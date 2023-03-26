from discord.ext import commands
from essentials import get_user, determine_gender, update_bank
from variables import UNREGISTRED as u, NUMBER_ERROR_REPLY, TRANSFER as t, CURRENCY_SYMBOL


class Transfer(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name = 'przelej')
    async def transfer(self, ctx, user, amount):
        if get_user(ctx):
            if get_user(user):
                try:
                    amount = int(amount)
                except:
                    await ctx.send(NUMBER_ERROR_REPLY)
                    return
                if amount < 0:
                    await ctx.send(NUMBER_ERROR_REPLY)
                elif amount > get_user(ctx)['bank']:
                    await ctx.send(t['low_bank'])
                else:
                    update_bank(user, amount)
                    update_bank(ctx, -amount)
                    await ctx.send(t['success'].format(amount = CURRENCY_SYMBOL + str(amount), user = user))
            else:
                await ctx.send(u['friend'])
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Transfer(bot))