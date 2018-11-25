# coding=utf-8
import numpy as np

print("""
===numpy.array===""")
print(np.array([1, 2, 3, 4]))

print(np.array((1.2, 2, 3, 4)))
print()

x = np.array(((1, 2, 3), (4, 5, 6)))
print(x)
print(x[1, 2])
print()

y = x[:, 1]  # y取值为 x第二列
print(y)
y[0] = 10
print(y)
print(x)  # y取了x的值后，改变y会改变x的那个值

print("""
===numpy.arange===""")

print(np.arange(15))  # numpy.ndarray
print(np.arange(15).reshape(3, 5))  # reshape变3行5列
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print()

print(np.linspace(1, 10, 20))  # 在从1到10中产生20个数：
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.eye(3))  # 单位矩阵(E矩阵)

print("""
===获取数组的属性===""")

a = np.zeros((2, 2, 2))
print(a)
print(a.ndim)  # 数组的维数
print(a.shape)  # 数组每一维的大小
print(a.size)  # 数组的元素数
print(a.dtype)  # 元素类型

print("""
===数组的加减运算===""")
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a - b)

a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))  ##生成2*3矩阵，元素为[0,1)范围的随机数
a *= 3
print(a)
b += a  # a+= b 会报错
print(b)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)  # 在从0到pi中产生3个数：
print(a + b)

print("""
===数组乘法运算===""")
b = np.arange(4)
print(b ** 2)  # 平方
print(a)
print(10 * np.sin(a))

print("""
===数组内部运算===""")
print(np.array(((0, 1), (0, 5))))
print(np.sum([[0, 1], [0, 5]]))

print(np.sum([[0, 1], [0, 5]], axis=0))  # 0表示将x轴平行的行叠加
print(np.sum([[0, 1], [0, 5]], axis=1))  # 1表示将y轴平行的列叠加
print()

b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0))  # 0表示将x轴平行的行叠加的和

print(b.cumsum(axis=1))  # 1表示将y轴平行的列的累积和
print(b.min(axis=1))  # 1表示将y轴平行的列的最小值

print("""
===三维数组===""")
x = np.array([[[0, 1, 2],
               [3, 4, 5],  # a
               [6, 7, 8]],

              [[9, 10, 11],
               [12, 13, 14],  # b
               [15, 16, 17]],

              [[18, 19, 20],
               [21, 22, 23],  # c
               [24, 25, 26]]])
print(x.sum(axis=0))  # abc 第一/二/三行相加
print(x.sum(axis=1))  # a/b/c sum(axis=0)
print(x.sum(axis=2))  # a/b/c sum(axis=1)

print("""
===数组的索引、切片===""")
a = np.arange(10) ** 3  # 记住，操作符是对数组中逐元素处理的！
print(a)
print(a[2:5])  # 2索引到4索引，不包含第5
print()

a[:6:2] = -1000  # 等同于a[0:6:2]= -1000，从开始到第6个位置，每隔一个元素将其赋值为-1000
print(a)
print(a[::-1])  # 反转a
for i in a:
    print(i ** 2, end=',')

print(""" 

===多维数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出。===""")
def f(row, column):
    return 10 * row + column
b= np.fromfunction(f,(5,4),dtype=int)   # 5行4列 元素按方法赋值
print(b)
""" 几行,几列"""
print(b[0:5, 1])  # 0到4行 1列
print(b[:, 1])  # 与上同 全部行，1列
print(b[1:3, :])  # 1,2行，全部列
print()
print(b[-1])  # 最后一行，等同于b[-1,:]，-1是第一个轴，而缺失的认为是：，相当于整个切片。
print(b[:, -1])  # 全部行，最后一列

for element in b.flat:  # flat 对数组中每个元素都进行处理
    print(element, end=' ')

print("""

===合并数组===""")
a = np.ones((2, 2))
b = np.eye(2)
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print()

c = np.hstack((a, b))
a[1, 1] = 5
print(c)  # 说明了是深拷贝
b = a
print(b is a)
c = a.copy()
print(c is a)

print("""
===矩阵转置运算===""")
a = np.array([[1,0],[2,3]])
print(a)
print(a.transpose())

print("""
===reshape更改数组的形状===""")
a = np.floor(10 * np.random.random((3, 4)))
print(a)
print(a.shape)
print()

print(a.ravel()) # 平坦化数组
a.shape= (6, 2)
print(a)
print(a.transpose())

print("""
===resize更改数组形状===""")
print(a)
a.resize((2,6)) #改变原矩阵
print(a)
print(a.reshape((2,6))) # 得到新矩阵 不改变原矩阵
