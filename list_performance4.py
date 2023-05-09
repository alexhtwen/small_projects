import time
from util_performance import show_performance, LOOPS

def create_lst_1(i):
    global lst1
    return lst1 + [i]

def create_lst_2(i):
    global lst2
    lst2 += [i]
    return lst2

def create_lst_3(i):
    global lst3
    lst3.append(i)
    return lst3

lst1 = []
lst2 = []
lst3 = []

print()
time0 = time.time()
for i in range(LOOPS):
    lst1 = create_lst_1(i)

time1 = time.time()
for i in range(LOOPS):
    lst2 = create_lst_2(i)

time2 = time.time()
for i in range(LOOPS):
    lst3 = create_lst_3(i)

time3 = time.time()
secs = (time0, time1, time2, time3)

print('Thousands function calls, with globals...')
show_performance(*secs)