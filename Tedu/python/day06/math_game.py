#coding:utf-8
import random

def exam():
    nums = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    if op in '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    prompt = '%s %s %s = ' %(nums[0],op,nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('\nVery good!')
    else:
        print('\nWrong answer!')

def main():
    while True:
        exam()
        yn = input('Contine(y/n)?').strip()[0]
        if yn in 'nN':
            print('\nByeBye!')
            break

if __name__ == '__main__':
    main()


