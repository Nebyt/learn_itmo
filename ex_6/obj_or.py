class Home:
    s = None
    pets = None
    foods = None

    def __init__(self, pets):
        Home.s = 100
        Home.pets = pets
        Home.foods = 200

    @staticmethod
    def get_s(): return Home.s

    @staticmethod
    def get_pets(): return Home.pets

    @staticmethod
    def get_foods(): return Home.foods

    @staticmethod
    def set_foods(foods):
        Home.foods = foods
        return Home.foods

class Pets:
    pets = []

    def get_pets(self):
        return self.pets

    def add_pets(self, pet):
        tmp_pets = self.pets
        tmp_pets.append(pet)
        self.pets = tmp_pets

    def del_pets(self, pet):
        tmp_pets = self.pets

        for i in range(len(tmp_pets)):
            if tmp_pets[i].vid == pet.vid:
                tmp_pets.pop(i)
                break

        self.pets = tmp_pets


class Cat:
    def __init__(self):
        self.vid = "cat"
        self.s = 20
        self.food = 23
        self.price = 20


class Hamster:
    def __init__(self):
        self.vid = "hamster"
        self.s = 10
        self.food = 2
        self.price = 3


class Master(Home):
    def __init__(self, pets):
        super(Master, self).__init__(pets)
        self.cash = 100
        self.name = "Vasia"

    def buy_Pets(self, pet):
        s = aval_s = 0

        money = self.cash - pet.price
        pets = Home.pets

        for pt in pets.get_pets():
            s = s + pt.s

        aval_s = super(Master, self).get_s() - s

        if money < 0:
            return
        elif aval_s <= 0:
            return
        else:
            super(Master, self).get_pets().add_pets(pet)
            self.cash = money

    def food_pets(self):
        pets = Home.pets

        food = Home.foods

        for pt in pets.get_pets():
            food = food - pt.food

        self.set_foods(food)

        print("pets =", pets.get_pets())
        print("food =", food)

    def food_count(self):
        tm_pets = Home.pets
        food = Home.foods
        food_count = 0
        cats_day_food = 0

        for pt in tm_pets.get_pets():
            food_count += pt.food

        for pt in tm_pets.get_pets():
            if isinstance(pt, Cat):
                cats_day_food += pt.food


        day_before_eat_hamster = food / food_count
        if int(day_before_eat_hamster) > 0:
            print('До того как съедят хомяка осталось {0} дн(я/ей)'.format(int(day_before_eat_hamster)))
            print('Котам надо {0} еды на день'.format(cats_day_food))
        else:
            print('Хомяка уже едят')
            print('Котам надо {0} еды на день'.format(cats_day_food))

m = Master(Pets())
m.buy_Pets(Cat())
m.buy_Pets(Cat())
m.buy_Pets(Cat())
m.buy_Pets(Hamster())
m.buy_Pets(Hamster())
m.food_pets()
m.food_count()