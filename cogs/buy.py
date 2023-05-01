from discord.ext import commands
from variables import ITEMS as i, CURRENCY_SYMBOL as cs, ERRORS as e, UNREGISTRED as u, COMMANDS as c
from essentials import get_user, determine_gender, update_cash


class Buy(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name = c['buy'])
    async def buy(self, ctx, id):
        if get_user(ctx):
            try:
                id = abs(int(id))
            except:
                await ctx.send(e['number'])
                return
            if id >= len(i['items']):
                await ctx.send(i['too_big_id'])
            elif get_user(ctx)['cash'] < i['items'][id]['price']:
                await ctx.send(e['low_cash'])
            else:
                get_user(ctx)['items'].append(id)
                update_cash(ctx, -i['items'][id]['price'])
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Buy(bot))