import random
#剪刀石头布小游戏
#电脑随机出拳，玩家自己决定
#列出所有选择，使用随机模块让电脑随机选择
all_choice = ['剪刀','石头','布']
compute = random.choice(all_choice)
#玩家选择出拳
player = input('请输入石头/剪刀/布：')
#玩家出剪刀
print('computer出:',compute,'player出',player)
if player == all_choice[0]:
    if compute == all_choice[0]:
        print('平局')
    elif compute == all_choice[1]:
        print('输')
    else:
        print('赢')
#玩家出石头
elif player == all_choice[1]:
    if compute == all_choice[0]:
        print('赢')
    elif compute == all_choice[1]:
        print('平局')
    else:
        print('输')
#玩家出布
else:
    if compute == all_choice[0]:
        print('输')
    elif compute == all_choice[1]:
        print('赢')
    else:
        print('平局')