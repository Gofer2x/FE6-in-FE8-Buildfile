import csv, os, time, sys

ENUMERATE = "Tools\\Enumerate\\Enumerate.py"

# Value types that have an invalid first item in the table.
invalidFirstItemTypes = [
    "Item",
    "Class"
]

# Value types that start their valid indexes at 0.
zeroIndexedTypes = [
    "Chapter"
]

inputPath = sys.argv[1]
outputPath = sys.argv[2]
valueType = sys.argv[3]

filename = os.path.split(inputPath)[1].replace(".csv","")


fields = []
rows = []

with open(inputPath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

values = []
for row in rows:
    values.append(row[0])


blankCounter = 1

# Item and Class tables have an invalid first item
if valueType in invalidFirstItemTypes:
    values = values[1:]

# First value as 1
if valueType in zeroIndexedTypes:
    values[0] = values[0]+" 0"
else:
    values[0] = values[0]+" 1"
for i in range(len(values)):
    
    # Replace the empty values with "BlankVALUE"
    if values[i] == "":
        values[i] = "Blank"+valueType+str(blankCounter)
        blankCounter += 1
    values[i] = values[i]+"\n"

# File to use with Enumerator
tempFilePath = "Temp"+filename+".txt"

print(f"Writing {tempFilePath}")
with open(tempFilePath,'w') as write:
    write.writelines(values)

print(f"Running Enumerator on {tempFilePath}")
os.system('%s %s %s' % (ENUMERATE, tempFilePath, outputPath))
os.remove(tempFilePath)

print("Exiting.")
time.sleep(1)