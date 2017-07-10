gameOn = True

while gameOn:
	print ("Pick one of the following options:")
	print ("1. Play a game: ")
	print ("2. Draw a picture: ")
	option = int(input("Enter Option:"))
	if not option:
		exit()
	# Checks and code flow based on user picked options. 
	if option == 1:
		print ("play game")
		print ("1. Taboo: ")
		print ("2. Pictionary: ")
		print ("3. I dont like both options:")
		gameName = int(input("Enter game option:"))

		# Check to see what game the player wants to play
		if gameName == 1:
			print ("Hey you are playing Taboo!")
		elif gameName == 2:
			print ("Hey you are playing Pictionary!")
		elif gameName == 3:
			print ("I know life is unfair")
		else:
			print ("Invalid Option")
	elif option == 2:
		print ("draw a picture")
	else:
		print ("invalid option")

	answer = input("Do you want to play yes/no ?")
	if answer == "yes":
		gameOn = True
	else:
		gameOn = False
print ("Game Over!!")