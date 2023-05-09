def sort_str(raw_str: str, reverse=False) -> str:
    return ''.join(sorted(list(raw_str), reverse=reverse))

def max_min(raw: int, operator: str) -> int | float | None:
    max_ = int(sort_str(str(raw), reverse=True))
    min_ = int(sort_str(str(raw)))
    # try:
    match operator:
        case '+':
            result = max_ + min_
        case '-':
            result = max_ - min_
        case '*':
            result = max_ * min_
        case '/':
            result = round(max_ / min_, 2)
        case '//':
            result = max_ // min_
        case '%':
            result = max_ % min_
        case '**':
            result = max_ ** min_
        case _:
            # raise SyntaxError('Invalid operator.')
            result = None
    return result

print()
print()
operators = ('+', '-', '*', '/', '//', '%', '@')
num = 2010838701
for oper in operators:
    print(f"max_min({num}, '{oper}'): {max_min(num, oper)}")
print()