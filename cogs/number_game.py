from random import randint
from variables import NUMBER_GAME as ng, UNREGISTRED as u, ERRORS as e, COMMANDS as c
from essentials import get_user, check_cooldown, determine_gender, update_cash, update_bank, reset_cooldown, get_cooldown
from discord.ext import commands

class NumberGame(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.bet = tuple()
        self.numbers = set()
        self.reply = ''
        self.number = 0
        self.amount = 0

    @commands.command(name = c['number_game'])
    async def number_game(self, ctx, bet):
        if get_user(ctx):
            if check_cooldown(ctx, 'number_game'):
                self.bet = tuple(set(bet.split(' ')))
                if len(self.bet) != ng['bets']:
                    await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                    return
                else:
                    for i in range(len(self.bet)):
                        try: int(self.bet[i])
                        except:
                            await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                            return
                        if int(self.bet[i]) < 1 or int(self.bet[i]) > ng['range']:
                            await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                            return
                        
                if (get_user(ctx)['cash'] < ng['price']):
                    await ctx.send(e['low_cash'])
                    return
                else:
                    update_cash(ctx, -ng['price'])                        
                
                while len(self.numbers) != ng['bets']:
                    self.numbers.add(str(randint(1, ng['range'])))
                self.reply += ng['numbers'].format(numbers = str(self.numbers)[1:-1]).replace("'", '') + '\n'
                for i in range(len(self.bet)):
                    if self.bet[i] in self.numbers: self.number += 1
                self.amount = ng['payouts'].get(str(self.number))
                if self.amount:
                    self.reply += ng['won'].format(gender = determine_gender(ctx), amount = self.amount, number = self.number, NUMBER_GAME_BETS = ng['bets'])
                    update_bank(ctx, self.amount)
                    await ctx.send(self.reply)
                else:
                    self.reply += ng['lose'].format(gender = determine_gender(ctx), number = self.number, NUMBER_GAME_BETS = ng['bets'])
                    await ctx.send(self.reply)
                reset_cooldown(ctx, 'number_game')
                self.numbers = set()
                self.reply = ''
                self.number = 0
            else:
                await ctx.send(ng['cooldown'].format(time = get_cooldown(ctx, 'number_game')))
            
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(NumberGame(bot))