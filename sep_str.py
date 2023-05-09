import random as r

def insert_sep(raw: str = '', sep: tuple | list = ()) -> str:
    return '' if not sep else r.choice(sep).join(raw).strip()

print()
print(f"{insert_sep() = }")
print(f"{insert_sep('Python') = }")
print(f"{insert_sep(sep=()) = }")
print(f"{insert_sep('abcdefg', ('.', ',')) = }")
print(f"{insert_sep('人有悲歡離合', ('*', '_', '^')) = }")
print(f"{insert_sep('月有陰晴圓缺', (' ',)) = }")
print(f"{insert_sep('123456', ('+', '-', '*', '/')) = }")
print(f"{insert_sep('心肝脾肺腎 ', ('臟 ',)) = }")
sep = (' 肩胛', ' 下頜', ' 肋', ' 肱', ' 中節趾')
print(f'{sep = }')
print(f"{insert_sep(' 骨骨骨骨', sep) = }")
print()
print()