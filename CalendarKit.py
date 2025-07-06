import calendar
import time

print(calendar.month(2003, 9))

print(calendar.monthcalendar(2003, 9))

print(calendar.calendar(1975))

print(calendar.isleap(1764))

print(calendar.leapdays(1764, 1768))

print(calendar.day_name[calendar.weekday(2003, 9, 1)])

print(calendar.FRIDAY)

print(calendar.timegm((2003, 1, 1, 1, 1, 1)))

print(time.ctime(calendar.timegm((2003, 1, 1, 1, 1, 1))))
