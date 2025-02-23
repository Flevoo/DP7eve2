from recept import Recept
from ingredient import Ingredient
from stap import Stap


# objecten voor de pasta ingriedient.
receptRodePasta = Recept("Rode Pasta", "Deze snelle pasta met rode saus, knoflook, paprika en Parmezaanse kaas is perfect comfortfood zonder lang in de keuken te staan.", [], [])
ingredientPasta = Ingredient("- pasta", 150, "Gram")
ingredientSaus = Ingredient("- Tomaten Saus", 400, "ML")
ingriedientUi = Ingredient("- Ui", 1, "aantal")
ingredientKruiden = Ingredient("- italiaanse kruiden", 1, "eetlepel")
ingredientPaprika = Ingredient("- Paprika", 1, "liter")
ingredientChili = Ingredient("- Chili", 1, "aantal")
ingredientParmezanCheese = Ingredient("- Parmezanche", 1, "aantal")
StapRodePasta1 = Stap("1.Kook de pasta volgens de aanwijzingen op de verpakking in een pan met gezouten water. Giet af en zet opzij.")

print (receptRodePasta.get_naam())
print (receptRodePasta.get_omschrijving())
receptRodePasta.voeg_ingredient_toe(ingredientPasta)
receptRodePasta.voeg_ingredient_toe(ingredientSaus)
receptRodePasta.voeg_ingredient_toe(ingriedientUi)
receptRodePasta.voeg_ingredient_toe(ingredientKruiden)
receptRodePasta.voeg_ingredient_toe(ingredientPaprika)
receptRodePasta.voeg_ingredient_toe(ingredientChili)
receptRodePasta.voeg_ingredient_toe(ingredientParmezanCheese)
receptRodePasta.voeg_stap_toe(StapRodePasta1)
receptRodePasta.get_ingredient()
receptRodePasta.get_stap()




