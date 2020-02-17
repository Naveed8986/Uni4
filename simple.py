
# Step 1: Reading contents from file

import csv

# creating a blank dictionary
rows = {}

fp = open('Teams1.txt', 'r')		# opening file in read mode
csvreader = csv.reader(fp)		# parsing the contents as csv

for row in csvreader:			
	rows[row[0]] = list(map(int, row[1:]))	# team name as keys and points as values

fp.close()				# closing the file pointer




# Step 2: Finding out the maximum total points earned by any team in the tournament 

maxi = 0
for name, points in rows.items():
	total = sum(points)		# adding up all the points
	if total > maxi:		
		maxi = total		




# Step 3: Declaring winner who has gained the maximum total points "maxi"

for name, points in rows.items():
	total = sum(points)
	if total == maxi:		# checking for total points = maxi
		print(name + " is the winner with total " + str(total) + " points earned!")


