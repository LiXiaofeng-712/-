#coding:utf-8

import pickle
import time
alist = [['date','zfb','wx','xj','balance']]
try:
    zfb = int(input('zfb:').strip())
    wx = int(input('wx:').strip())
    xj = int(input('xj:').strip())
except:
    print('error exit')
    exit()
else:
    sum = zfb + wx + xj
    blist = [time.strftime('%F'),zfb,wx,xj,sum]
    alist.append(blist)

def money(zfb,wx,xj):
    data = int(input('input money:').strip())



def show_menu():
    prompt = '''[0] counter
[1] exit
Please choice(0~1):'''
    while True:
        choice = input(prompt).strip()
        if choice == '1':
            print('\nBye!')
            break
    money(zfb,wx,xj)

if __name__ == '__main__':
    show_menu()