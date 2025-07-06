import time

print(time.time())
print(time.ctime(time.time()))

print()

print(time.gmtime(time.time()))
print(time.asctime(time.gmtime(time.time())))

print()

print(time.localtime())
print(time.asctime(time.localtime()))

print()

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print()

print(time.mktime((2023, 7, 24, 12, 34, 56, 0, 0, 0)))
print(time.ctime(time.mktime((1987, 1, 1, 1, 1, 1, 1, 1, 1))))

print()

print(time.ctime(time.perf_counter()))
print(time.sleep(2))
print(time.ctime(time.perf_counter()))
