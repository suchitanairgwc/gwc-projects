
# Definition for the class: Car
class Car(object):
	# initialize your class attributes
	carMaxPrice = 0
	carMPG = 0
	carType = ""
	carName = ""

	def __init__(self, name):
		self.carName = name
        
	# All the setter methods for this class
	# Set Car Type
	def setCarType(self, typeOption):
		carTypeDict = {"1": "Convertible", "2": "Hybrid", "3" : "Composite"}
		if carTypeDict.get(typeOption):
			self.carType = carTypeDict[typeOption]
		else:
			self.carType = -1

	# Set Price
	def setPrice(self, price_range):
		priceDict = { "1" : 40000, "2" : 50000 ,"3" : 100000}
		if priceDict.get(price_range):
			priceRange = priceDict[price_range]
			self.carMaxPrice = priceRange
		else:
			self.carMaxPrice = -1
	
	# Set MPG	
	def setMPG(self, mpg):
		mpgDict = { "1" : 20 ,"2" : 30, "3" : 40}
		if mpgDict.get(mpg):
			self.carMPG = mpgDict[mpg]
		else:
			self.carMPG = -1
			
	# All the getter methods for this class
	# Get name			
	def getName(self):
		return self.carName
	
	# Get MPG
	def getMPG(self):
		return self.carMPG

	# Get Price
	def getPrice(self):
		return self.carMaxPrice

	# Get Car Type
	def getCarType(self):
		return self.carType

	
def carInventory(name, type, maxprice, mpg):
	found = 0
	typesDict = {
		"Convertible" : ["Ford Mustang", "Mercedes SLK"],
		"Hybrid" : ["Honda Civic", "Toyota Prius"],
		"Composite" : ["Chevrolet Volt", "Tesla Model S"]
	}

	carDetailsDict = {
		"Ford Mustang" : [25000, 25, ["silver","blue","yellow","red"]],
		"Mercedes SLK" : [48000, 30, ["silver","white","black"]],
		"Honda Civic" : [30000, 45, ["slate grey","white"]],
		"Toyota Prius" : [30000, 45, ["baby blue","dark grey"]],
		"Chevrolet Volt" : [35000, 100, ["white","maroon"]],
		"Tesla Model S" : [68000, 100, ["black","deep blue"]],
	}
	carList = typesDict.get(type)
	for car in carList:
		details = carDetailsDict[car]
		if details[0] <= maxprice:
			if details[1] >= mpg:
				found += 1
				print ("\n\nMatch found for: ", name)
				print ("Car Make: ", car)
				print ("MSRP USD: ", details[0])
				print ("MPG: ", details[1])
				print ("Available colors: ", details[2])
	if found == 0:
		print ("Search criteria should be updated, no matches found for: ", name)

		

# Main starts here
print ('\n\n #### WELCOME!! to the NON-SLEAZY virtual car shop! ####\n\n')

# This will be used in a print statement to provide options to the user
# on car types he/she can pick from
car_options = """
Please pick the type of car you are interested in:
1. Convertible
2. Hybrid
3. Composite (Electricity and Gas)
"""

# This will be used in a print statement to provide options to the user on 
# price ranges
price_ranges = """
1. < 40K
2. < 50K
3. < 100K
"""

# This section will be used to take a color input on your car
miles_per_gallon = """
1. 20 mpg
2. 30 mpg
3. 40 mpg
"""
carName = input("What would you like to call your car: ")	
carType = input(car_options)
carPriceRange = input(price_ranges)
carMPG = input(miles_per_gallon)

# Instantiate your car from the "Car" class
myCar = Car(carName)

# Set the type of car and the price range for the car
myCar.setCarType(carType)
myCar.setPrice(carPriceRange)
myCar.setMPG(carMPG)


# Get the car name, price range and type of car
myCarName = myCar.getName()
myCarType = myCar.getCarType()
myCarMax = myCar.getPrice()
myCarMpg = myCar.getMPG()
# 

# Error Checking Code
if myCarType == -1:
	print("Invalid type of car specified, exiting...")
	exit(1)

if myCarMax == 0 or myCarMax == -1:
	print("Invalid Price range specified for your car, exiting...")
	exit(1)

if myCarMpg == 0 or myCarMpg == -1:
	print("Invalid selection for MPG, exiting..")
	exit(1)

#print ("My car is called: ", myCarName)
#print ("Car type selected: ", myCarType)
#print ("Maximum price range specified is: ", myCarMax)
#print ("Miles per gallon for %s is:  %s mpg." %(myCarName, myCarMpg))

carInventory(myCarName, myCarType, myCarMax, myCarMpg)


