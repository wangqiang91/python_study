"""
    模块说明
"""
print(__doc__)

# 如果当前模块是主模块，则模块名是__main__;
# 如果当前模块不是主模块是被导入的 ，则模块名是文件名称；
print(__name__)

"""
    时间模块
"""
import time
print(time.time())
print(time.localtime())

# 时间戳  ==》  时间元祖：
time_tuple = time.localtime(1679392054.128453)
print(time_tuple)

# 时间元祖 ==》 时间戳：
print(time.mktime(time_tuple))

# 时间元祖 ==》 字符串：
print(time.strftime("%Y/%m/%d %H:%M:%S",time_tuple))

# 字符串 ==》 时间元祖:
print(time.strptime("2023/03/21 17:47:34","%Y/%m/%d %H:%M:%S"))