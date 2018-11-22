# coding=utf-8
import os

print"""获取目录下的所有目录"""
i=0
for root,dirs,files in os.walk('E:\Work\TestPyFile'):

    for dir in dirs:
        print dir
        i+=1
print i

import os

print"""
文件个数"""
i = 0
for root, dirs, files in os.walk('E:\Work\TestPyFile'):

    for f in files:
        print file
        i += 1
print i

print"""
返回tuple"""
for list_all in os.walk("E:\Work\TestPyFile"):
    print list_all

print"""
返回打印结果"""
for root, dirs, files in os.walk("E:\Work\TestPyFile"):
    print root, dirs, files


print os.listdir('E:\Work\TestPyFile')

print"""
file2"""
path = 'E:\Work\TestPyFile'

print(os.path.basename(path))  # 查询路径中包含的文件名
print(os.path.dirname(path))  # 查询路径中包含的目录

info = os.path.split(path)  # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))  # 查询多个路径的共同部分
os.path.normpath(path)  # 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'

import os.path

path = 'E:\Work\TestPyFile'

print(os.path.exists(path))  # 查询文件是否存在

print(os.path.getsize(path))  # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))  # 路径是否指向常规文件
print(os.path.isdir(path))  # 路径是否指向目录文件
