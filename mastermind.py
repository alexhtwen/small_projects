import random as rd

ans = ''.join(str(digit) for digit in rd.choices(range(10), k=4))
# ans
print('okjhihijjk')
while True:
    digits = input('Input your guess:')
    if digits == '-1':
        break
    a_count = b_count = 0
    for i, digit in enumerate(digits):
        if digit == ans[i]:
            a_count += 1
        elif digit in ans:
            b_count += 1

    print(f'{digits}: {a_count}A{b_count}B')
    if a_count == 4:
        break
