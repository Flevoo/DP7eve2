class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid):
        self.__naam = naam
        self.__hoeveelheid = 0.0
        self.__eenheid = eenheid

    def __str__(self):
        return self.__naam

