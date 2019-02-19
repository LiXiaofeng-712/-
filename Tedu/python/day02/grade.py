#判断成绩
#60 及格 70 良 80 好 90 优秀 否则 需要努力

#获取用户输入的成绩
score = int(input('请输入成绩：'))
#判断用户成绩
if score >= 90 :
    print('优秀')
elif score >= 80 :
    print('好')
elif score >= 70 :
    print('良')
elif score >= 60 :
    print('及格')
else :
    print('继续努力！')