# def say():
#     print('hello')
#
# say()

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
# cp('/etc/passwd','/root/passwd')

def mysum(num1,num2):
    return num1 + num2
# sum = mysum(3,4)
# print(sum)
print(mysum(4,5))

def sum(num=20):
    print('*'*num)
sum()