'''
if ' ' :
    print('yes')
else:
    print('no')

x,y = 3,4
a = x if x < y else y
print(a)

if x < y:
    print(x)
else:
    print(y)
'''

import random
num = random.randint(1,100)
print(num)
isrunning = True
count = 5
print('**********猜数小游戏！！！**********')
while isrunning:
    count -= 1
    print('\t\t\t第{}局\t\t\t'.format(5-count))
    answer = int(input('\tguess a number (1~100):'))
    if count == 0:
        print('你输了！')
        print('正确答案是：%d'%num)
        isrunning = False
    else:
        if answer > num:
            print('\t猜大了！')
            print('\t还有',count,'次机会！')
        elif answer < num:
            print('\t猜小了！')
            print('\t还有',count,'次机会！')
        else:
            print('\t猜对了！')
            isrunning = False

