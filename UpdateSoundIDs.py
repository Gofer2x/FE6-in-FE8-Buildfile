import csv

csvData = []
with open('FE6toFE8Sounds.csv', mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        csvData.append(lines)

output = []

id = "dummy"

for item in csvData:
    name = item["Name"]

    if item["FE8 Target ID"] == "i":
        id = hex(int(id,16)+1).upper().replace("X","x")
    else:
        id = item["FE8 Target ID"]    

    define = ("#define "+name+" "+id+"\n")
    print(define)
    output.append(define)

with open("Definitions/IDs/SoundIDs.event","w") as write:
    write.writelines(output)

input("Done. Enter to exit program...")