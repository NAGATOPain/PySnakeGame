import random


class Food:

    __RATIO = 25
    __COLOR = (255, 255, 51)

    def __init__(self):
        x = random.randrange(0, 501 - 25, 25)
        y = random.randrange(100, 601 - 25, 25)
        self.__pos = (x, y, self.__RATIO, self.__RATIO)

    def get_pos(self):
        return self.__pos

    def generate(self):
        x = random.randrange(0, 501 - 25, 25)
        y = random.randrange(100, 601 - 25, 25)
        self.__pos = (x, y, self.__RATIO, self.__RATIO)

    def get_color(self): return self.__COLOR
