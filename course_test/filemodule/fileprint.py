# coding=gbk
import os

"""GBK!!!"""


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
                    num = name.rfind("、")
                    new_name = name[num + 1:]
                    os.rename(fullname + name, fullname + new_name)
                    break


def Test():
    dir = "E:\Work\TestPyFile"
    outfile = os.path.join(dir, "depth.txt")
    wildcard = ".avi .mp4 .wmv"

    file = open(outfile, "w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 1)

    file.close()


Test()
