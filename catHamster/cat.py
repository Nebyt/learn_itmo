from catHamster import pets

class Cat(pets.Pets):
    def __init__(self):
        self.vid = 'cat'
        super(Cat, self).__init__(5, 20, 10)
