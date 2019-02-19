def set_color(func):
    def color():
        return '\033[31;1m%s\033[0m' % func()
    return color

def hello():
    return 'Hello World!'

@set_color
def welcome():
    return 'Hello China'



if __name__ == '__main__':
    a = set_color(hello)
    print(a())
    # b = set_color(welcome)
    # print(b())