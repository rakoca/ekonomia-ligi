from variables import SCHEME, users, REGISTRED as r, COMMANDS as c
from essentials import get_user, determine_gender, get_user_id
from json import dumps
from discord.ext import commands

class Register(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name = c['register'])
    async def register(self, ctx):
        if get_user(ctx):
            await ctx.send(r['reply'].format(gender = determine_gender(ctx)))
        else: 
            users.update({get_user_id(ctx): SCHEME.copy()})
            file = open('users.json', 'w')
            file.write(dumps(users))
            file.close()
            await ctx.send(r['success'])

async def setup(bot):
    await bot.add_cog(Register(bot))