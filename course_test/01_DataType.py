# coding=utf-8

# 基本使用
counter = 100  # 整型
miles = 1000.0  # 浮点
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

# 多重赋值
a = b = c = 1
d, e, f = 1, 2, "john"


a = tuple(range(1, 10, 2))
print(a)

b = tuple("hello")
print(b)

c = complex(1, -2)
print(c)
# 1 - 4j + 2j**2(-4)
print(c ** 2)

x = 1
e = eval('x+1')  # 不是 11
print(e)

f = dict([(1, 2), (3, 4), ('a', 100)])
print(f)
