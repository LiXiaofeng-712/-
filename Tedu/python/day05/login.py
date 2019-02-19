
#coding:utf-8
import getpass
import subprocess
user = {}

def register():
    subprocess.call('clear')
    username = input('请输入用户名：')
    passwd = getpass.getpass('请输入密码：')
    if username in user:
        print('\033[31;1m用户%s以存在，注册失败！\033[0m' %username)
    else:
        user[username] = passwd

def login():
    subprocess.call('clear')
    username = input('请输入用户名：')
    passwd = getpass.getpass('请输入密码：')
    # if username in user and passwd == user[username]:
    if user.get(username) == passwd:
        print('\033[32;1m登陆成功！\033[0m')
    else:
        print('\033[31;1m登陆失败!\033[0m')

def show_menu():
    cmds = {'0':register,'1':login}
    prompt = '''[0]注册
[1]登陆
[2]退出 
请选择：'''
    while True:
        choice = input(prompt).strip()
        if choice not in ['0','1','2']:
            print('无效选择，请重试！')
            continue
        if choice == '2':
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()