from glob import glob
import numpy as np
files = glob("./*/")
i = 0
files.remove('./pair-wise/')

files.extend(glob("./pair-wise/*/"))

for i in range(0,len(files)):
	input_file = open(files[i]+"difference.csv")
	output_file = open(files[i]+"stats.csv", "w")
	normal_data = [[],[],[],[],[],[],[],[],[],[]]
	for line in input_file.readlines():
		line_split = line.split(',')
		for j in range(8):
			if (line_split[j] != "None"):
				normal_data[j].append(float(line_split[j]))

	output_file.write(str(float(np.mean(normal_data[0]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[1]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[2]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[3]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[4]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[5]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[6]))))
	output_file.write(",")
	output_file.write(str(float(np.mean(normal_data[7]))))
	output_file.write("\n")
	
	output_file.write(str(float(np.std(normal_data[0]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[1]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[2]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[3]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[4]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[5]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[6]))))
	output_file.write(",")
	output_file.write(str(float(np.std(normal_data[7]))))
	output_file.write("\n\n")
		
	
	
	
