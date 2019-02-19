#九九乘法表
#range函数，顾头不顾尾，结尾+1
for i in range(1,10):
    for j in range(1,i+1):
        print('%sx%s=%s'%(j,i,j*i),end='\t')
        #print(str(j)+'x'+str(i)+'='+str(j*i),end='\t')
        #print('{0}x{1}={2}'.format(j,i,(i*j)),end='\t')
    print()

