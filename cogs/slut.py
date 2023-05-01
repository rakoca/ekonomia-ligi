from random import randint
from variables import CURRENCY_SYMBOL, SLUT as s, UNREGISTRED as u, COMMANDS as c
from essentials import get_user, check_cooldown, update_cash, determine_gender, set_cash, set_bank, update_bank, reset_cooldown, get_cooldown
from discord.ext import commands

class Slut(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.reply = ''
        self.amount = 0
        self.balance = 0

    @commands.command(name = c['slut'])
    async def slut(self, ctx):
        if get_user(ctx):
            if check_cooldown(ctx, 'slut'):
                if randint(0, 1):
                    self.reply = s['replies_p'][randint(0, len(s['replies_p']) - 1)]
                    self.amount = randint(s['range_p'][0], s['range_p'][1])
                    update_cash(ctx, self.amount)
                    await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(self.amount)))
                else:
                    self.reply = s['replies_f'][randint(0, len(s['replies_f']) - 1)]
                    self.amount = randint(s['range_f'][0], s['range_f'][1])
                    self.balance = get_user(ctx)['bank'] + get_user(ctx)['cash']
                    if self.balance < self.amount:
                        await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(get_user(ctx)['cash'] + get_user(ctx)['bank'])))
                        set_cash(ctx, 0)
                        set_bank(ctx, 0)
                    else:
                        if get_user(ctx)['cash'] < self.amount:
                            update_bank(ctx, get_user(ctx)['cash'] - self.amount)
                            set_cash(ctx, 0)
                        else:
                            update_cash(ctx, -self.amount)
                        await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(self.amount)))
                reset_cooldown(ctx, 'slut')
            else:
                await ctx.send(s['cooldown'].format(gender = determine_gender(ctx), time = get_cooldown(ctx, 'slut')))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Slut(bot))