# coding=utf-8

str = 'HelloWorld!'    #字符串在python中本质上是一个字符序列Seq

print(str)  # 打印整个字符串
print(str[0])  # 打印字符串第一个字母 H
print(str[2:5])  # 打印第3到第5个字母,含首不含尾 llo
print(str[2:])  # 打印从第3个字母到末尾    lloWorld!
print(str[:2])  # 打印从头部到第3个字母,含首不含尾  He
print(str * 2)  # 字符串重复2次
print(str + "TEST")  # 字符串拼接
