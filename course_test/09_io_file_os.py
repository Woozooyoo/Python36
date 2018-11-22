# coding=utf-8

print("""
从文本文件中每读取一行文本便输出""")
fileHandler = open('./a.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
line = fileHandler.readline()
while line:
    print(line)
    line = fileHandler.readline()
fileHandler.close()

print("""
其他文件IO函数的使用""")
fileHandler = open('./a.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
# 读取整个文件
contents = fileHandler.read()  # read读整个文件 封装成str
print(type(contents))
print(contents)
print(fileHandler.tell())

# 读取所有行,再逐行输出
fileHandler.seek(0)
lines = fileHandler.readlines()  # readlines 读所有行封装成 list[str]
print(type(lines))
for line in lines:
    print(line)
# 当前文件指针的位置
print(fileHandler.tell())

fileHandler.close()

print("""
文件的写操作""")
fileHandler = open('./a.txt', 'a+')  # 或者调用open()函数
fileHandler.write("\r\n")
fileHandler.write("thank you")

fileHandler.seek(0)
contents = fileHandler.read()
print(contents)
print(fileHandler.tell())
fileHandler.close()

print("""
文件内容的删除操作  读入内存再写入 大文件效率低""")
import os

pswpath = os.path.join(".", "a.txt")
tmp = os.path.join(".", "b.txt")
with open(pswpath) as f:
    lines = f.readlines()
    curr = lines[:-1]
f = open(tmp, 'w+')  # 以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
f.writelines(curr)
f.close()

