# Created by MonTage_fz at 2019/7/12
for a in range(0, 10):
    print(a)


a = list(range(0, 10))
print(a)

for a in range(0, 10, 2):
    print(a, end=' | ')


for a in range(10, 0, -2):
    print(a, end=' | ')


a = list(range(0, 10))

for i in a:
    if not i % 2:
        print(i)


for i in a:
    if i % 2:
        print(i)

# 取出下面列表中的基数
i = ['神', 2, '奇', 4, '女', 6, '侠', 8, 9]

for j in range(0, len(i), 2):
    print(i[j], end=' | ')


b = i[0:len(i):2]
print(b)
