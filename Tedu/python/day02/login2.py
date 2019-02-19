'''
#测试用户的输入正确显示登陆成功，否则登陆失败
user=input('请输入用户名:')
passwd=input('请输入密码:')
if user == '' or passwd == '':
    print('请输入正确的用户和密码！')
    exit
elif user == 'bob' and passwd == '123456':
    print('Login successful')
else:
    print('Login inorrect')
'''

'''
#判断成绩的小测试
grade = int(input('请输入成绩：'))
if grade > 90:
    print('优秀！')
elif grade > 80:
    print('好！')
elif grade > 70:
    print('良！')
elif grade > 60:
    print('及格！')
else:
    print('你要努力了！')
'''

'''
#测试单独元素返回值为False的元素
if 0 or '' or (0+0j) or () or [] or {}:
    print('yes')
else:
    print('no')

#单独元素的判断
if 10:
    print('yes')
else:
    print('no')
'''

import random
print(random.randint(1,3))