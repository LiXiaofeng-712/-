'''
    随机生成10个数字
    利用递归，实现快速排序
'''

import random

#快速排序
# def sort(seq):
#     if len(seq) < 2:
#         return seq
#
#     middle = seq[0]
#     smaller = []
#     larger = []
#     for i in seq[1:]:
#         if middle > i:
#             smaller.append(i)
#         else:
#             larger.append(i)
#     return sort(smaller) + [middle] + sort(larger)

#冒泡排序
def sort(seq):
    count = len(seq)
    for i in range(0,count):
        for j in range(i+1,count):
            if seq[i] > seq[j]:
                seq[i],seq[j] = seq[j],seq[i]
    return seq


if __name__ == '__main__':
    nums = [random.randint(1,100) for i in range(10)]
    print(nums)
    print(sort(nums))