# coding=gbk
import os
from mp4_time import FileCheck
import sys

reload(sys)
sys.setdefaultencoding('gbk')
file_dir = "E:\Work\TestPyFile"
fc = FileCheck()


def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    (filename, extension) = os.path.splitext(name)
                    file_times = fc.get_file_times(fullname)
                    file.write((fullname + "\t" + file_times + "\n"))
                    break


def Test():
    dir = file_dir
    outfile = os.path.join(dir, "depth.txt")
    wildcard = ".avi .mp4 .wmv"

    file = open(outfile, "w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 1)

    file.close()


Test()
