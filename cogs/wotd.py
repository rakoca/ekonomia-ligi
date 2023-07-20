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
            self.wotd_custom = self.file.read().split('\n\n')
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
                    for element in self.wotd_custom[1:-2]:
                        self.content += element + '\n\n'
                    self.content += self.wotd_custom[-1]
                    self.file.write(self.content)
                except:
                    pass
                self.file.close()
                self.file = None
                self.wotd_custom = None
            else:
                self.word = '<@&' + str(w['role']) + '>\n'
                self.wotd_custom = self.wotd_custom[0].split('\n')
                self.word += '**' + self.wotd_custom[0] + '**'
                await self.bot.get_channel(w['channel']).send(self.word)
                for element in self.wotd_custom[1:]:
                    await self.bot.get_channel(w['channel']).send(element)
                self.file = open('wotd_custom', 'r')
                self.content = self.file.read()
                self.file.close()
                self.file = None
                self.content = self.content.split('\n\n')
                self.wotd_custom = ''
                for element in self.content[1:-2]:
                    self.wotd_custom += element + '\n\n'
                self.wotd_custom += self.content[-1]
                self.file = open('wotd_custom', 'w+')
                self.file.write(self.wotd_custom)
                self.file.close()
                self.wotd_custom = None


async def setup(bot):
    await bot.add_cog(Wotd2(bot))