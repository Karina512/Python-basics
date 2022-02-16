from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consuption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v
    
    @property
    def consuption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consuption(self):
        return 2 * self.h + 0.3

    def sum_consuption(self, list_suits):
        a = 0
        for suit in list_suits:
            a += suit.consuption
        return a

coat = Coat(50)
costume = Suit(1.96)
costume_1 = Suit(1.24)
costume_2 = Suit(1.76)
costume_3 = Suit(2.10)
list_costumes = [costume, costume_1, costume_2, costume_3]
print(coat.consuption)
print(costume.consuption)
print(costume.sum_consuption(list_costumes))
