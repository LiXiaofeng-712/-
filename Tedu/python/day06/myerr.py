#coding:utf-8
try:
    num = int(input('数字：'))
    result = 100 / num

except (ValueError,ZeroDivisionError):
    print('无效输入！')
# except ZeroDivisionError:
#     print('无效输入')
except (EOFError,KeyboardInterrupt):
    print('\n手动退出')
    exit()
# except KeyboardInterrupt:
#     print('\n退出')
#     exit()
else:
    print(result)
finally:
    print('Done')

# def set_age(name,age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超过范围')
#     print('%s is %s years old' %(name,age))
#
# def set_age1(name,age):
#     assert 0 < age < 120,'年龄超过范围'
#     print('%s is %s years old' %(name,age))
#
# if __name__ == '__main__':
#     # set_age('刘欢',244)
#     set_age1('bob',244)