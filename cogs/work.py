from random import randint
from discord.ext import commands
from variables import CURRENCY_SYMBOL, WORK as w, UNREGISTRED as u, COMMANDS as c
from essentials import get_user, check_cooldown, update_cash, reset_cooldown, get_cooldown, determine_gender

class Work(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.amount = 0
        self.reply = ''

    @commands.command(name = c['work'])
    async def work(self, ctx):
        if get_user(ctx):
            if check_cooldown(ctx, 'work'):
                self.amount = randint(w['range'][0], w['range'][1])
                update_cash(ctx, self.amount)
                reset_cooldown(ctx, 'work')
                self.reply = w['replies'][randint(0, len(w['replies']) - 1)]
                await ctx.send(self.reply.format(amount = CURRENCY_SYMBOL + str(self.amount), gender = determine_gender(ctx)))
            else:
                await ctx.send(w['cooldown'].format(gender = determine_gender(ctx), time = get_cooldown(ctx, 'work')))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Work(bot))