import time
from util_performance import show_performance, LOOPS

print()
time0 = time.time()
lst1 = []
for i in range(LOOPS):
    lst1 = lst1 + [i]     # 測試方法-1: list plus list

time1 = time.time()
lst2 = []
for i in range(LOOPS):
    lst1 += [i]           # 測試方法-2: addition assignment(+=)

time2 = time.time()
lst3 = []
for i in range(LOOPS):
    lst3.append(i)        # 測試方法-3: append()

time3 = time.time()
secs = (time0, time1, time2, time3)
print('Sans function call...')
show_performance(*secs)