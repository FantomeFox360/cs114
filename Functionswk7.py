import random
def getAnswer (word):
    word = input('Please input word:  ')
    print (word)
    num = len(word)
    r = random.randint(1, num)
    return r

fortune = getAnswer(23)
print (fortune)
