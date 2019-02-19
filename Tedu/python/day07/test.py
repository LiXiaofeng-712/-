# import hashlib
#
# m = hashlib.md5(b'12346')
# print(m.hexdigest())
#
# with open('/etc/passwd','rb') as f:
#     data = f.read()
#     m = hashlib.md5(data)
#     print(m.hexdigest())

#打印文件，每次10行

# def read_file(fname):
#     lines = []
#     count = 0
#     for i in fname:
#         lines.append(i)
#         count += 1
#         if count == 10:
#             yield lines
#             lines.clear()
#             count = 0
#     if lines:
#         yield lines
#
# if __name__ == '__main__':
#     with open('/etc/passwd') as f:
#         for i in read_file(f):
#             print(i)
#             print('*'*20)

# def block(fname):
#     content = []
#     count = 0
#     for i in fname:
#         content.append(i)
#         count += 1
#         if count == 10:
#             yield content
#             content.clear()
#             count = 0
#     if content:
#         yield content
#
# if __name__ == '__main__':
#     with open('/etc/shadow') as f:
#         for i in block(f):
#             print(i)
#             print('*'*20)

#装饰器
# def set_color(func):
#     def color():
#         return '\033[33;1m%s\033[0m' % func()
#     return color
#
# # @set_color
# def hello():
#     return 'hello'
#
# # @set_color
# def welcome():
#     return 'welcome'
#
# if __name__ == '__main__':
#     hello = set_color(hello)
#     print(hello())
#     welcome = set_color(welcome)
#     print(welcome())

#编写检查文件md5值的程序
# import hashlib
# import sys
#
# def check(fname):
#     m = hashlib.md5()
#     with open(fname,'rb') as f:
#         while True:
#             data = f.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     print(check(sys.argv[1]))

# import sys
# import hashlib
#
# def check(fname):
#     m = hashlib.md5()
#     with open(fname,'rb') as f:
#         while True:
#             data = f.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     print(check(sys.argv[1]))

#记账小程序
import random
import os
from time import strftime
from pickle import dump
from pickle import load

#初始化
def init_data(fname):
    data = [
        [strftime('%F'),0,0,10000,'init']
    ]
    with open(fname,'wb') as f:
        dump(data,f)

#收入
def save(fname):
    # while True:
    amount = int(input('金额：'))
    b = input('备注：').strip()
    with open(fname, 'rb') as f:
        alist = load(f)
    balance = alist[-1][-2] + amount
    with open(fname,'wb') as f1:
        alist.append([strftime('%F'),amount,0,balance,b])
        dump(alist,f1)


#支出
def cost(fname):
    amount = int(input('金额：'))
    b = input('备注：').strip()
    with open(fname, 'rb') as f:
        alist = load(f)
    balance = alist[-1][-2] - amount
    with open(fname, 'wb') as f1:
        alist.append([strftime('%F'), amount, 0, balance, b])
        dump(alist, f1)

#查询
def query(fname):
    with open(fname,'rb') as f:
        fread = load(f)
    print('%-14s%-10s%-10s%-12s%-20s'%('date','save','cost','balance','comment'))
    for i in fread:
        print('%-14s%-10s%-10s%-12s%-20s'%tuple(i))


#菜单
def show_menu():
    fname = '/tmp/account.txt'
    if not os._exists(fname):
        init_data(fname)
    cmds = {'0':save,'1':cost,'2':query}
    prompt = '''[0] 收入
[1] 支出
[2] 查询
[3] 退出
请选择：'''
    while True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            break
        except ValueError:
            continue
        if choice not in [str(i) for i in range(4)]:
            print('无效输入！')
            continue
        if choice == '3':
            print('\nBye')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
