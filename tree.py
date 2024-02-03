class Tree():
    def __init__(self, breed: str, age: int, height: int):
        self.breed = breed
        self.age = age
        self.height = height

    tree1 = Tree('ceder', 150, 25)
    print(f'{tree1.breed = }\t{tree1.age}')
