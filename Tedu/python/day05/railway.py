#coding:utf-8

import time

counter = 19
n = 0

print('*' * counter,end='')
while True:
    print('\r%s@%s' %('*' * n,'*' * (counter - n)),end='')
    n += 1
    time.sleep(0.3)
    if n == counter:
        n = 0

