#!/usr/bin/env python3
#导入随机模块
import random

#定义列表
all = ['剪刀','石头','布']
#定义玩家获胜的列表
win = [['剪刀','布'],['石头','剪刀'],['布','石头']]

#定义用户显示窗口
tem = '''[0]剪刀
[1]石头
[2]布
请选择(0/1/2):
'''
n = 1
play_num = 0
comp_num = 0
while 1:
    print('*********第%d句*********'%n)
    #电脑随机生成剪刀石头布
    comp = random.choice(all)
    #print(comp)
    ind = int(input(tem))
    #获取用户选择
    play = all[ind]
    #print(play)
    print('play:{0},comp:{1}'.format(play,comp))
    #当comp和play相等时，平局
    if play == comp :
        print('平局!')
    #若在win中存在表示玩家获胜
    elif [play,comp] in win :
        print('第%d局，你赢了！'%n)
        play_num += 1
        if play_num >= 2:
            print('恭喜！你赢了！')
            break
    else:
        print('第%d局，你输了！'%n)
        comp_num += 1
        if comp_num >= 2:
            print('很可惜，你输了！')
            break
    n += 1
