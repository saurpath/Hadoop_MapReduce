import sys

valid_quality_values = [0,1,4,5,9]

for line in sys.stdin:
    line = line.strip()
    yearMonthDay = int(line[15:23])
    temperature = int(line[87:92])
    quality = int(line[92])
    if ((temperature != 9999) and (temperature != -9999) and (quality in valid_quality_values)):
        print(f"{yearMonthDay}\t{temperature}")
