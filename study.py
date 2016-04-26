import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'Salaries.csv'
salariesDF = pd.read_csv(filename)
print salariesDF.head()

teamID = salariesDF["teamID"].unique()

# Database with two columns
salariesDF_reduced = salariesDF[["teamID","salary"]]

salariesDF_summary_by_teamID = salariesDF_reduced.groupby("teamID").agg([np.sum,np.max,np.min,np.mean])
salariesDF_summary_by_teamID.columns = ["sum", "max", "min", "mean"]
print salariesDF_summary_by_teamID.head()


def bargraph(column): # column = sum, max, min, mean
	frequency = salariesDF_summary_by_teamID[column].sort_values(axis=0, ascending = False).head(10)
	objects = frequency.index
	y_pos = np.arange(len(objects))
	plt.bar(y_pos, frequency, align='center')
	plt.xticks(y_pos, objects)
	plt.ylabel('Number')
	plt.title("Top 10 {} of salaries by teamID".format(column))
	print "Top 10 {} of salaries by teamID".format(column)
	print frequency
	plt.show()

""" Bar graph of the number of players by teamID """
if False:
	bargraph("sum")
	bargraph("max")
	bargraph("min")
	bargraph("mean")

""" data by year """
salariesDF_by_year = salariesDF[["yearID","salary"]].groupby("yearID").agg([np.sum,np.max,np.min,np.mean])
salariesDF_by_year.columns = ["sum", "max", "min", "mean"]

if True:
	f, axarr = plt.subplots(4, sharex=True)
	axarr[0].set_title('Sum by year')
	axarr[0].plot(salariesDF_by_year.index, salariesDF_by_year["sum"])
	axarr[1].set_title('Maximum by year')
	axarr[1].plot(salariesDF_by_year.index, salariesDF_by_year["max"])
	axarr[2].set_title('Minimum by year')
	axarr[2].plot(salariesDF_by_year.index, salariesDF_by_year["min"])
	axarr[3].set_title('Mean by year')
	axarr[3].plot(salariesDF_by_year.index, salariesDF_by_year["mean"])
	plt.show()

""" Finding maximum year """
maxSalaryByYear = salariesDF_by_year["max"].argmax()
print "\nMaximum salary occurs in {}, $ {}\n".format(maxSalaryByYear, salariesDF_by_year["max"].loc[maxSalaryByYear])

""" Find player with the maximum in 2009 """
maxDFyear = salariesDF[salariesDF["yearID"]==2009]
maxPlayer2009 = maxDFyear[maxDFyear["salary"] == salariesDF_by_year["max"].loc[maxSalaryByYear]]
maxPlayerID = maxPlayer2009["playerID"].values[0]
print maxPlayerID
print "Detailed information of the player"
print maxPlayer2009, "\n"

""" maximum player's yearly graph """
maxPlayerDF = salariesDF[salariesDF["playerID"] == maxPlayerID]
print maxPlayerDF
if True:
	plt.plot(maxPlayerDF["yearID"], maxPlayerDF["salary"])
	plt.show()