from discord.ext import commands
import discord
from variables import COMMANDS as c, UNREGISTRED as u, ERRORS as e, ITEMS as i, NAME
from essentials import get_user, determine_gender

class Use(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.id = 0
        self.commands = ''
        self.guild = None
    
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
                self.commands = i['items'][self.id]['command'].split('|')
                self.guild = ctx.guild
                for command in self.commands:
                    if command.startswith('say '):
                        await ctx.send(command[3:].format(gender = determine_gender(ctx)))
                    if command.startswith('createrole '):
                        command = command.split(' ')
                        name = None
                        color = None
                        pos = discord.utils.get(ctx.guild.roles, name=NAME).position - 1
                        for argument in command:
                            if argument.startswith('color:'):
                                color = args[int(argument.split(':')[1])]
                            if argument.startswith('name:'):
                                name = args[int(argument.split(':')[1])]
                            try:
                                role = await self.guild.create_role(name=name, color=discord.Color(int(color, 16)))
                                await role.edit(position=pos)
                                await ctx.message.author.add_roles(role)
                            except Exception as e:
                                print(e)
                                #PROPOZYCJA: kolor jest dodawany do bazy kolorów użytkownika i ten może sobie dowolnie z nich wybierać
            else:
                await ctx.send(i['item_not_found'])
        else:
            await ctx.send(u['self'])

async def setup(bot):
    await bot.add_cog(Use(bot))