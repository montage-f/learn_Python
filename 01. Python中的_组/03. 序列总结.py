# Created by MonTage_fz at 2019/7/12

# str,list, tuple  可以称为序列

'hello world'[1]

[1, 2, 3][1]

(1, 2, 3)[1]

'hello world'[6:]

[1, 2, 3, 4, 5, 6][2:]

(1, 2, 3, 4, 5, 6)[2:]

# 判断 3 是否在 一个序列里面
3 in [1, 2, 3, 4, 5, 6]
# 判断 3 是否不在 一个序列里面
3 not in [1, 2, 3, 4, 5, 6]

'w' in 'hello world'

'w' not in 'hello world'

1 in (1, 2, 3)

1 not in (1, 2, 3)

# 序列的长度
len([1, 2, 3, 4, 5, 6])
len('hello world')
len((1, 2, 3))

# 序列的最大值

max([1, 2, 3, 4, 5, 6])
max('hello world')
max((1, 2, 3))

# 序列的最小值


min([1, 2, 3, 4, 5, 6])
min('hello world')
min((1, 2, 3))

# 将字符串转换成编码
ord('w')
ord('d')
ord(' ')
