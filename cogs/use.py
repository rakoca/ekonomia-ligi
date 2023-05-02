from discord.ext import commands
from variables import COMMANDS as c, UNREGISTRED as u, ERRORS as e, ITEMS as i
from essentials import get_user, determine_gender

class Use(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.id = 0
        self.actions = ''
    
    @commands.command(name = c['use'])
    async def use(self, ctx, id, *args):
        if get_user(ctx):
            try:
                self.id = abs(int(id))
            except:
                await ctx.send(e['number'])
                return
            if self.id in get_user(ctx)['items']:
                get_user(ctx)['items'].remove(self.id)          
                self.actions = i['items'][self.id]['action'].split('|')
                for action in self.actions:
                    if action.startswith('say '):
                        await ctx.send(action[3:].format(gender = determine_gender(ctx)))
            else:
                await ctx.send(i['item_not_found'])
        else:
            await ctx.send(u['self'])

async def setup(bot):
    await bot.add_cog(Use(bot))