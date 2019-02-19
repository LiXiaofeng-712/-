#求1～100之间整数的累加


count = 0
sum100 = 0
while count < 100:
    count += 1
    sum100 += count
print(sum100)

#求1～100之间所有偶数的和
count = 0
sum100 = 0
while count < 100:
    count += 1
    #if count % 2 == 0:
    if count % 2 == 1:
        continue
    sum100 += count
print(sum100)
