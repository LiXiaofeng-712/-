#!/usr/bin/env python3
import getpass
uname = input('请输入用户名：')
upass = getpass.getpass('请输入密码：')
if uname == 'bob' and upass == '123456':
    print('\033[32;1mLogin successful!\033[0m')
else:
    print('\033[32;1mLogin inorrect!\033[0m')
