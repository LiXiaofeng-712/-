# def mygen():
#     yield 'hello world'
#     a = 10 + 320
#     yield a
#     yield [1,2,3]
# a = mygen()
# for i in a:
#     print(i)

def block(fname):
    content = []
    count = 0
    for lines in fname:
        content.append(lines)
        count += 1
        if count == 10:
            yield content
            content.clear()
            count = 0
    if content:
        yield content


if __name__ == '__main__':
    with open('/etc/passwd') as fobj:
        for lines in block(fobj):
            print(lines)
            print('*'*40)