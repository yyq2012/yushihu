# 练习 2 百分制成绩转为等级制
# 90分以上    --> A
# 80分~89分    --> B
# 70分~79分	   --> C
# 60分~69分    --> D
# 60分以下    --> E

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('您的成绩为 %s' % grade)