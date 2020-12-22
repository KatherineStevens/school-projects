# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Katherine Stevens
# Section: 462
# Assignment: Lab9b_Act3.py
# Date: 27 October 2020
from math import *
# open the csv file for reading
file = open("WeatherData.csv", "r")

list2 = []
# read the csv file and compute
mylist = file.readlines()
for i in range(len(mylist)):
    mylist[i] = mylist[i].strip()
    l = mylist[i].split(",")
    list2.append(l)
#print(mylist)
#print(list2)
#convert to int and float
for i in range(1,len(list2)):
    for j in range(1,14):
        list2[i][j] = float(list2[i][j])
#print(list2)

#loop for max
#   a. maximum temp seen over the 3 yr period

max = list2[1][1]
for i in range(1,len(list2)):
    if list2[i][1] > max:
        max = list2[i][1]
#print(max)


#   b. minimum temp seen over the 3 yr period

min = list2[1][3]
for i in range(1,len(list2)):
    if list2[i][3] < min:
        min = list2[i][3]
#print(min)

#   c. avg daily precipitation over the 3 yr period (2 dec places)
sum = 0
for i in range(1,len(list2)):
    sum += list2[i][13]
avg_prec = sum / (len(list2)-1)
#print(avg_prec)
#output results in console

print("3-year maximum temperature:", int(max), "F")
print("3-year minimum temperature:", int(min), "F")
print("3-year average precipitation: %.2f" %avg_prec, "inches\n")


#   take input month and year
month = input("Enter a month: ")
year = input("Enter a year: \n")
print("For ", month," ", year, ":", sep="")
dict = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}
if month in dict:
    month_number = dict[month]
    
# for that month
#       a. calc avg of low temps  (1 dec)
total = 0
low = 0
for i in range(1, len(list2)):
    date = list2[i][0].split("/")
    #print(date)
    if date[2] == year and date[0] == month_number:
        low += list2[i][3]
        total += 1
avg_low = low / total
print("Average low temperature: %.1f" %avg_low, "F")

#       b. calc % of days when avg humidity below 75% (1 dec)
humidity_number = 0
total_humidity = 0
for i in range(1, len(list2)):
    date = list2[i][0].split("/")
    if date[2] == year and date[0] == month_number:
        total_humidity += 1
        if list2[i][8] < 75:
            humidity_number += 1
humidity_percent = (humidity_number / total_humidity) * 100

per_string = "%.1f" % humidity_percent + "%"
print("Percentage of days with average humidity below 75%:", per_string) 

precipitation_count = 0
num_days = 0
var = 0
#       c. calc mean and standard dev of daily precipitation levels (4 dec)
for i in range(1, len(list2)):
    date = list2[i][0].split("/")
    if date[2] == year and date[0] == month_number:
        precipitation_count += list2[i][13]
        num_days += 1
mean = precipitation_count / num_days

for i in range(1, len(list2)):
    date = list2[i][0].split("/")
    if date[2] == year and date[0] == month_number:
        var += ((list2[i][13] - mean) ** 2)
        
stan_dev = sqrt(var / (num_days))
        
print("Mean daily precipitation: %.4f" %mean, "inches")
print("Standard deviation of daily precipitation: %.4f" %stan_dev, "inches")
        
        

file.close()














