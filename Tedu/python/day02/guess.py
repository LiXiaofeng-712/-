#猜数字游戏
#随机生成一个数字，用户猜数字，提示猜大了/猜小了/猜对了
import random
answer = random.randint(1,100)
print(answer)
n = 1
while n <= 5:
    num = int(input("guess is num(1~100):"))
    if answer > num:
        print('猜小了')
    elif answer < num:
        print('猜大了')
    else:
        print('猜对了')
        break
    n += 1
print('正确答案：%d'%answer)