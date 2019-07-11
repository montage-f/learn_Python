# Created by MonTage_fz at 2019/7/11
# https://docs.python.org/zh-cn/3/tutorial/controlflow.html
words = ['cat', 'lad', 'dog', 'rat', 'window']
for w in words:
    print(w, len(w))

# 通过拷贝, 然后循环副本
# 如果写成 for w in words:，这个示例就会创建无限长的列表，一次又一次重复地插入 window。
for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)

print(words)
