class Pets:
    pets = []
    time_swim = 20

    def __init__(self, price=0, food=0, square=0):
        self.price = price
        self.food = food
        self.square = square

    def get_pets(self):
        return self.pets

    def add_pets(self, pet):
        tmp_pets = self.pets
        tmp_pets.append(pet)
        self.pets = tmp_pets

    def swim(self, time):
        if time > self.time_swim:
            print('Seems the pet is drown')
        else:
            print('The pet like swim')


class Hamster(Pets):
    time_swim = 10

    def __init__(self):
        self.vid = 'hamster'
        super(Hamster, self).__init__(50, 2, 3)

    def swim(self, time):
        if time > self.time_swim:
            print('Seems the hamster is drown')
        else:
            print('The hamster like swim')


class Cat(Pets):
    def __init__(self):
        self.vid = 'cat'
        super(Cat, self).__init__(20, 5, 10)


pet = Pets()
pet.add_pets(Cat())
pet.add_pets(Hamster())
pet.add_pets(Cat())
for p in pet.get_pets():
    p.swim(15)
    print(p.food, p.price, p.square)