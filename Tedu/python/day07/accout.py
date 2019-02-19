#记账小程序

#coding:utf-8
import os
from time import strftime
import pickle

def init_data(fname):
    data = [
        [strftime('%F'),0,0,10000,'init']
    ]
    with open(fname,'wb') as fobj:
        pickle.dump(data,fobj)

def save(fname):
    while True:
    amount = int(input('金额：'))
    comment = input('备注：').strip()
    with open(fname,'rb') as fobj:
        record_list = pickle.load(fobj)
    balance = record_list[-1][-2] + amount
    with open(fname,'wb') as fobj:
        record_list.append([strftime('%F'),amount,0,balance,comment])
        pickle.dump(record_list,fobj)

def cost(fname):
    amount = int(input('金额：'))
    comment = input('备注：').strip()
    with open(fname, 'rb') as fobj:
        record_list = pickle.load(fobj)
    balance = record_list[-1][-2] - amount
    with open(fname, 'wb') as fobj:
        record_list.append([strftime('%F'),0,amount,balance,comment])
        pickle.dump(record_list,fobj)

def query(fname):
    with open(fname,'rb') as fobj:
        fread = pickle.load(fobj)
    print('%-14s%-10s%-10s%-12s%-20s'%('date','save','cost','balance','comment'))
    for record in fread:
        print('%-14s%-10s%-10s%-12s%-20s'%tuple(record) )

def show_menu():
    cmds = {'0':save,'1':cost,'2':query}
    fname = 'record.data'
    #判断文件不存在，调用初始化函数
    if not os.path.exists(fname):
        init_data(fname)
    prompt = '''[0] 记录收入
[1] 记录支出
[2] 查询
[3] 退出
请选择(0~3):'''
    while True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            choice = '3'
        if choice not in [str(i) for i in range(4)]:
            print('无效输入，请重新输入！')
            continue
        if choice == '3':
            print('\nBye')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
