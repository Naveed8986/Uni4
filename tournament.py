import csv

rows = {}

with open(input("Input file name: "), 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		rows[row[0]] = list(map(int, row[1:]))


maxi = max([sum(val) for val in rows.values()])
winners = list(filter(lambda x: sum(x[1]) == maxi, rows.items()))

print("Winner/s: ")
for winner in winners:
	print("=> '" + winner[0] + "' with total " + str(sum(winner[1])) + " points earned!")
 
