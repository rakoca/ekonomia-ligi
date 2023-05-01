from json import loads
from time import time
from datetime import time as dtime
from discord.ext import commands
import discord

file = open('config.json')
config = loads(file.read())
file.close()

file = open('users.json')
users = loads(file.read())
file.close()

SCHEME = {
    'cash': 0,
    'bank': 0,
    'items': [],
    'work_cooldown': time(),
    'crime_cooldown': time(),
    'slut_cooldown': time(),
    'number_game_cooldown': time()
}
COMMANDS = config.get('commands')
PREFIX = config.get('prefix')
DESC = config.get('desc')
CURRENCY_SYMBOL = config.get('currency_symbol')
JSON_UPDATED = config.get('json_updated')
GIRL_ROLE = config.get('girl_role')
ERRORS = config.get('errors')
UNREGISTRED = config.get('unregistred')
REGISTRED  = config.get('registred')
GIVE = config.get('give')
BALANCE = config.get('balance')
WORK = config.get('work')
CRIME = config.get('crime')
SLUT = config.get('slut')
NUMBER_GAME = config.get('number_game')
DEPOSIT = config.get('deposit')
COOLDOWNS = config.get('cooldowns')
ROB = config.get('rob')
WOTD = config.get('wotd')
WITHDRAW = config.get('withdraw')
TRANSFER = config.get('transfer')
ITEMS = config.get('items')
config = None