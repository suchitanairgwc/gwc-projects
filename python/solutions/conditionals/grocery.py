grocery = []

keepEditing = True

while keepEditing:
	#Check if the user wants to keep adding
	addOrRemove = input("Do you want to add or remove items, type add/remove/ ?")

	if addOrRemove == "add":
		groceryItem = input("Enter item to add to your grocery list: ")
		grocery.append(groceryItem)
		keepEditing = True
	elif addOrRemove == "remove":
		print ("Grocery List: ", grocery)
		removeItem = input("Enter item to remove")
		grocery.remove(removeItem)
		keepEditing = True
	else:
		print ("Invalid Option")
		keepEditing = False

	continueEditing = input("Do you want to keep editing your grocery list Y/N?")
	if continueEditing.upper() == "Y":
		keepEditing = True
	else:
		keepEditing = False

print ("This is my final grocery list: ", grocery)
