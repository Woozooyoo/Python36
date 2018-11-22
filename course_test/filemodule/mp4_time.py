# coding=utf-8
import os
import sys
import xlwt
from moviepy.editor import VideoFileClip

"""
python 获取视频文件的大小，时长等"""
file_dir = "E:\Work\TestPyFile"  # 定义文件目录


class FileCheck():

    def __init__(self):
        self.file_dir = file_dir

    def get_filesize(self, filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    def get_file_oritimes(self, filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename, filename)
        return clip.duration

    def get_file_times(self, filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename, filename)
        file_time = self.timeConvert(clip.duration)
        return file_time

    def sizeConvert(self, size):  # 单位换算
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(size / G) + 'G Bytes'
        elif size >= M:
            return str(size / M) + 'M Bytes'
        elif size >= K:
            return str(size / K) + 'K Bytes'
        else:
            return str(size) + 'Bytes'

    def timeConvert(self, size):  # 单位换算
        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒'
        if size < H:
            return u'%s分钟%s秒' % (int(size / M), int(size % M))
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt

    def timeConvertOri(self, size):  # 单位换算
        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒'
        if size < H:
            return u'%s分钟%s秒' % (int(size / M), int(size % M))
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt

    def get_all_file(self):
        u"""
        获取视频下所有的文件
        """
        for root, dirs, files in os.walk(file_dir):
            return files  # 当前路径下所有非目录子文件

# fc = FileCheck()
# files = fc.get_all_file()
# print files
# datas = [[u'文件名称', u'文件大小', u'视频时长']]  # 二维数组
# for f in files:
#     cell = []
#     file_path = os.path.join(file_dir, f)
#     file_size = fc.get_filesize(file_path)
#     file_times = fc.get_file_times(file_path.encode("gbk"))
#     print file_times
#     print u"文件名字：{filename},大小：{filesize},时长：{filetimes}".format(filename=f, filesize=file_size, filetimes=file_times)
#     cell.append(f)
#     cell.append(file_size)
#     cell.append(file_times)
#     datas.append(cell)
