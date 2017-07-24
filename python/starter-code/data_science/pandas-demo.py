#from pandas import DataFrame
import pandas as pd
import numpy as np

#from matplotlib import pylab
#from pylab import *
import matplotlib.pyplot as plt


# Data for each of the columns in my Dataframe
revenue = [2.4, 3.6, 4.5, 5.6, 6.5]
operationalCost = [1.3, 2.5, 2.7, 2.9, 3.0]
year = [2013, 2014, 2015, 2016, 2017]
marketGrowth = [50, 65, 75, 77, 81  ]

year1 = pd.date_range(start='2012', end='2017')

# Adding a new dataframe
annualRevenueCostDataframe = pd.DataFrame(
	{
		"Revenue": revenue, 
		"Year": year, 
		"Ops Cost" : operationalCost,
		"MarketGrowth": marketGrowth
	}
)

# Printing a dataframe
print (annualRevenueCostDataframe)

# Plotting a dataframe
## Plot a single column as a line chart
#annualRevenueCostDataframe.plot(x='Year' , y='Revenue')

## Plot a single column as a bar chart
#annualRevenueCostDataframe.plot(x='Year' , y='Revenue', kind='bar', title='Revenue')
## Plot multiple columns as a horizontal bar chart
# annualRevenueCostDataframe.plot(x='Year' , y=['Ops Cost', 'Revenue'], kind='barh')
annualRevenueCostDataframe.plot(
	x='Year' ,
	y=['Ops Cost', 'Revenue'], 
	kind='bar', 
	title = 'Costs v.s. Revenue',
	colormap = 'viridis'
)


plt.show()