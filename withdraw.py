from variables import bot, UNREGISTRED as u
from essentials import get_user, determine_gender

# przenieść ten  plik do ./cogs po napisaniu skryptu

@bot.command(name = 'wypłać')
async def withdraw(ctx, amount):
    if get_user(ctx):
        if amount == 'wszystko':
            await ctx.send()
    else:
        await ctx.send(u['self'].format(gender = determine_gender(ctx)))