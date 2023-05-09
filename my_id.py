items = [1, 2, 3]
print(items)
id1 = id(items)
print(id1)
print(id(items[:]))

print('--------')
items[:] = []
print(items)
id2 = id(items)
print(id2)
print(id1 == id2)