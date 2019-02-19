

from random import choice
from string import ascii_letters
from string import digits

all_choice = ascii_letters + digits + '_'

def pas(num=8):
    result = ''
    for i in range(num):
        tmp = choice(all_choice)
        result += tmp
    return result

if __name__ == '__main__':
    print(pas())