#使用列表生成斐波那契数列
fib = [0,1]
#for i in range(8):
#    a = fib[-1]
#    b = fib[-2]
#    temp = a + b
#    fib.append(temp)
#print(fib)

#for i in range(8):
#    fib.append(fib[-1]+fib[-2])
#print(fib)

ulen = int(input('请输入斐波那契数列长度：'))
for i in range(ulen-2):
    fib.append(fib[-1] + fib[-2])
print(fib)

print(len(fib))