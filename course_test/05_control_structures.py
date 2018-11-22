# coding=utf-8

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
# if的条件可以是数字或字符串或者布尔值True和False（布尔表达式）
# 如果是数字，则只要不等于0，就为true
# 如果是字符串，则只要不是空串，就为true

print ("""
if else""")
var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)

print ("""
嵌套if else""")
var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
elif var < 50:
    print("Expression value is less than 50")
else:
    print("Could not find true expression")

print ("""
 while循环""")
count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

print ("""
 for循环""")
# 求素数
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, i, j))
            break

    else:
        print(num, 'is a prime number')

print
# 遍历集合
r = range(10, 15)  # list
print(r)
for num in r:
    print(num),

r = {1, 2, 3, 4, 5, 5}  # set类型
print(r)
for num in r:
    print(num),

r = ["aaa", 3, "c"]  # list
print(r)
for num in r:
    print(num),

r = {"a": 9, "b": 10}  # dict
print(r)
for num in r.values():
    print(num),

print ("""

 斐波那契数列""")
a = 0
b = 1
while b < 1000:
    print(b),
    a, b = b, a + b

print

# 递归方式实现 生成前20项
lis = []
for i in range(20):
    if i == 0 or i == 1:  # 第1,2项 都为1
        lis.append(1)
    else:
        lis.append(lis[i - 2] + lis[i - 1])  # 从第3项开始每项值为前两项值之和
print(lis)

print ("""
 冒泡排序""")


def bubbleSort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # ｊ为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


nums = [5, 2, 45, 6, 8, 2, 1]

print(bubbleSort(nums))

print ("""
 有序数组中的二分查找""")
key = int(input("请输入您要查找的整数："))
c = [10, 11, 12, 17, 19, 21, 22, 24, 32, 38, 49, 51, 66, 78, 90]


def BinarySearch(key, c):
    lo, hi = 0, len(c) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if key < c[mid]:
            hi = mid - 1
        elif key > c[mid]:
            lo = mid + 1
        else:
            print("%s在数组中的索引为%s" % (key, mid))
            return
    print("%s不在该数组中" % key)
    return


BinarySearch(key, c)

print ("""
 快速排序""")


def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return


def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]

print("initial array:", arr)
QuickSort(arr, 0, len(arr) - 1)
print ("result array:", arr)
