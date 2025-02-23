import ingredient, stap

class Recept:
    def __init__(self, naam, omschrijving, ingredient_list, stappenlist):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = ingredient_list
        self.__stappenlist = stappenlist
    
    def __str__(self):
        pass

    def voeg_ingredient_toe(self, ingredient: ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredient(self):
        for ingredient in self.__ingredient_list:
            print(ingredient)

    def get_naam(self):
        return self.__naam
    
    def voeg_stap_toe(self, stap : stap):
        self.__stappenlist.append(stap)