# coding=utf-8

"""7.1、获取当前时间，例如："""
import time, datetime

# 当前时间:
print(time.time())
print(time.localtime(time.time()))
# 结构化时间 time.struct_time(tm_year=2018, tm_mon=10, tm_mday=2, tm_hour=21, tm_min=33, tm_sec=2, tm_wday=1, tm_yday=275,
#  tm_isdst=0)
print(time.asctime(time.localtime(time.time())))

print("""
7.2、获取格式化的时间
可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():""")
# 1、日期转换为字符串
# 首选：
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# 其次：
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
# 最后：
print(str(datetime.datetime.now())[:19])

# 2、字符串转换为日期
expire_time = "2013-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
print(d)

print("""
7.3、获取日期差""")

## 定义时差步长
oneday = datetime.timedelta(1)
print(oneday)
# 今天，2014-03-21
today = datetime.date.today()
# 昨天，2014-03-20
yesterday = datetime.date.today() - oneday
# 明天，2014-03-22
tomorrow = datetime.date.today() + oneday
# 获取今天零点的时间，2014-03-21 00:00:00
today_zero_time = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
print(today_zero_time)

# 0:00:00.001000
print(datetime.timedelta(milliseconds=1), end=' ')  # 1毫秒
# 0:00:01
print(datetime.timedelta(seconds=1), end=' ')  # 1秒
# 0:01:00
print(datetime.timedelta(minutes=1), end=' ')  # 1分钟
# 1:00:00
print(datetime.timedelta(hours=1), end=' ')  # 1小时
# 1 day, 0:00:00
print(datetime.timedelta(days=1), end=' ')  # 1天
# 7 days, 0:00:00
print(datetime.timedelta(weeks=1))

print("""
7.4、获取时间差""")
# 1 day, 0:00:00
oneday = datetime.timedelta(days=1)
# 今天，2014-03-21 16:07:23.943000
today_time = datetime.datetime.now()
# 昨天，2014-03-20 16:07:23.943000
yesterday_time = datetime.datetime.now() - oneday
# 明天，2014-03-22 16:07:23.943000
tomorrow_time = datetime.datetime.now() + oneday
# 注意时间是浮点数，带毫秒。

# 那么要获取当前时间，需要格式化一下：
print(datetime.datetime.strftime(today_time, '%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(yesterday_time, '%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strftime(tomorrow_time, '%Y-%m-%d %H:%M:%S'))

print("""
7.5、获取上个月最后一天""")
last_month_last_day = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)
print(last_month_last_day)

print("""
7.6、字符串日期格式化为秒数，返回浮点类型：""")
expire_time = "2013-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
time_sec_float = time.mktime(d.timetuple())
print(time_sec_float)

print("""
7.7、日期格式化为秒数，返回浮点类型：""")
d = datetime.date.today()
time_sec_float = time.mktime(d.timetuple())
print(time_sec_float)

print("""
7.8、秒数转字符串""")
time_sec = time.time()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_sec)))
