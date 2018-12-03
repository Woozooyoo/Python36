# coding:utf-8

import os

if __name__ == "__main__":
    i = 1
    while i < 13:
        file_name = 'url_20181128_' + str(i) + 'kw'
        start_num = (i - 1)*10000000 + 1
        end_num = 10000000*i
        cmd1 = "sed -n '{0},{1}p' url_20181128 >>{2}".format(start_num, end_num, file_name)
        os.system(cmd1)
        i += 1
