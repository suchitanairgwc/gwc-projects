import csv
import string

# Open the CSV File and read it in.
f = open(input("Enter the filename: "))
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
print(elementsList[0])

# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algorithm here.
selectedCountry = input("What country are you looking for?????? ")
beginningIndex = 0
endingIndex = len(elementsList)

index = int((beginningIndex + endingIndex)/2)

while elementsList[index] != selectedCountry:
	# print(index)
	print("beginning" + str(beginningIndex) + "ending: "+ str(endingIndex) +
		 "index" + str(index))

	if elementsList[index] < selectedCountry:
		beginningIndex = index
		endingIndex = endingIndex
	elif elementsList[index] > selectedCountry:
		beginningIndex = beginningIndex
		endingIndex = index
	else: 
		print("Yay you found the country: " + selectedCountry + "at index " + str(index))
		break
	index = int((beginningIndex + endingIndex)/2)
print("Yay you found the country: " + selectedCountry + "at index " + str(index))

print("Done.")
