'''
#!/usr/bin/env python3
import random
#1. 提示并获取用户的输入
player = int(input("请输入 0剪刀 1石头 2布:"))
#2. 让电脑出一个随机数
computer = random.randint(0,2)
#3. 判断用户的输入,然后显示对应的结果
#if 玩家获胜的条件:
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print("赢了,,,,可以去买奶粉了.....")
#elif 玩家平局的条件:
elif player==computer:
    print("平局了,,,洗洗手决战到天亮....")
else:
    print("输了,,,回家拿钱 再来....")
'''

'''
import random

computer = random.choice(['石头', '剪刀', '布'])
player = input('请出拳(石头/剪刀/布)：')
# print('您出了:', player, '计算机出的是:', computer)
print('您出了: %s, 计算机出的是: %s' % (player, computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('You WIN!!!')
    else:
        print('You LOSE!!!')
elif player == '剪刀':
    if computer == '石头':
        print('You LOSE!!!')
    elif computer == '剪刀':
        print('平局')
    else:
        print('You WIN!!!')
else:
    if computer == '石头':
        print('You WIN!!!')
    elif computer == '剪刀':
        print('You LOSE!!!')
    else:
        print('平局')
'''


import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2)：'''
computer = random.choice(all_choices)
ind = int(input(prompt))
player = all_choices[ind]
print('您出了: %s, 计算机出的是: %s' % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
