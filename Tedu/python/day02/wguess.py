import random
answer = random.randint(1,100)
count = 0
while count <= 5:
    u_num = int(input('请输入1～100之间的数字：'))
    if u_num > answer:
        print('猜大了！')
    elif u_num < answer:
        print('猜小了！')
    else:
        print('恭喜你，猜对了')
        break
    count += 1
print('正确答案是%d'%answer)