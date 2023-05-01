from discord.ext import commands
from essentials import get_user, determine_gender
from variables import ITEMS as i, UNREGISTRED as u, COMMANDS as c

class ItemsList(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.response = ''
        self.items = set()

    @commands.command(name = c['items_list'])
    async def items_list(self, ctx):
        if get_user(ctx):
            self.items = set(get_user(ctx)['items'])
            for n in self.items:
                self.response += '**' + i['items'][n]['name'] + '** (x' + str(get_user(ctx)['items'].count(n)) +')\n' + i['items'][n]['desc'] + '\n\n'
            await ctx.send(self.response)
            self.response = ''
        else:
            await ctx.send(u['self'].format(gender = determine_gender(ctx)))

async def setup(bot):
    await bot.add_cog(ItemsList(bot))