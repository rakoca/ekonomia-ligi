from requests import get
from bs4 import BeautifulSoup as BS
from variables import WOTD as w
from discord.ext import tasks, commands
from datetime import time as dtime

class Wotd(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @tasks.loop(time = dtime(hour = w['time']))
    async def word_of_the_day(self):
        channel = self.bot.get_channel(w['channel'])
        req = get('https://sjp.pl/sl/los/')
        soup = BS(req.content, 'html.parser')
        word = '<@&' + str(w['role']) + '>\n'
        word += '**' + req.url.split('/')[-1] + '**' + '\n'
        soup = str(soup.find_all('p')[3])
        soup = soup[74:-4]
        soup = soup.replace('<br/>', '\n')
        word += soup
        await channel.send(word)
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.word_of_the_day.start()

async def setup(bot):
    await bot.add_cog(Wotd(bot))