#!/usr/bin/env python3
import string
import keyword

first_ch = string.ascii_letters + '_'
other_ch = string.ascii_letters + string.digits + '_'

def check(ch):
    if ch[0] not in first_ch:
        return '1st invalid'
    for ind,val in enumerate(ch[1:]):
        if val not in other_ch:
            return 'char in position %s invalid' %(ind+2)
    if not keyword.iskeyword(ch):
        return 'is keyword'
    return '%s is valid' %ch

if __name__ == '__main__':
    print(check('(hel'))
    print(check('he*l'))
    print(check('True'))
    print(check('hello'))