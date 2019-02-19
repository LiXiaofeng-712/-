#coding:utf-8
#列表模拟栈结构
#栈：先进后出的结构,后出先进结构
# import os
import subprocess

stack = []
#压栈功能
def push_it():
    subprocess.call('clear')
    data = input('data to push:').strip()
    if data:
        stack.append(data)
        print('\033[31;1msucessful!\033[0m')

#出栈功能
def pop_it():
    subprocess.call('clear')
    if stack:
        print('from stack popped \033[31;1m%s\033[0m' %stack.pop())
    else:
        print('\033[31;1mEmpty stack!\033[0m')

#查询功能
def view_it():
    subprocess.call('clear')
    print('\033[32;1m%s\033[0m' %stack)

#菜单功能
def show_menu():
    cmds = {'0':push_it,'1':pop_it,'2':view_it}
    alist = ['0','1','2','3']
    prompt = '''[0] push
[1] pop
[2] view
[3] quit
Please input your choice (0/1/2/3):'''
    while True:
        choice = input(prompt).strip()
        if choice not in alist:
            subprocess.call('clear')
            print('Invalid choice.Try again!')
            continue
        if choice == '3':
            break

        cmds[choice]()
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()


if __name__ == '__main__':
    show_menu()