import random
choice = ['剪刀','石头','布']
win = [['剪刀','布'],['石头','剪刀'],['布','石头']]
comp_num = 0
play_num = 0
tmp = '''[0]剪刀
[1]石头
[2]布
请选择(0/1/2)：
'''
count = 1
while 1:
    print('第%d局！'%count)
    computer = random.choice(choice)
    ind = int(input(tmp))
    player = choice[ind]
    print('computer choice:', computer, 'player choice:', player)
    if player == computer:
        print('平局！')
    elif [player,computer] in win:
        print('You Win！')
        play_num += 1
        if play_num >= 2:
            print('恭喜你赢了!')
            break
    else:
        print('You Lose！')
        comp_num += 1
        if comp_num >= 2:
            print('你输了!')
            break
    count += 1