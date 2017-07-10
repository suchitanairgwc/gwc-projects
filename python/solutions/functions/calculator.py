# Function to add numbers in the given list
def add(number_list):
	result = 0
	for number in number_list:
		result = result + int(number)
	return result

# Function to find the average of numbers in the given list
def average(number_list):
	result = 0 
	listSum = 0
	listLength = len(number_list)
	listSum = add(number_list)
	result = listSum/listLength
	return result

# Our main program starts here`
answer = 0

option = input("Do you want to add or find an average ? add/average ")
if option != "add" and option != "average":
	print ("Invalid Option")
	exit()
numbersIn = input("Enter numbers separated by comma: ")

numbersList = numbersIn.split(",")

if option == "add":
	answer = add(numbersList)
elif option == "average":
	answer = average(numbersList)
print ("The answer is:", answer)
