#模拟cp
#将/bin/ls 作为源文件
#将/root/ls 作为目标文件
# with open('/bin/ls','rb') as s:
#     ls = s.read()
#     #print(ls)
#     with open('/root/ls','wb') as d:
#         d.write(ls)
#         d.close()
#     s.close()
#打开/bin/ls 作为源文件
f1 = open('/bin/ls','rb')
#打开/root/ls 作为目标文件
f2 = open('/root/ll','wb')
#重复的从源文件读取内容到目标文件，建议一点一点读
while True:
    data = f1.read(4096)
    #if data == '':
    if not data:
        break
    f2.write(data)
#关闭文件
f1.close()
f2.close()
