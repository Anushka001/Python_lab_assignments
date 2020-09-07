# Write a Python program to convert month name to a number of days.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
name_of_month = input("Enter the name of Month: ")

if name_of_month == "February":
	print("Number of days in this month: 28 or 29 days")
elif name_of_month in ("April", "June", "September", "November"):
	print("Number of days in this month: 30 days")
elif name_of_month in ("January", "March", "May", "July", "August", "October", "December"):
	print("Number of days in this month: 31 days")
else:
	print("Wrong month name") 