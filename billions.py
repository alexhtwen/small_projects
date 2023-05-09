from time import time


import psutil

def get_available_memory():
    mem_info = psutil.virtual_memory()
    available_memory = mem_info.available
    return available_memory





# Define a generator function to generate the items of the tuple
def generate_tuple_items(num_items):
    for i in range(num_items):
        yield i

available_memory = get_available_memory()
print(f"Available memory before creating a huge tuple: {available_memory :,} bytes")
items1 = 680_000_000
time1 = time()
# Create a huge tuple using generator expression.
huge_tuple1 = tuple(generate_tuple_items(items1))
time2 = time()
print(f'seconds to create a tuple with {items1:,} items: {round(time2 - time1, 2)}')
print(f'{len(huge_tuple1) = :,}\n')
available_memory = get_available_memory()
print(f"Available memory after creating a huge tuple: {available_memory :,} bytes")
exit()

items2 = 10_000_000
time1 = time()
# Create a second tuple using generator expression.
huge_tuple2 = tuple(generate_tuple_items(items2))
time2 = time()
print(f'seconds to create a tuple with {items2:,} items: {round(time2 - time1, 2)}')
print(f'{len(huge_tuple2) = :,}')
available_memory = get_available_memory()
print(f"Available memory before creating a huge tuple: {available_memory :,} bytes")