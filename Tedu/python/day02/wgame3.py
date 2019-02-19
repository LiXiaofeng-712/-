'''
#!/usr/bin/env python3
import random

i = 1  # 游戏次数
win = 0  # 赢局次数
while i <= 3:
    # 1. 提示并获取用户的输入
    player = int(input("请输入 0剪刀 1石头 2布:"))

    # 2. 让电脑出一个随机数
    computer = random.randint(0, 2)
    # 让用户输入合法
    if player == 0 or player == 1 or player == 2:
        # 3. 判断用户的输入,然后显示对应的结果
        if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            print("第" + str(i) + "局" + "赢了")
            win += 1
        elif player == computer:
            print("第" + str(i) + "局" + "平局")
        else:
            print("第" + str(i) + "局" + "输了")
        i += 1
    else:
        print("请重新输入合法数字")
# 4. 判断最终猜拳结果：3局两胜
if win >= 2:
    print("恭喜，你赢了！！")
else:
    print("你输了！！")
'''

import random

all_choices = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
cwin = 0
pwin = 0
while cwin < 2 and pwin < 2:
    computer = random.choice(all_choices)
    ind = int(input(prompt))
    player = all_choices[ind]
    print("Your choice: %s, Computer's choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')

