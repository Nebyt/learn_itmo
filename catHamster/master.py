class Master:
    __square = 0

    def __init__(self, square):
        self.cash = 100
        self.name = "Vasia"
        self.__square = square

    @staticmethod
    def get_square():
        return Master.__square