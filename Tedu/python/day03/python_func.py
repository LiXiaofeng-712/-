#!/usr/bin/env python3
def mtable(num):
    for i in range(1, num+1):
        for j in range(1, i + 1):
            print('%sx%s=%s' % (j, i, j * i), end='\t')
            # print(str(j)+'x'+str(i)+'='+str(j*i),end='\t')
            # print('{0}x{1}={2}'.format(j,i,(i*j)),end='\t')
        print()
#mtable(9)

def fibs(num):
    fib = [0,1]
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])
    return fib
#print(fibs(10))

import sys
def cp(src,dst):
    '''cp(src,dst)
    src 源文件路径
    dst 目标文件路径'''
    f1 = open(src,'rb')
    f2 = open(dst,'wb')
    while True:
        data = f1.read(4096)
        if not data:
            break
        f2.write(data)
    f1.close()
    f2.close()
cp(sys.argv[1],sys.argv[2])