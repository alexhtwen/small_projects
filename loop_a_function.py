import time

LOOPS = 50_000

def do_something() -> None:
    return None

time1 = time.time()
for i in range(LOOPS):
    pass

time2 = time.time()
for i in range(LOOPS):
    do_something()

time3 = time.time()

sans_function = time2 - time1
with_function = time3 - time2

print()
print(f'1. sans function call: {sans_function}')
print(f'2. with function call: {with_function}')
print(f'is 1 faster than 2: {sans_function < with_function}')
