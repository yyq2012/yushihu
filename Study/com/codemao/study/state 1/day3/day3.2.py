# 练习1 用骰子决定干什么

from random import randint

num = randint(1, 6)
if num == 1:
    result = '唱个歌'
elif num == 2:
    result = '跳个舞'
elif num == 3:
    result = '学狗叫'
elif num == 4:
    result = '学猫叫'
elif num == 5:
    result = '讲笑话'
else:
    result = '念绕口令'
# print(result)
print('%d %s' % (num, result))
