from discord.ext import commands
from variables import WOTD as w, COMMANDS as c
from bs4 import BeautifulSoup as BS
from requests import get

class Wotd2(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.word = None
        self.soup = None

    @commands.command(name = c['wotd'])
    async def wotd2(self, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            self.soup = BS(get('https://sjp.pl/sl/los/').content, 'html.parser')
            self.word = '<@&' + str(w['role']) + '>\n'
            self.word += '**' + str(self.soup.find_all('h1')[0].contents[0]) + '**' + '\n'
            self.soup = str(self.soup.find_all('p')[3].contents).replace("['", '').replace("', <br/>, '", '\n').replace("']", '')
            self.word += self.soup
            await self.bot.get_channel(w['channel']).send(self.word)

async def setup(bot):
    await bot.add_cog(Wotd2(bot))