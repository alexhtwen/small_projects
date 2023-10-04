class BreakException(Exception):
    pass

def break_if(condition):
    if condition:
        raise BreakException()

try:
    results = [x for x in range(10) if x < 5 or break_if(True)]
except BreakException:
    pass
finally:
    print(results)
