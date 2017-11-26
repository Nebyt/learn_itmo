from catHamster import pets

class Hamster(pets.Pets):
    time_swim = 10

    def __init__(self):
        self.vid = 'hamster'
        super(Hamster, self).__init__(2, 50, 3)

    def swim(self, time):
        if self.time_swim > 10:
            print('Seems the hamster is drown')
        else:
            print('The hamster like swim')