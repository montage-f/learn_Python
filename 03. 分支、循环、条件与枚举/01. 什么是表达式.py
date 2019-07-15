# Created by MonTage_fz at 2019/7/12

# 表达式(Expression) 是运算符(operation) 和操作数(operand) 所构成的"序列"
# 序列是有顺序的,
# 多个,且没顺序是不能称为序列的


# 将字符串1转换成int类型
c = int('1') + 2
print(c)

a = 1
b = 2
c = 3
print(a + b * c)

print(a and b or c)
print((a or b) and c)

# 先算not, 再算and, 最后算or
