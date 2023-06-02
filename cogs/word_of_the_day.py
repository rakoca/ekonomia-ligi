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
        self.file = None
        self.wotd_custom = None
        self.content = ''
        
    @tasks.loop(time = dtime(hour = w['time']))
    async def word_of_the_day(self):
        self.file = open('wotd_custom', 'r')
        self.wotd_custom = self.file.read().split('\n')
        self.file.close()
        if (self.wotd_custom[0] == ''):
            self.soup = BS(get('https://sjp.pl/sl/los/').content, 'html.parser')
            self.word = '<@&' + str(w['role']) + '>\n'
            self.word += '**' + str(self.soup.find_all('h1')[0].contents[0]) + '**' + '\n'
            self.soup = str(self.soup.find_all('p')[3].contents).replace("['", '').replace("', <br/>, '", '\n').replace("']", '')
            self.word += self.soup
            await self.bot.get_channel(w['channel']).send(self.word)
            self.file = open('wotd_custom', 'w')
            self.content = ''
            try: 
                for element in self.wotd_custom[1:-1]:
                    self.content += element + '\n'
                self.file.write(self.content)
            except:
                pass
            self.file.close()
            self.wotd_custom = None
        else:
            self.word = '<@&' + str(w['role']) + '>\n'
            self.word += '**' + self.wotd_custom[0] + '**' + '\n'
            self.word += self.wotd_custom[1]
            await self.bot.get_channel(w['channel']).send(self.word)
            self.file = open('wotd_custom', 'w')
            self.content = ''
            for element in self.wotd_custom[2:-1]:
                self.content += element + '\n'
            self.file.write(self.content)
            self.file.close()
            self.wotd_custom = None

    @commands.Cog.listener()
    async def on_ready(self):
        await self.word_of_the_day.start()

   
async def setup(bot):
    await bot.add_cog(Wotd(bot))