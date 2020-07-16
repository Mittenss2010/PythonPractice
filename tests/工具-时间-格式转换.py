python的时间格式转换
复制代码
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time;  # 引入time模块
 
ticks = time.time()
print "当前时间戳为:", ticks
 
localtime = time.localtime(time.time())
print "本地时间为 :", localtime
 
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
 
## 输出格式：2016-03-20 11:45:39
## time.localtime() 默认为当前时间
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
 
# 将格式字符串转换为时间戳
a = "Wed Feb 07 11:40:32 2018"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
print('')
 
import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
 
import calendar
 
cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;
复制代码
输出如下：

复制代码
当前时间戳为: 1517974979.48
本地时间为 : time.struct_time(tm_year=2018, tm_mon=2, tm_mday=7, tm_hour=11, tm_min=42, tm_sec=59, tm_wday=2, tm_yday=38, tm_isdst=0)
本地时间为 : Wed Feb 07 11:42:59 2018
2018-02-07 11:42:59
Wed Feb 07 11:42:59 2018
1517974832.0
 
当前的日期和时间是 2018-02-07 11:42:59.478000
ISO格式的日期和时间是 2018-02-07T11:42:59.478000
当前的年份是 2018
当前的月份是 2
当前的日期是  7
dd/mm/yyyy 格式是  7/2/2018
当前小时是 11
当前分钟是 42
当前秒是  59
以下输出2016年1月份的日历:
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31