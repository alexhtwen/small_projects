import time
from util_performance import show_performance, LOOPS

def create_lst_1(loops):
    lst = []
    for i in range(loops):
        lst = lst + [i]
    return lst

def create_lst_2(loops):
    lst = []
    for i in range(loops):
        lst += [i]
    return lst

def create_lst_3(loops):
    lst = []
    for i in range(loops):
        lst.append(i)
    return lst

print()
time0 = time.time()
lst1 = create_lst_1(LOOPS)

time1 = time.time()
lst2 = create_lst_2(LOOPS)

time2 = time.time()
lst3 = create_lst_3(LOOPS)

time3 = time.time()
secs = (time0, time1, time2, time3)

print('Three function calls, sans globals...')
show_performance(*secs)