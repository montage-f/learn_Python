# Created by MonTage_fz at 2019/7/12

# 两个常见的循环 1. while 2. for

# 计算0~99以内基数的和
count = 0
sum = 0
while sum <= 99:
    sum += 1
    if sum % 2 != 0:
        count += sum

print(count)  # 2500


# 计算0~99以内偶数的和
i = 0
j = 100
while j > 0:
    i += j
    j -= 2

print(i)  # 2550



#  while 与 else 连用

a=1
while a < 10:
    a += 1
else:
    print('循环执行结束!')

# 在递归算法中, 使用while循环比较合适