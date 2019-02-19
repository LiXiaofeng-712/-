'''
#!/usr/bin/env python3
import random
secret = random.randint(1,100)        #生成随机数
time = 5        #猜数字的次数
print("---------欢迎来到猜数字的地方，请开始---------")
while time > 0:
    guess = int(input("*数字区间0-100，请输入你猜的数字:"))
    print("你输入数字是：",guess)
    if 0 <= guess < 100:
        if guess == secret:
            print("猜对了，真厉害")
        else:
            print("太遗憾了，你猜错了，你还有",time-1,"次机会")
        time -= 1
    else:
        print("输入非法，请重新输入")
print("游戏结束，正确的结果是：",secret)

'''

import random

num = random.randint(1, 100)
counter = 0
while counter < 5:
    answer = int(input('guess the number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:  # 循环被break就不执行了，没有被break才执行
    print('the number is:', num)




