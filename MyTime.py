import random
import time


# 时间字符串转秒数
def time2seconds(t):
    h, m, s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


# 秒数转时间
def seconds2time(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


# 返回两个时间之间的随机时间字符串
# start 开始时间字符串 例子：00:00:00
# end 结束时间字符串 例子：23:59:59
def randomTimeStr(start, end):
    return seconds2time(random.sample(range(time2seconds(start), time2seconds(end)), 1)[0])


__a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
__a2 = (2500, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置结束日期时间元组（2500-01-01 00：00：00）

__start = time.mktime(__a1)  # 生成开始时间戳
__end = time.mktime(__a2)  # 生成结束时间戳

random.seed('D31BDB38-93A9-4F1C-BF9F-52202B8CDA67')


def randomDateTimeStr(fromat='%Y-%m-%d %H:%M:%S'):
    # 在开始和结束时间戳中随机取出一个
    # 将时间戳生成时间元组
    date_touple = time.localtime(random.randint(__start, __end))
    return time.strftime(fromat, date_touple)
