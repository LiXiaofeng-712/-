#!/usr/bin/env python3
#coding:utf-8
'''
编写一个程序，要求用户输入文件名
如果文件已存在，要求用户重新输入
提示用户输入数据，每行数据先写到列表中
将列表数据写入到用户输入的文件名中
'''

import os
def get_fname():
    while True:
        fname = input('Please input filename:')
        if not os.path.exists(fname):
            break
        print('file is exists! Please try again!')
    return fname

def get_data():
    print('请输入数据，输入end结束！')
    content = []
    while True:
        data = input('>>>')
        if data == 'end':
            break
        #content.append(data+'\n')
        content.append(data)
    return content

def write_file(fname,data):
    with open(fname,'w') as f:
        f.writelines(data)

if __name__ == '__main__':
    fname = get_fname()
    #data = get_data()
    data = [line+'\n' for line in get_data()]
    print(fname)
    print(data)
    write_file(fname,data)

