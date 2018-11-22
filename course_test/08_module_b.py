# coding=utf-8
"""
引入了 module a   加载 a 的时候 a 的执行代码也会执行
"""
import course_test._08_module_a

course_test._08_module_a.print_func("haha")

from course_test._08_module_a import *

print_func("heihei")

from course_test._08_module_a import print_func as pf

pf("xixi")

# import 多次时  只要导入过一次后面就不会再加载
# in module a:  _08_module_a
# 在b中调用了module a的 __name__ 是其模块名: _08_module_a
print('in module b,', __name__)
