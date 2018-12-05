# coding:utf-8

import os
import sys

f_date = sys.argv[1]

if __name__ == "__main__":
    i = 1
    while i < 14:
        file_name = 'url_{0}_'.format(f_date) + str(i) + 'kw'
        start_num = (i - 1) * 10000000 + 1
        end_num = 10000000 * i
        cmd1 = "sed -n '{0},{1}p' url_{2} >>{3}".format(start_num, end_num, f_date, file_name)
        os.system(cmd1)
        i += 1
