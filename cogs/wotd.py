from discord.ext import commands
from variables import WOTD as w, COMMANDS as c
from bs4 import BeautifulSoup as BS
from requests import get

class Wotd2(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.word = None
        self.soup = None
        self.file = None
        self.wotd_custom = None
        self.content = ''

    @commands.command(name = c['wotd'])
    async def wotd2(self, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            self.file = open('wotd_custom', 'r')
            self.wotd_custom = self.file.read().split('|')
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
                    for element in self.wotd_custom[1:]:
                        self.content += element + '|'
                    self.file.write(self.content)
                except:
                    pass
                self.file.close()
                self.wotd_custom = None
            else:
                self.word = '<@&' + str(w['role']) + '>\n'
                self.word += '**' + self.wotd_custom[0] + '**'
                self.wotd_custom[1] = self.wotd_custom[1].split('\n')
                await self.bot.get_channel(w['channel']).send(self.word)
                for element in self.wotd_custom[1]:
                    await self.bot.get_channel(w['channel']).send(element)
                self.file = open('wotd_custom', 'w')
                self.content = ''
                for element in self.wotd_custom[2:-1]:
                    self.content += element + '|'
                self.file.write(self.content)
                self.file.close()
                self.wotd_custom = None


async def setup(bot):
    await bot.add_cog(Wotd2(bot))