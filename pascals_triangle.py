# Alex's version
def pascals_triangle(rows: int = 1) -> list:
    triangle = []
    for i in range(rows):
        triangle.append([1])
        for number in range(1, i):
            num_to_add_1 = triangle[i - 1][number]
            num_to_add_2 = triangle[i - 1][number - 1]
            this_num = num_to_add_1 + num_to_add_2
            triangle[i].append(this_num)
        ... if i == 0 else triangle[i].append(1)
    return triangle

try:
    print(f'{pascals_triangle(1)=}')
    print(f'{pascals_triangle(2)=}')
    print(f'{pascals_triangle(3)=}')
    print(f'{pascals_triangle(5)=}')
    print(f'{pascals_triangle(12)=}')
    print(f'{pascals_triangle()=}')
    print(f'{pascals_triangle(0)=}')
except Exception as e:
    print(e)