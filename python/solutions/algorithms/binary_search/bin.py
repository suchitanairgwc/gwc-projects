fopen = open('countries.csv')

data = fopen.read()



dataList = data.split('\n')


for dataElement in dataList:
	print (dataElement)


searchElement = input("Enter element from list to find position: ")

first = 0

last = len(dataList)-1
found = False
	
while first<=last and not found:
	midpoint = (first + last)//2
	if dataList[midpoint] == searchElement:
	    found = True
	    print ("found at:", midpoint)
	else:
		if searchElement < dataList[midpoint]:
			last = midpoint-1
		else:
			first = midpoint+1	

if found == False:
	print ("Could not find: ", searchElement)