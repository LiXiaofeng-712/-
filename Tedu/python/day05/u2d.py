#coding:utf-8

'''
Windows文本文件的行结束标志是\r\n
类unix文本文件的行结束标志是\n
编写程序，将unix文本文件格式转换为windows文本文件的格式
'''

import sys

def unxin2doc(fname):
    dst_fname = fname + '.txt'
    with open(fname) as src_fobj:
        with open(dst_fname,'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip('\n\r ') + '\r\n'
                dst_fobj.write(line)


if __name__ == '__main__':
    unxin2doc(sys.argv[1])