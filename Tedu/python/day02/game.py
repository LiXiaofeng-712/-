#剪刀石头布小游戏
#定义石头，剪刀，布
game = ('石头','剪刀','布')
#获取玩家输入数字
sdict = {1:game[0],2:game[1],3:game[2]}
print('1--石头')
print('2--剪刀')
print('3--布')
num = int(input('请在1-3之间选择：'))
#电脑随机出拳，导入随机模块
import random
rand = random.randint(1,3)
#判断
print('电脑出',sdict[rand],'玩家出',sdict[num])
if rand == 1:
    if num == 1:
        print('平局！')
    elif num == 2:
        print('电脑获胜！')
    elif num == 3:
        print('玩家获胜！')
elif rand == 2:
    if num == 1:
        print('玩家获胜！')
    elif num == 2:
        print('平局！')
    elif num == 3:
        print('电脑获胜！')
elif rand == 3:
    if num == 1:
        print('电脑获胜！')
    elif num == 2:
        print('玩家获胜！')
    elif num == 3:
        print('平局！')
