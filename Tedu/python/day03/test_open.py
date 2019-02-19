# fobj = open('welcome.py','r')
# print(fobj)
# data = fobj.read(11)
# print(data)
# data = fobj.read(11)
# print(data)
# data = fobj.readline()
# print(data)
# print('*'*20)
# data = fobj.readlines()
# print(data)
# # fobj.write('Hello world\n')
# fobj.close()

# fobj = open('welcome.py')
# for i in fobj:
#     print(i,end='')
# fobj.close()

# fobj = open('welcome.py','w')
# fobj.write('hello')
# fobj.write(' world\n')
# fobj.writelines(['hello\n','world\n'])
# fobj.flush()
# fobj.close()

# fobj = open('welcome.py','w')
# fobj.writelines(['#!/usr/bin/env python3\n','print("hello world!")\n'])
# fobj.close()
# import os
# with open('mtable.py','a') as f:
#     f.tell()
#     f.seek(,0)
#     f.write('#!/usr/bin/env python3\n')
#     f.close()
#os.system('python3,mtable.py')

with open('welcome.py','r+') as f:
    old = f.read()
    f.seek(0,0)
    f.write('hello\n'+old)