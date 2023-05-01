from random import randint
from variables import CURRENCY_SYMBOL, CRIME as c, UNREGISTRED as u, COMMANDS as cmd
from essentials import get_user, check_cooldown, update_cash, determine_gender, set_cash, set_bank, update_bank, reset_cooldown, get_cooldown
from discord.ext import commands

class Crime(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.reply = ''
        self.amount = 0
        self.balance = 0

    @commands.command(name = cmd['crime'])
    async def crime(self, ctx):
        if get_user(ctx):
            if check_cooldown(ctx, 'crime'):
                if randint(0, 1):
                    self.reply = c['replies_p'][randint(0, len(c['replies_p']) - 1)]
                    self.amount = randint(c['range_p'][0], c['range_p'][1])
                    update_cash(ctx, self.amount)
                    await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(self.amount)))
                else:
                    self.reply = c['replies_f'][randint(0, len(c['replies_f']) - 1)]
                    self.amount = randint(c['range_f'][0], c['range_f'][1])
                    self.balance = get_user(ctx)['cash'] + get_user(ctx)['bank']
                    if self.balance < self.amount:
                        await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(self.balance)))
                        set_cash(ctx, 0)
                        set_bank(ctx, 0)
                    else:
                        if get_user(ctx)['cash'] < self.amount:       
                            update_bank(ctx, get_user(ctx)['cash'] - self.amount)
                            set_cash(ctx, 0)
                        else:
                            update_cash(ctx, -self.amount)
                        await ctx.send(self.reply.format(gender = determine_gender(ctx), amount = CURRENCY_SYMBOL + str(self.amount)))
                reset_cooldown(ctx, 'crime')
            else:
                await ctx.send(c['cooldown'].format(gender = determine_gender(ctx), time = get_cooldown(ctx, 'crime')))
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(Crime(bot))