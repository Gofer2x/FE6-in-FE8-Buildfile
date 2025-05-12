import shutil, argparse

# Takes array of strings starting with the MultiLine marker and ending with the MultiLineEnd marker (inclusive) as input.
def formatMultiLine(data):

    # Remove comment slashes and newlines.
    processedData = []
    for item in data:
        processedData.append(item.strip()[2:])

    #The name and arguments are in the second line.
    nameAndArgs = processedData[1]

    # Instructions are everything except the first two and the last line.
    multiLineInstructions = processedData[2:-1]
    oneLineInstructions = " ; ".join(multiLineInstructions)

    oneLine = (f"#define {nameAndArgs} \"{oneLineInstructions}\"\n")
    return oneLine

# Takes an .event file's contents in an array of string as input.
def findMultiLines(data):

    oneLinesToInsert = []
    currentLineIndex = 0
    while currentLineIndex != len(data):
        line = data[currentLineIndex]

        # Match if the 2nd (comment //) to len(marker)+2 characters are the MultiLineStart marker.
        if line.lower().strip() == multiLineStartMarker.lower():
            multiLineStartIndex = currentLineIndex
            print(f"Found MultiLineStart at line {multiLineStartIndex}.")

            # Look for MultiLineEnd marker starting at current index.
            for j in range(multiLineStartIndex,len(data)):

                # Match if the 2nd (comment //) to len(marker)+2 characters are the MultiLineEnd marker.
                if data[j].lower().strip() == multiLineEndMarker.lower():
                    multiLineEndIndex = j
                    print(f"Found MultiLineEnd at line {multiLineEndIndex}.")
                    break
            oneLine = formatMultiLine(data[multiLineStartIndex:multiLineEndIndex+1])
            # We insert the OneLine one line *after* the MultiLineEnd line.
            toInsertIndex = multiLineEndIndex+1
            # First element in array is the line index where to insert the OneLine, the second is the actual OneLine string.
            oneLinesToInsert.append([toInsertIndex,oneLine])
            #Increase index by however long the MultiLine was.
            currentLineIndex += multiLineEndIndex-multiLineStartIndex+2


        # No MultiLineStart found, increase index by 1.
        else:
            currentLineIndex += 1
    return oneLinesToInsert

# Takes a filepath and array of index+string pairs to insert MultiLines into a file.
def insertMultiLines(inputPath,oneLinesToInsert):
    print(f"Making backup of {inputPath}.")
    shutil.copyfile(inputPath,inputPath+".bak")
    with open(inputPath,"r") as r:
        data = r.readlines()
    for oneLinePair in oneLinesToInsert:
        data[oneLinePair[0]] = oneLinePair[1]
        print(f"Inserting OneLine definition at line {oneLinePair[0]}.")
    print(f"Saving processed {inputPath}.")
    with open(inputPath,"w") as w:
        w.writelines(data)

def doProcessing(inputPath):
    with open(inputPath,"r") as r:
        data = r.readlines()
    oneLinesToInsert = findMultiLines(data)
    if len(oneLinesToInsert) != 0:
        insertMultiLines(inputPath,oneLinesToInsert)
    else:
        print(f"No MultiLines found in {inputPath}. Exiting.")
        exit()

parser = argparse.ArgumentParser(description='Folds commented multi-line Event Assembler defines into single line ones that can be used.')
parser.add_argument('input', type=str, help='Path of the .event file to process.')
parser.add_argument('--startMarker', type=str, default="//MultiLineStart", help='Strin to look for to detect the start of a MultiLine.')
parser.add_argument('--endMarker', type=str, default="//MultiLineEnd", help='Strin to look for to detect the end of a MultiLine.')
args = parser.parse_args()

multiLineStartMarker = args.startMarker
multiLineEndMarker = args.endMarker
doProcessing(args.input)