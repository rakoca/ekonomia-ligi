from random import randint
from discord.ext import commands
from variables import CURRENCY_SYMBOL, WORK as w, UNREGISTRED as u
from essentials import get_user, check_cooldown, update_cash, reset_cooldown, get_cooldown, determine_gender

class Work(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'pracuj')
    async def work(self, ctx):
        if get_user(ctx):
            if check_cooldown(ctx, 'work'):
                amount = randint(w['range'][0], w['range'][1])
                update_cash(ctx, amount)
                reset_cooldown(ctx, 'work')
                reply = w['replies'][randint(0, len(w['replies']) - 1)]
                await ctx.send(reply.format(amount = CURRENCY_SYMBOL + str(amount), gender = determine_gender(ctx)))
            else:
                await ctx.send(w['cooldown'].format(gender = determine_gender(ctx), time = get_cooldown(ctx, 'work')))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Work(bot))