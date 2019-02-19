#!/usr/bin/env python3
'''
程序接受用户输入
判断用户输入的标识符是否合法
用户输入的标识符不能使用关键字
有不合法字符，需要指明第几个字符不合法
'''
import string
import keyword

#定义首字符和其余字符
first_char = string.ascii_letters+'_'
other_char = string.ascii_letters+string.digits+'_'

#检查用户输入字符是否合法
def check_id(idt):
    #判断首字符是否合法
    if idt[0] not in first_char:
        return '1st invalid'
    #判断其余字符是否合法
    for ind,val in enumerate(idt[1:]):
        if val not in other_char:
            return 'char in position %s invalid' %(ind+2)
    #判断是否为关键字
    if keyword.iskeyword(idt):
        return 'is keyword'
    #以上都不满足,则为合法字符
    return '%s is vaild' %idt

#测试
if __name__ == '__main__':
    print(check_id('8hello'))
    print(check_id('hell+o'))
    print(check_id('hello'))
    print(check_id('True'))




