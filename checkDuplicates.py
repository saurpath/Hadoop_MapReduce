import sys

with open("temperatureResults","r") as file:
	data = file.readlines()

dates = []
for line in data:
	date,temperature = line.split("\t")
	if date in dates:
		print("Validation Failed!")
		sys.exit(1);
	else:
		dates.append(date)
print("Validation Passed!")
