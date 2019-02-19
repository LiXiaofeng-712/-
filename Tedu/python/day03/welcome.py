
#斐波那契数列
# def fib(num):
#     f = [0,1]
#     for i in range(num - 2):
#         # d = f[-1] + f[-2]
#         # f.append(d)
#         # print(d)
#         f.append(f[-1]+f[-2])
#     print(f)
#
# fib(10)
#
# #九九乘法表
# def mtable(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print('%sx%s=%s' %(j,i,j*i),end='\t')
#         print()
# mtable(9)
#
# #模拟cp操作
# import sys
# def copy(src_path,dst_path):
#     f1 = open(src_path, 'rb')
#     f2 = open(dst_path, 'wb')
#     while True:
#         #with open(src_path,'rb') as f1:
#         data = f1.read(4096)
#         if not data:
#             break
#         #with open(dst_path,'wb') as f2:
#         f2.write(data)
#     f2.close()
#     f1.close()
# copy(sys.argv[1],sys.argv[2])

#猜数程序
# def guess():
#     import random
#     rand = random.randint(1,100)
#     while True:
#         play = int(input('Please input a number(1~100):'))
#         if play > rand:
#             print('dale')
#         elif play < rand:
#             print('xiaole')
#         else:
#             print('duile')
#             break
# guess()

#判断合法用户
# def login():
#     user = input('user:')
#     pas = input('pass:')
#     if user == 'bob' and pas == '123456':
#         print('Login successful')
#     else:
#         print('Login inorrect')
# login()

#编写判断成绩的程序
# def grade():
#     score = int(input('score:'))
#     if score > 90:
#         print('youxiu')
#     elif score > 80:
#         print('hao')
#     elif score > 70:
#         print('liang')
#     elif score > 60:
#         print('jige')
#     else:
#         print('bujige')
# grade()

#编写石头剪刀布小游戏
# def game():
#     import random
#     all = ['shitou','jiandao','bu']
#     win = [['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
#     promte = '''
#     [0]shitou
#     [1]jiandao
#     [2]bu
#     Please choice:'''
#     comp = random.choice(all)
#     ind = int(input(promte))
#     play = all[ind]
#     print('comp is:%s,play is:%s' %(comp,play))
#     if play == comp:
#         print('pingju')
#     elif [play,comp] in win:
#         print('yingle')
#         #break
#     else:
#         print('shule')
# game()

#完善石头剪刀布小游戏
# def game():
#     import random
#     all = ['shitou','jiandao','bu']
#     win = [['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
#     promte = '''
#     [0]shitou
#     [1]jiandao
#     [2]bu
#     Please choice:'''
#     count_c = 0
#     count_p = 0
#     isrunning = True
#     while isrunning:
#         if count_c < 2 and count_p < 2:
#             comp = random.choice(all)
#             ind = int(input(promte))
#             play = all[ind]
#             print('comp is:%s,play is:%s' %(comp,play))
#             if play == comp:
#                 print('pingju')
#             elif [play,comp] in win:
#                 print('yingle')
#                 count_p += 1
#                 #isrunning = False
#             else:
#                 print('shule')
#                 count_c += 1
#         elif count_c == 2:
#             print('comp is win')
#             isrunning = False
#         else:
#             print('play is win')
#             isrunning = False
# game()

def game():
    import random
    all = ['shitou','jiandao','bu']
    win = [['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
    promte = '''
    [0]shitou
    [1]jiandao
    [2]bu
    Please choice:'''
    count_c = 0
    count_p = 0
    isrunning = True
    while isrunning:
        if count_c < 2 and count_p < 2:
            comp = random.choice(all)
            ind = int(input(promte))
            play = all[ind]
            print('comp is:%s,play is:%s' %(comp,play))
            if play == comp:
                print('pingju')
            elif [play,comp] in win:
                print('yingle')
                count_p += 1
                #isrunning = False
            else:
                print('shule')
                count_c += 1
        elif count_c == 2:
            print('comp is win')
            isrunning = False
        else:
            print('play is win')
            isrunning = False

# print('hello-'+'how-are-you')
# name1 = [1,2,3,4]
# name2 = name1
# name3 = name1[:]
# name2[0] = 5
# name3[1] = 6
# print(name1,name2,name3)

# x = 1
# x = x + 2.5
# print(x)
