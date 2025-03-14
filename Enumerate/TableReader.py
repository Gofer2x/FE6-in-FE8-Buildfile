import csv

filepaths = [
    "../Tables/NightmareModules/Character and Class/CharacterTable.csv",
    "../Tables/NightmareModules/Character and Class/ClassTable.csv",
    "../Tables/NightmareModules/Item/ItemTable.csv"
]



for filepath in filepaths:

    fields = []
    rows = []


    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    if "CharacterTable" in filepath:
        valueType = "Character"
    elif "ClassTable" in filepath:
        valueType = "Class"
    elif "ItemTable" in filepath:
        valueType = "Item"


    values = []
    for row in rows:
        values.append(row[0])
    blankCounter = 1
    if valueType == "Item" or valueType == "Class":
        values = values[1:]
    values[0] = values[0]+" 1"
    for i in range(len(values)):
        
        if values[i] == "":
            values[i] = "Blank"+valueType+str(blankCounter)
            blankCounter += 1
        values[i] = values[i]+"\n"

    

    with open(valueType+"IDs.txt",'w') as write:
        write.writelines(values)
    print("Writing "+valueType+"IDs.txt")

#input("Enter to exit...")