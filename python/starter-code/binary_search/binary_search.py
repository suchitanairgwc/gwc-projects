import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
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
