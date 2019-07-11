# + 表示连接, * 表示重复

lists = ['a', 'b', 'c', 'd']
tinyList = [123, 'runoob']
print(lists)
print(lists[0])
print(lists[1:3])
print(lists[2:])
print(tinyList * 2)
print(tinyList + lists)


def reverse_words(inputs: str = ''):
    input_words = inputs.split(' ')
    input_words = input_words[-1::-1]
    return ' '.join(input_words)


if __name__ == "__mina__":
    input_i = 'i like python'
    rw = reverse_words(input_i)
    print(rw)

a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a + b
