# coding=utf-8


print("""
定义函数  python函数是引用传递""")


def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([4, 3, 2, 1])  # 把list当作一个整体元素加入
    mylist.extend([1, 2, 3, 4])  # 相融两个list
    print("Values inside the function: ", mylist)
    return (mylist, "haha")


# 调用函数
mylist = [10, 20, 30]
haha = changeme(mylist)
print(haha)
print("Values outside the function: ", mylist)  # 引用传递
print()


# 默认参数
# 有默认值的参数后面不能再跟无默认值的参数
def printinfo(name, age=35):
    print("Name: ", name)
    print("Age ", age)
    return


# 调用
# 如果调换了参数的顺序，则必须把参数名都带上
printinfo(age=50, name="micheal")
printinfo("monica")

print("""
  可变参数 类似String.. args""")


def printinfo(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print("Output is: ")
    print(arg1)
    print('可变参数类型是：', type(vartuple))
    for var in vartuple:
        print(var)
    return


# 调用
printinfo(10)
printinfo(70, 60, 50)

print("""
  定义lambda: anonymous fun""")
sum = lambda arg1, arg2: arg1 + arg2  # lambda表达式
# 调用
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))
print()

# 返回多个值
tup = lambda x, y: (x + 1, y + 1)
c = tup(2, 3)
print(c[0], c[1])

(a, b) = tup(2, 3)
print(a, b)

print()


def outfunc(func, x, y):
    c = func(x, y)
    print(c)


outfunc(lambda x, y: x + y, 1, 2)
