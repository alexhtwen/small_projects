def reorder_list1(input_list):
    return [item for item in input_list if item is not None] + [item for item in input_list if item is None]

def reorder_list2(input_list):
    return sorted(input_list, key=lambda x: x is None)

def reorder_list3(input_list):
    return [item for item in input_list if (item is not None) or (count := (count if 'count' in locals() else 0) + 1) is None] + [None] * count

def reorder_list4(input_list):
    return [item for item in input_list if item is not None] + [None] * sum(1 for item in input_list if item is None)

def reorder_list5(input_list):
    return (new_list := [item for item in input_list if item is not None]) + [None]*(len(input_list) - len(new_list))


print()
# print(f"{reorder_list3([]) = }")
print(f"{reorder_list3([4, 3, None, 9, None, None, 1]) = }")
# print(f"{reorder_list3(['None', '0', '6']) = }")
print()

exit()

import time
import random as r

loops = 10000
in_list = [r.choice([i for i in range(10)] + [None]) for i in range(100000)]

time1 = time.time()
for _ in range(loops):
    new_list = reorder_list1(in_list)
time2 = time.time()
print(f'reorder_list1: {time2 - time1 = }')

time1 = time.time()
for _ in range(loops):
    new_list = reorder_list2(in_list)
time2 = time.time()
print(f'reorder_list2: {time2 - time1 = }')

time1 = time.time()
for _ in range(loops):
    new_list = reorder_list3(in_list)
time2 = time.time()
print(f'reorder_list3: {time2 - time1 = }')

time1 = time.time()
for _ in range(loops):
    new_list = reorder_list4(in_list)
time2 = time.time()
print(f'reorder_list4: {time2 - time1 = }')

time1 = time.time()
for _ in range(loops):
    new_list = reorder_list5(in_list)
time2 = time.time()
print(f'reorder_list5: {time2 - time1 = }')