# coding=gbk
import os
from mp4_time import FileCheck
import sys

reload(sys)
sys.setdefaultencoding('gbk')
file_dir = "E:\Study\BDpan\\003-尚硅谷大数据集合\尚硅谷大数据2017-201804\\31_尚硅谷大数据技术之友盟项目-9.10左右七天"
fc = FileCheck()
global_times = 0


def ListFilesToTxt(dir, file, timefile, wildcard, recursion):
    global global_times
    file_times = 0
    exts = wildcard.split(" ")
    files = os.listdir(dir)

    n = 0  # 为了控制最后一个元素输出
    length = len(files)  # 为了控制最后一个元素输出 当最后一个元素不是视频就不行了
    for name in files:
        n += 1  # 为了控制最后一个元素输出
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, timefile, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    (filename, extension) = os.path.splitext(name)
                    file_times += + fc.get_file_oritimes(fullname)
                    global_times += fc.get_file_oritimes(fullname)
                    file.write((fullname + "\n"))
                    if n == length:  # 为了控制最后一个元素输出
                        file.write(fc.timeConvert(file_times) + "\n")
                        timefile.write(dir + "\t" + fc.timeConvert(file_times) + "\n")
                    break


def Test():
    dir = file_dir
    outfile = os.path.join(dir, "deptht.txt")
    outfiletime = os.path.join(dir, "depthTime.txt")
    wildcard = ".avi .mp4 .wmv .rmvb"

    file = open(outfile, "w")
    timefile = open(outfiletime, "w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, timefile, wildcard, 1)

    totaltime = os.path.join(dir, "duration" + fc.timeConvert(global_times))
    file2 = open(totaltime, "w")

    file.close()
    timefile.close()
    file2.close()


Test()
