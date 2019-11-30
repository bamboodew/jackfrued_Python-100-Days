# datetime是Python处理日期和时间的标准库。
# 获取当前日期和时间
# 我们先看如何获取当前日期和时间：
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2015, 4, 19, 12, 20, 9)
print(dt)

# datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))

# str转换为datetime
str_day = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(str_day)

# datetime转换为str
print(now.strftime('%a,%b %d %H:%M'))

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print('now:', now)
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print('强制设置为UTC+8:00:', dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)  # 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
