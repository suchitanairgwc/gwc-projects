fopen = open('countries.csv')

data = fopen.read()



dataList = data.split('\n')


for dataElement in dataList:
	print (dataElement)


searchElement = input("Enter element from list to find position: ")

searchIndexBegin = 0
searchIndexEnd = len(dataList) - 1


count = 0
notFound = True
searchIndex = int(round(len(dataList[searchIndexBegin:searchIndexEnd])/2))
while searchIndexBegin <= searchIndexEnd and notFound:
	if (searchIndexEnd - searchIndexBegin) == 1:
		if searchElement == dataList[searchIndexEnd]:
			print ("Found element at position: ", searchIndex, "in attempts:", count)
			notFound = False
			break;
		else:
			break
	if searchElement < dataList[searchIndex]:
		searchIndexEnd = searchIndex
		searchIndex = int(round(len(dataList[searchIndexBegin:searchIndexEnd])/2))
	elif searchElement > dataList[searchIndex]:
		searchIndexBegin = searchIndex
		searchIndex += int(round(len(dataList[searchIndexBegin:searchIndexEnd])/2))
	else:
		print ("Found element at position: ",  searchIndex, "in attempts:", count)
		notFound = False
	count += 1
	

if notFound:
	print("Element not found")
	