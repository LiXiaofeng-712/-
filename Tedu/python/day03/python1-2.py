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
#print(num)
isrunning = True
count = 0
while count < 5:
    answer = int(input('guess a number (1~100):'))
    if answer > num:
        print('猜大了！')
    elif answer < num:
        print('猜小了！')
    else:
        print('猜对了！')
        break
        isrunning = False
    count += 1
else:
    print('你输了，正确答案是：%d'%num)