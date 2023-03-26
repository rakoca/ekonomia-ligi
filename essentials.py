from variables import users, COOLDOWNS, GIRL_ROLE
from time import time

def get_user(ctx) -> list:
    try: return users.get(str(ctx.message.author.id))
    except: return users.get(ctx[0][2:-1])
def get_user_id(ctx) -> str:
    return str(ctx.message.author.id)
def update_cash(ctx, amount) -> None:
    try: users[str(ctx.message.author.id)]['cash'] += int(amount)
    except: users[ctx[0][2:-1]]['cash'] += int(amount)
def set_cash(ctx, amount) -> None:
    try: users[str(ctx.message.author.id)]['cash'] = int(amount)
    except: users[ctx[0][2:-1]]['cash'] = int(amount)
def update_bank(ctx, amount) -> None:
    try: users[str(ctx.message.author.id)]['bank'] += int(amount)
    except: users[ctx[0][2:-1]]['bank'] += int(amount)
def set_bank(ctx, amount) -> None:
    try: users[str(ctx.message.author.id)]['bank'] = int(amount)
    except: users[ctx[0][2:-1]]['bank'] += int(amount)
def reset_cooldown(ctx, type: str) -> None:
    users[str(ctx.message.author.id)][type + '_cooldown'] = time()
def check_cooldown(ctx, type) -> bool:
    return time() - get_user(ctx)[type + '_cooldown'] >= COOLDOWNS[type]
def get_cooldown(ctx, type) -> int:
    return int(COOLDOWNS[type] - time() + get_user(ctx)[type + '_cooldown'])
    return id[2:-1]
def determine_gender(ctx) -> str:
    if ctx.message.author.get_role(GIRL_ROLE):
        return ('a', 'ę', 'a', 'szłaś', 'a')
    else:
        return ('e', 'ą', 'y', 'szedłeś', '')
