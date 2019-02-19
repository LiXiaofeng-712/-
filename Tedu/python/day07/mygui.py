'''
    窗口程序提供三个按钮
    其中两个按钮的前景色均为白色，背景色为蓝色
    第三个按钮前景色为红色，背景色为红色
    按下第三个按钮后，程序退出
'''


#导入模块
import tkinter
from functools import partial

# def hello():
#     lb.config(text='Hello China')
#
# def welcome():
#     lb.config(text='Hello Tedu')

def say_hi(word):
    def greet():
        lb.config(text='Hello %s' % word)
    return greet

#定义windows句柄
window = tkinter.Tk()
#定义界面标签显示内容
lb = tkinter.Label(window,text='Hello world!')
#使用偏函数定义tkinter.Button函数
MyButton = partial(tkinter.Button,window,fg='white',bg='blue')
#定义三个按钮内容
b1 = MyButton(text='button 1',command=say_hi('China'))
b2 = MyButton(text='button 2',command=say_hi('Tedu'))
b3 = MyButton(text='button 3',command=window.quit) #选择3退出
#使用for循环安装3个按钮
for i in (lb,b1,b2,b3):
    i.pack()
#主程序方法，显示窗口
window.mainloop()