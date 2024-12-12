pairs =[
["Roy","Lilina"],
["Roy","Marcus"],
["Roy","Wolt"],
["Roy","Cecilia"],
["Roy","Sophia"],
["Roy","Sue"],
["Roy","Shanna"],
["Roy","Larum"],
["Roy","Alen"],
["Roy","Lance"],
["Clarine","Klein"],
["Clarine","Rutger"],
["Clarine","Dieck"],
["Clarine","Lance"],
["Clarine","Dorothy"],
["Fae","Sophia"],
["Fae","Igrene"],
["Fae","Sue"],
["Fae","Niime"],
["Fae","Elffin"],
["Sin","Dayan"],
["Sin","Sue"],
["Sin","Fir"],
["Sin","Dorothy"],
["Sin","Zeiss"],
["Sue","Dayan"],
["Sue","Wolt"],
["Dayan","Yoder"],
["Dayan","Gonzalez"],
["Dayan","Rutger"],
["Barthe","Lilina"],
["Barthe","Ogier"],
["Barthe","Bors"],
["Barthe","Gwendolyn"],
["Barthe","Astolfo"],
["Bors","Lilina"],
["Bors","Gwendolyn"],
["Bors","Astolfo"],
["Bors","Ogier"],
["Gwendolyn","Lilina"],
["Gwendolyn","Ogier"],
["Gwendolyn","Astolfo"],
["Douglas","Elffin"],
["Douglas","Geese"],
["Douglas","Igrene"],
["Douglas","Perceval"],
["Douglas","Cecilia"],
["Douglas","Larum"],
["Wolt","Marcus"],
["Wolt","Alen"],
["Wolt","Lance"],
["Dorothy","Saul"],
["Dorothy","Perceval"],
["Dorothy","Yoder"],
["Klein","Perceval"],
["Klein","Dieck"],
["Klein","Elffin"],
["Klein","Thea"],
["Saul","Yoder"],
["Saul","Cecilia"],
["Saul","Igrene"],
["Saul","Elen"],
["Elen","Melady"],
["Elen","Zeiss"],
["Elen","Lugh"],
["Elen","Chad"],
["Yoder","Niime"],
["Yoder","Melady"],
["Chad","Lugh"],
["Chad","Raigh"],
["Chad","Cath"],
["Chad","Hugh"],
["Karel","Fir"],
["Karel","Bartre"],
["Karel","Rutger"],
["Karel","Zeiss"],
["Karel","Noah"],
["Fir","Bartre"],
["Fir","Noah"],
["Fir","Rutger"],
["Rutger","Dieck"],
["Dieck","Ward"],
["Dieck","Lot"],
["Dieck","Shanna"],
["Ogier","Lilina"],
["Ogier","Larum"],
["Garret","Lilina"],
["Garret","Geese"],
["Garret","Larum"],
["Garret","Cath"],
["Garret","Gonzalez"],
["Alen","Thea"],
["Alen","Marcus"],
["Alen","Lance"],
["Alen","Ward"],
["Lance","Marcus"],
["Lance","Lot"],
["Perceval","Cecilia"],
["Perceval","Elffin"],
["Perceval","Larum"],
["Igrene","Sophia"],
["Igrene","Astolfo"],
["Marcus","Lilina"],
["Astolfo","Lilina"],
["Ward","Shanna"],
["Ward","Lot"],
["Ward","Echidna"],
["Lot","Shanna"],
["Lot","Echidna"],
["Bartre","Gonzalez"],
["Bartre","Zeiss"],
["Bartre","Cath"],
["Lugh","Raigh"],
["Lugh","Hugh"],
["Lugh","Melady"],
["Lilina","Gonzalez"],
["Hugh","Niime"],
["Hugh","Raigh"],
["Hugh","Cath"],
["Niime","Raigh"],
["Niime","Sophia"],
["Raigh","Sophia"],
["Larum","Echidna"],
["Larum","Geese"],
["Juno","Thea"],
["Juno","Shanna"],
["Juno","Zelot"],
["Juno","Trec"],
["Juno","Noah"],
["Thea","Shanna"],
["Thea","Zelot"],
["Shanna","Zelot"],
["Zeiss","Melady"],
["Elffin","Cecilia"],
["Cath","Geese"],
["Melady","Trec"],
["Gonzalez","Echidna"],
["Gonzalez","Trec"],
["Noah","Zelot"],
["Noah","Trec"],
["Trec","Zelot"],
["Echidna","Geese"],
["Lilina","Cecilia"],
]


charsInOrder = [
"Roy",
"Marcus",
"Alen",
"Lance",
"Wolt",
"Bors",
"Merlinus",
"Elen",
"Dieck",
"Ward",
"Lot",
"Shanna",
"Chad",
"Lugh",
"Clarine",
"Rutger",
"Saul",
"Dorothy",
"Sue",
"Zelot",
"Trec",
"Noah",
"Astolfo",
"Lilina",
"Barthe",
"Ogier",
"Gwendolyn",
"Fir",
"Sin",
"Geese",
"Gonzalez",
"Klein",
"Thea",
"Larum",
"Elffin",
"Echidna",
"Bartre",
"Raigh",
"Cath",
"Melady",
"Perceval",
"Cecilia",
"Sophia",
"Igrene",
"Garret",
"Fae",
"Hugh",
"Zeiss",
"Douglas",
"Niime",
"Juno",
"Dayan",
"Yoder",
"Karel"]

charIDsDict = {}

i = 0
for char in charsInOrder:
    i += 1
    charIDsDict[char] = i

for pair in pairs:
    a = charIDsDict[pair[0]]
    b = charIDsDict[pair[1]]
    if a>b:
        pair = pair.reverse()

print(pairs)

categorizedPairs = {}
for char in charsInOrder:
    categorizedPairs[char] = []

for pair in pairs:
    categorizedPairs[pair[0]].append(pair[1])



finalCategorizedPairs = {}
for char in charsInOrder:
    finalCategorizedPairs[char] = []


keys = categorizedPairs.keys()
for char in keys:
    for i in range(len(charsInOrder)):
        if charsInOrder[i] in categorizedPairs[char]:
            finalCategorizedPairs[char].append(charsInOrder[i])

finalFinalReal = []
keys = finalCategorizedPairs.keys()
for char in keys:
    for char2 in finalCategorizedPairs[char]:
        finalFinalReal.append([char,char2])



keys = categorizedPairs.keys()
with open("output.txt","w") as wr:
    for pair in finalFinalReal:
        t = ["[\""+pair[0]+"\",\""+pair[1]+"\"],\n"]
        wr.writelines(t)