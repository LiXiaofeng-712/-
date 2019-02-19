#!/usr/bin/env python3
username = input('username: ')
password = input('password: ')
if username == 'bob':
    if password == '123456':
        print('Login successful')
    else:
        print('Login incorrect')
else:
    print('Login incorrect')
