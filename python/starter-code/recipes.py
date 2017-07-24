# Recipe catalog that keeps track of recipes already stored in the program
recipeCatalogList = ["Scrambled Eggs"]

# This list contains the ingredients used in a recipe
# This list contains dictionaries and lists in it. 

ingredientsDict = {
	"Scrambled Eggs": 
		[
			"eggs: 3", 
			"olive oil: 2 ts",
			"grated cheese: 1 tbs", 
			"salt: to taste", 
			"pepper: to taste", 
			"dried thyme: 1 ts"
		]
}


# This dictionary stores the steps for a recipe
# This dictionary contains a list 

preparationStepsDict = {
	"Scrambled Eggs": [
		"1. Crack eggs in a bowl", 
		"2. Whisk eggs",
		"3. Heat oil in a pan",
		"4. Pour beaten eggs onto pan and stir till eggs start to solidify",
		"5. Add salt, pepper, thyme, and cheese",
		"6. Serve hot and enjoy!"
	]
	
}


# function to find and print recipe
def findRecipe(recipeName):
	recipeFound = 0;
	print ("\nHere is the recipe for: " + recipeName)
	# Print ingredients for the recipe
	for recipe, ingredients in ingredientsDict.items():
		if recipe == recipeName:
			recipeFound +=1;
			print ("\nIngredients:")
			for item in ingredients:
				print (item)
	# Print preparation steps for the recipe
	for recipe, steps in preparationStepsDict.items():
		if recipe == recipeName:
			recipeFound +=1;
			print ("\nSteps:")
			for instruction in steps:
				print (instruction)

	return recipeFound

# TODO Steps
# First add an additional recipe to the lists, dictionaries above as a trial run
# Next iteration, add another function to add recipes
### This function will need the recipe name, list of ingredients and list of steps
### Also figure what stes should be executed in this function to add to the existing list of recipes 



# main function starts here

## TODO Steps
## Figure out how you will ask for user input to allow printing of existing recipes
## Figure out how you will ask for user input to add new recipes.

# printing the recipe catalog list
for recipe in recipeCatalogList:
   print (recipe)

# Get the input for the recipe
selectedRecipe = input("Please select a recipe from above: ")

# Call funtion to find and print the recipe
result = findRecipe(selectedRecipe)

# Evaluate result to figure out if the recipe was returned completely or not.
if result == 0:
	print('Ooops recipe not found!')
elif result < 2:
	print('Sorry! recipe does not look to be complete.')
else:
	print('Recipe found and printed successfully')







