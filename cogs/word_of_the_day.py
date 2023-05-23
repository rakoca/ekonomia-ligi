from requests import get
from bs4 import BeautifulSoup as BS
from variables import WOTD as w
from discord.ext import tasks, commands
from datetime import time as dtime

class Wotd(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.word = None
        self.soup = None
        
    @tasks.loop(time = dtime(hour = w['time']))
    async def word_of_the_day(self):
        self.soup = BS(get('https://sjp.pl/sl/los/').content, 'html.parser')
        self.word = '<@&' + str(w['role']) + '>\n'
        self.word += '**' + str(self.soup.find_all('h1')[0].contents[0]) + '**' + '\n'
        self.soup = str(self.soup.find_all('p')[3].contents).replace("['", '').replace("', <br/>, '", '\n').replace("']", '')
        self.word += self.soup
        await self.bot.get_channel(w['channel']).send(self.word)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.word_of_the_day.start()

   
async def setup(bot):
    await bot.add_cog(Wotd(bot))