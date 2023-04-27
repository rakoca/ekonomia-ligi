from discord.ext import commands
from variables import WOTD as w
from bs4 import BeautifulSoup as BS
from requests import get

class Wotd2(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name = 'sd')
    async def wotd2(self, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            channel = self.bot.get_channel(w['channel'])
            req = get('https://sjp.pl/sl/los/')
            soup = BS(req.content, 'html.parser')
            word = '<@&' + str(w['role']) + '>\n'
            word += '**' + str(soup.find_all('h1')[0].contents[0]) + '**' + '\n'
            soup = str(soup.find_all('p')[3].contents[0])
            soup = soup.replace('<br/>', '\n')
            word += soup
            await channel.send(word)

async def setup(bot):
    await bot.add_cog(Wotd2(bot))