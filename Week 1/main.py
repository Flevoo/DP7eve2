from recept import Recept
from ingredient import Ingredient
from stap import Stap


# objecten voor de pasta ingriedient.
receptA = Recept("pasta","lekkere pasta",[], [])
ingredientA = Ingredient("Bloem", 20,"ML")
IngriedientB = Ingredient("Saus", 200, "ML")
IngriedientC = Ingredient("Gehaktballen", 10, "aantal")
IngredientD = Ingredient("Italiaanse kruiden", 200, "gram")
IngredientE = Ingredient("water", 2, "liter")


print (receptA.get_naam())
receptA.voeg_ingredient_toe(ingredientA)
receptA.get_ingredient()