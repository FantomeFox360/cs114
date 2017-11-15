import random
def randomscreem():
    atext = ('A') * random.randint(1,16)
    htext = ('H') * random.randint(1,16)
    msg= atext + htext
    return msg
output = randomscreem()
while True:
    print(randomscreem())
