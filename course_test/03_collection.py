# coding=utf-8

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # 含首不含尾 1到2
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists
print(list)  # +tinylist 没改变原来
print(list.extend(tinylist))  # None
list = sorted(list, key=lambda s: str(s))  # 排序
print(list)  # extend 后list改变

# 修改list中的元素
list[0] = "python"
list.append(['yyyy', 'zzzz'])   # 添加这个list为元素
list.extend(['angelababy', 66666])  # 追加成列表
del list[len(list)-1]
print(list)

print("""
tunple测试
""")
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # Prints complete tuple
print(tuple[0])  # Prints first element of the tuple
print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
print(tuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints tuple two times
print(tuple + tinytuple)  # Prints concatenated tuple
# tuple[1]=66666    #会报错，因为元组是不可变列表
print(tuple)

print("""
dictionary测试
""")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # Prints value for 'one' key
dict['one'] = "This is new one"
print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(dict)
print(tinydict)  # Prints complete dictionary

bdict = dict
bdict[2] = "This is b two"  # 值转递复制
print(dict)

cdict = dict.copy()
cdict[2] = "This is c two"  # 拷贝相同内容 非引用同值
print(cdict)
print(dict)

print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

print("""
set测试
""")
# 定义一个set：
a = {1, 1, 2, 3, 4, 5}  # 会去重
b = {'a', 'b', 1}
print(a)
print(a.remove(3))
print(a.add(6))
print(a.union(b))  # 会去重
