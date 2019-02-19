import random

def block(fname):
    content = []
    count = 0
    for i in fname:
        content.append(i)
        count += 1
        if count == 10:
            yield content
            content.clear()
            count =0
    if content:
        yield content

if __name__ == '__main__':
    # nums = [random.randint(1,100) for i in range(10)]
    with open('/etc/passwd') as fobj:
        for i in block(fobj):
            print(i)
            print('*'*50)