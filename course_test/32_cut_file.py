# coding:utf-8

import os

if __name__ == "__main__":
    i = 0
    while i < 106:
        file_name = '000' + str(i).zfill(3) + '_0'
        dir_name = '/data/11084769/url_data/url_2018_1205_billion/'
        cmd1 = "cat {0}|cut -f 1 >>{1}{0}".format(file_name, dir_name)
        os.system(cmd1)
        i += 1
