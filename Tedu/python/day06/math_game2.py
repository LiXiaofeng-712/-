#coding:utf-8
import random

# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x - y

def exam():
    cmds = {'+':lambda x,y: x + y,'-':lambda x,y: x - y}
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' %(nums[0],op,nums[1])
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:     #except为空表示匹配所有异常,不推荐
            print()
            continue
        if answer == result:
            print('\nVery good!')
            break
        # else:
        print('\nWrong answer!')
        counter += 1
    else:
        print('%s%s' %(prompt,result))

def main():
    while True:
        exam()
        try:
            yn = input('Contine(y/n)?').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            yn = 'n'
        if yn in 'nN':
            print('\nByeBye!')
            break

if __name__ == '__main__':
    main()