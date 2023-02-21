import random as r

def insert_sep(raw: str = '', sep: tuple | list = ()) -> str:
    # print('/' + raw + '/')
    return '' if not sep else r.choice(sep).join(raw).strip()

print()
print(f"{insert_sep() = }")
print(f"{insert_sep('Python') = }")
print(f"{insert_sep(sep=()) = }")
print(f"{insert_sep('abcdefg', ('.', ',')) = }")
print(f"{insert_sep('棄我去者昨日之日不可留', ('*', '_', '^')) = }")
print(f"{insert_sep('亂我心者今日之日多煩憂', (' ',)) = }")
print(f"{insert_sep('123456', ('+', '-', '*', '/')) = }")
print(f"{insert_sep('心肝脾肺腎 ', ('臟',)) = }")
sep = (' 左中', ' 左食', ' 右中', ' 右食', ' 拇指')
print(f'{sep = }')
print(f"{insert_sep(' 指指指指指指指', sep) = }")
print()
