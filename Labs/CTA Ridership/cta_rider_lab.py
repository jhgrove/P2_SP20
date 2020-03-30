"""
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s).
   Just add a comment here to explain. (2pts)
"""

import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)

headers = data.pop(0)
print(headers)

years1 = [x[0] for x in data]
bus1 = [x[1] for x in data]
rail1 = [x[3] for x in data]
total1 = [x[4] for x in data]

years = years1[-10:]
bus = bus1[-10:]
rail = rail1[-10:]
total = total1[-10:]

print(years)
print(bus)
print(rail)
print(total)

xxx = years[bus]
xxx = [int(x) for x in xxx]
print(xxx)

yyy = years[bus]
yyy = [int(x) for x in yyy]

# plt.plot(month_numbers, my_library)  # plots line graph
plt.plot(years, xxx, color='darkgreen', label='Bus')  # plots a line graph
plt.plot(years, yyy, color='blue', label='Rail')

# plt.xticks(month_numbers, month_names, rotation=45)  # replaces the shown values on the graph axis
plt.axis([-1, 10, 0, 16000])
plt.title("Title", fontsize=20)
plt.xlabel('Years')
plt.ylabel('Ridership')
plt.legend()

# axis
# labels
# title
# legend (label plots)

plt.show()
