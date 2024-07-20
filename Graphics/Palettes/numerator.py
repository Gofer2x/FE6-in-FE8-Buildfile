with open("input not numerated.txt", "r") as reader:
	data = reader.readlines()

output = []

i = 1
for line in data:
	if ("{i}") in line:
		line = line.replace("{i}","{"+str(i)+"}")
		i += 1
	output.append(line)

with open("Input.txt", "w") as writer:
	writer.writelines(output)