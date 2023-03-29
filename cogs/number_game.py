from random import randint
from variables import NUMBER_GAME as ng, UNREGISTRED as u
from essentials import get_user, check_cooldown, determine_gender, update_cash, update_bank, reset_cooldown, get_cooldown
from discord.ext import commands

class NumberGame(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'totolotek')
    async def number_game(self, ctx, bet):
        if get_user(ctx):
            if check_cooldown(ctx, 'number_game'):
                if (get_user(ctx)['cash'] < ng['cost']):
                    await ctx.send(ng['low_cash'].format(gender = determine_gender(ctx)))
                    return
                else:
                    update_cash(ctx, -ng['cost'])

                bet = tuple(set(bet.split(' ')))
                if len(bet) != ng['bets']:
                    await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                    return
                else:
                    for i in range(len(bet)):
                        try: int(bet[i])
                        except:
                            await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                            return
                        if int(bet[i]) < 1 or int(bet[i]) > ng['range']:
                            await ctx.send(ng['wrong_bet'].format(NUMBER_GAME_BETS = ng['bets'], NUMBER_GAME_RANGE = ng['range']))
                            return
                        
                numbers = set()
                reply = ''
                number = 0
                while len(numbers) != ng['bets']:
                    numbers.add(str(randint(1, ng['range'])))
                reply += ng['numbers'].format(numbers = str(numbers)[1:-1]).replace("'", '') + '\n'
                for i in range(len(bet)):
                    if bet[i] in numbers: number += 1
                amount = ng['payouts'].get(str(number))
                if amount:
                    reply += ng['won'].format(gender = determine_gender(ctx), amount = amount, number = number, NUMBER_GAME_BETS = ng['bets'])
                    update_bank(ctx, amount)
                    await ctx.send(reply)
                else:
                    reply += ng['lose'].format(gender = determine_gender(ctx), number = number, NUMBER_GAME_BETS = ng['bets'])
                    await ctx.send(reply)
                reset_cooldown(ctx, 'number_game')
            else:
                await ctx.send(ng['cooldown'].format(time = get_cooldown(ctx, 'number_game')))
            
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(NumberGame(bot))