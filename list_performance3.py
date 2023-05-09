import time
from util_performance import show_performance, LOOPS

def create_lst_1(lst, i):
    return lst + [i]

def create_lst_2(lst, i):
    lst += [i]
    return lst

def create_lst_3(lst, i):
    lst.append(i)
    return lst

print()
time0 = time.time()
lst1 = []
for i in range(LOOPS):
    lst1 = create_lst_1(lst1, i)

time1 = time.time()
lst2 = []
for i in range(LOOPS):
    lst2 = create_lst_2(lst2, i)

time2 = time.time()
lst3 = []
for i in range(LOOPS):
    lst3 = create_lst_3(lst3, i)

time3 = time.time()
secs = (time0, time1, time2, time3)

print('Thousands function calls, sans globals...')
show_performance(*secs)
# print(lst1)
# print(lst2)
# print(lst3)