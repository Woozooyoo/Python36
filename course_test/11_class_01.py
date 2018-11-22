# coding=utf-8


class Employee:
    """ doc
    所有员工的基类"""
    empCount = 0  # 相当于静态变量

    # 构造函数
    def __init__(self, name, salary, age):  # 类方法必须包含参数self,且为第一个参数
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp01 = Employee("zhangsan", 100000, 18)
print(emp01.name)
print(emp01.salary)
emp01.displayCount()
emp01.displayEmployee()
emp02 = Employee("lisi", 400000, 48)
del emp02.age
# print emp02.age
emp02.displayCount()
attr = getattr(emp02, 'age', None)
print(attr)
print("emp02.__class__:", emp02.__class__)
print

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)  # 父类
print("Employee.__dict__:", Employee.__dict__)

print("""
私有属性""")


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print counter.__secretCount  # 报错，实例不能访问私有变量
print(counter._JustCounter__secretCount)
