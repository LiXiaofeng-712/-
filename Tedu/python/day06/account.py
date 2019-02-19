#coding:utf-8
import time
import pickle

get_time = time.strftime('%F')
alist = [['时间','收入','支出','余额','备注']]
def init():
    f = open('/tmp/account.txt','wb')
    data = [get_time,0,0,10000,'初始化']
    alist.append(data)
    pickle.dump(alist,f)
    f.close()

def income():
    Money_data = int(input('收入金额：').strip())
    Desc_data = input('备注：').strip()
    balance = int(alist[-1][-2]) + Money_data
    blist = [get_time, Money_data, 0, balance, Desc_data]
    alist.append(blist)
    if Money_data:
        if Desc_data:
            with open('/tmp/account.txt','rb') as f1:
                a = pickle.load(f1)
            with open('/tmp/account.txt','wb') as f2:
                pickle.dump(a,f2)
                pickle.dump(blist,f2)


def pay():
    Money_data = int(input('支出金额：').strip())
    Desc_data = input('备注：').strip()
    balance = int(alist[-1][-2]) - Money_data
    blist = [get_time, 0, Money_data, balance, Desc_data]
    alist.append(blist)
    if Money_data:
        if Desc_data:
            with open('/tmp/account.txt','rb') as f1:
                a = pickle.load(f1)
            with open('/tmp/account.txt','wb') as f2:
                pickle.dump(a,f2)
                pickle.dump(blist,f2)

def select():
    f = open('/tmp/account.txt','rb')
    while True:
        try:
            show = pickle.load(f)
            print(show)
        except:
            break

def show_menu():
    cmds = {'0':income,'1':pay,'2':select}
    prompt = '''[0] 记录收入
[1] 记录支出
[2] 查询账本
[3] 退出
请选择(0~3)：'''
    while True:
        try:
            choice = input(prompt).strip()
        except:
            choice = '3'
        if choice == '3':
            print('\nBye!')
            break
        cmds[choice]()



if __name__ == '__main__':
    init()
    show_menu()
    print(alist)