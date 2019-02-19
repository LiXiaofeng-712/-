import random
answer = random.randint(1,100)
time = 5
print('*************欢迎进入猜数小游戏*************')
while time > 0:
    guess = int(input('请输入1～100数字：'))
    time -= 1
    if 0 < guess < 100:
        if guess > answer:
            print('猜大了！')
            print('你还有%d次机会！'%time)
        elif guess < answer:
            print('猜小了！')
            print('你还有%d次机会！' % time)
        else:
            print('恭喜你，猜对了！')
            print('一共猜了%d次'%(5-time))
            break
    else:
        print('输入有误!')
print('游戏结束，正确答案是：{}'.format(answer))