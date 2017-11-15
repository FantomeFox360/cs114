print('what is your name')
name = input()
print('its good to meet you' + name)

import random
def randomanswer():
    r = random.randint(1,8)
    if r == 1:
        return 'your day will be filled with doom'
    elif r == 2:
        return 'killing luck today'
    elif r == 3:
        return 'gloomy day good luck out thier'
    elif r == 4:
        return 'your day will be filled with joy'
    elif r == 5:
        return 'someone you know may die today'
    elif r == 6:
        return 'armagendon is coming'
    elif r == 7:
        return 'light will follow you eveywhere today'
    elif r == 8:
        return 'your day is considered to be the best day ever and everything will go your way'

fortune = randomanswer()
print(fortune)
