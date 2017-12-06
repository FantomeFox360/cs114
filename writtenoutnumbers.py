"""Convert a number in base-10 into a written out number in English."""

def prompt_user_for_number():
    return int(input('A number between 1 and 99: '))

def get_tens_number(num):
    tens = num // 10
    return tens

def get_ones_number(num):
    ones = num % 10
    return ones

def get_tens_word(tens):
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

def get_ones_word(ones):
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
    return ones_word

def get_irregular_numbers(ones, ones_word, tens_word):
    if ones == 1:
        return 'eleven'
    elif ones == 2:
        return  'twelve'
    elif ones == 3:
        return  'thirteen'
    else:
        return  ones_word + 'teen'


def regular_numbers_message(tens, ones, tens_word, ones_word):
    return tens_word + '-' + ones_word

def main():
    num = prompt_user_for_number()
    tens = get_tens_number(num)
    ones = get_ones_number(num)
    tens_word = get_tens_word(tens)
    ones_word = get_ones_word(ones)
    irregular_numbers = get_irregular_numbers(ones, ones_word, tens_)
    message = regular_numbers_message(tens, ones, tens_word, ones_word)
    print(message)

main()
