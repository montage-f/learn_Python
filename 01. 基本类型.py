# Number 数字类型

type(1)  # int
type(1.1)  # float
type(1 + 1.0)  # float
type(2 * 3)  # int
type(2 / 2)  # float
type(2 // 2)  # int

# bool 布尔类型
type(True)  # bool
type(False)  # bool
bool([])  # False
bool([1, 2, 3])  # True
bool({})  # False
bool({'a': 1})  # True
bool('')  # False
bool(None)  # False


# complex 复数

# str 字符串
# 在pyhton 中 用单引号, 双引号, 和三引号 来表示字符串
type('hello world')  # str
print('hello world\npython')

# 在字符串前面加上一个 r, 那么这个字符串就代表原始字符串
# 如果不加上 r,那么\n将会被转义
print(r'C:\nginx-1.16.0')

# 字符串操作
print('hello' + ' world')
print('hello ' * 3)
print('hello world'[0])
print('hello world'.split(' '))  # 将字符串以规定的符号分开,且返回成一个数组
print('hello world'[0:5])  # 截取字符串
print('hello world'[6:])
