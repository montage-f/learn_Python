# Created by MonTage_fz at 2019/7/12

# for 循环主要是用来循环遍历字典, 序列, 或者是集合
lis = ['小丽', '小芳', '小张', '小田']

for i in lis:
    print(i)

lis2 = ('小芳', '小张', '小李', '小花')
for i in lis2:
    print(i, end='')

lis3 = {1, 2, 3, 4, 5}

for i in lis3:
    print(i)
else:
    print('列表循环完成~')


lis3 = [1, 2, 3, 4, 5]
for i in lis3:
    if i % 2:
        continue
    print(i)
else:
    print(i)


lis4 = [1, 2, 3, 4, 5]
for i in lis3:
    if not (i % 2):
        break
    print(i)


