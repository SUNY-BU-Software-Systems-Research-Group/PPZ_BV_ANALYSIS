from glob import glob
files = glob("./*/")
i = 0
files.remove('./pair-wise/')
files.extend(glob("./pair-wise/*/"))
import sys

difference = ""
if (len(sys.argv) == 2):
	difference = sys.argv[1]
else:
	difference = "DIFF"


def distinction(normal,abnormal):
	if difference == "DIFF":
		return abs(normal-abnormal)
	elif difference == "P_ERR":
		if (normal == 0 and abnormal == 0):
			return 0
		elif (normal == 0):
			return None
		else:
			return abs(float(abs(normal-abnormal))/normal)

for i in range(0,len(files)):
	print files[i]
	norm = files[i] +"normal/"
	abnorm = files[i] + "abnormal/"
	normal_csv =  open(norm + files[i][2:-1] + "_normal.csv") if 'pair-wise' not in files[i] else open(norm + files[i][12:-1] + "_normal.csv")
	abnormal_csv =  open(abnorm + files[i][2:-1] + "_abnormal.csv") if 'pair-wise' not in files[i] else open(abnorm + files[i][12:-1] + "_abnormal.csv")
	normal_lines = normal_csv.readlines()
	abnormal_lines = abnormal_csv.readlines()
	output = open(files[i]+"difference.csv", "w")
	for j in range(0, min(len(normal_lines),len(abnormal_lines))):
		normal = normal_lines[j].split(',')
		abnormal = abnormal_lines[j].split(',')
		output.write(str(distinction(float(normal[0]), float(abnormal[0]))))
		output.write(",")
		output.write(str(distinction(float(normal[1]), float(abnormal[1]))))
		output.write(",")
		output.write(str(distinction(float(normal[2]), float(abnormal[2]))))
		output.write(",")
		output.write(str(distinction(float(normal[3]), float(abnormal[3]))))
		output.write(",")
		output.write(str(distinction(float(normal[4]), float(abnormal[4]))))
		output.write(",")
		output.write(str(distinction(float(normal[5]), float(abnormal[5]))))
		output.write(",")
		output.write(str(distinction(float(normal[6]), float(abnormal[6]))))
		output.write(",")
		output.write(str(distinction(float(normal[7]), float(abnormal[7]))))
		output.write(",")
		output.write("\n")
	#output.close()
