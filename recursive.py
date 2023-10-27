import sys
sys.setrecursionlimit(175_000_000)

def r(count: int):
    if count == 170_000_000:
        return count
    else:
        count += 1
        return r(count)

print(r(1))
