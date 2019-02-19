# import time
# t = time.localtime()
# print(t)
# print(t.tm_year)
# print(t.tm_wday)
# print(time.time())
# print(time.ctime())
# print(time.sleep(0))
# print(time.strftime('%Y-%m-%d'))
# print(time.strftime('%F'))

# from datetime import datetime
# t = datetime.now()
# print(t)
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# import os
# print(os.getcwd())
# # os.mkdir('/tmp/mydemo')
# # os.listdir('/tmp/mydemo')
# # os.chdir('/tmp/mydemo')
# # os.mknod('abc.txt')
# # os.chmod('abc.txt',0o744)
#
# # print(os.path.islink('/etc/grub2.cfg'))
#
# # print(os.path.split('/etc/sysconfig/network-scripts/ifcfg-eth0'))
# print(os.path.dirname('/etc/sysconfig/network-scripts/ifcfg-eth0'))
# print(os.path.basename('/etc/sysconfig/network-scripts'))

# import pickle
# alist = ['egg','banana','apple']
# f = open('/tmp/shop','wb')
# pickle.dump(alist,f)
# f.close()
# f = open('/tmp/shop','rb')
# blist = pickle.load(f)
# print(blist[1])
# f.close()

# a = lambda x,y: x + y
# print(a(10,32))

# import random
# # def func(x):
# #     return x % 2
#
# if __name__ == '__main__':
#     nums = [random.randint(1,100) for i in range(10)]
#     print(nums)
#     # result = list(filter(lambda x: x % 2,nums))
#     # print(result)
#     # print(result)
#     result1 = list(map(lambda x:x * 2 + 1,nums))
#     print(result1)
#     print(result1)

x = 10
def add():
    global x
    x += 10
    print(x)
add()
print(x)