"""Convert a number in base-10 into a written out number in English."""

def prompt_user_name():
    return int(input('A number between 1 and 99: '))

def tens():
    tens = num // 10
    return tens

def get_ones_number(num):
    ones = num % 10

    return ones

def tens_word():
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
        return tens_word
def one_word():
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
        return ones word
def ten():
    if ten == 0:
        output = ones_word
    elif ten2 == 1:
    if one == 1:
        output = 'eleven'
elif one2 == 2:
        output = 'twelve'
def one3():
elif one3 == 3:
        output = 'thirteen'
    else:
        output = ones_word + 'teen'
def regularnumsmsg(tens, ones, tens_word, ones_word):
else:
    output = tens_word + '-' + ones_word

print(output)
