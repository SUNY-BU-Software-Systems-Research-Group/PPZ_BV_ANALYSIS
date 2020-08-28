from glob import glob
import numpy as np
import matplotlib.pyplot as plt
files = glob("./*/")
i = 0
files.remove('./pair-wise/')
files.extend(glob("./pair-wise/*/"))
plt.rcParams["figure.figsize"] = (3,2.3)

roll_vals = []
pitch_vals = []
x_vals = []
y_vals = []
alt_vals = []
course_vals = []
speed_vals = []
climb_vals = []


def autolabel(rects, files):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width(), 0,
                " " + (files[2:-5] if 'pair-wise' not in files else files[2:-1]),
                ha='center', va='bottom', rotation=45)

def pearson_correlation(x,y,ddof=0):
	mean_x = mean(x)
	mean_y = mean(y)
	n = len(x)
	if ddof == 0:
		scale_denom = 1
		scale_nom = 1
	else:
		ddof = 1
		scale_denom = n-1
		scale_nom = n
	denom = scale_denom*stddev(x,ddof)*stddev(y,ddof)
	if denom == 0:
		return "undefined"
	mean_xy = mean([x * y for x, y in zip(x,y)])
	return abs((scale_nom*(mean_xy - (mean_x * mean_y))) / denom)


for i in range(0,len(files)):
	input_file = open(files[i]+"stats.csv")
	normal_means = []
	normal_stddevs = []
	lines = input_file.readlines()
	means_str = lines[0].split(',')
	stddevs_str = lines[1].split(',')

	for j in range(8):
		normal_means.append(float(means_str[j]))
		normal_stddevs.append(float(stddevs_str[j]))
		
		
	
	roll_vals.append((normal_means[0], normal_stddevs[0], files[i]))
	pitch_vals.append((normal_means[1], normal_stddevs[1], files[i]))
	x_vals.append((normal_means[2], normal_stddevs[2], files[i]))
	y_vals.append((normal_means[3], normal_stddevs[3], files[i]))
	alt_vals.append((normal_means[4], normal_stddevs[4], files[i]))
	course_vals.append((normal_means[5], normal_stddevs[5], files[i]))
	speed_vals.append((normal_means[6], normal_stddevs[6], files[i]))
	climb_vals.append((normal_means[7], normal_stddevs[7], files[i]))


xticks = [0, 1, 2, 3, 4, 5, 6]
labels = ['G', 'F', 'E', 'D', 'C', 'B','A']
for i in range(len(files)):
	#xticks.append(i)
	files[i] = files[i][2:-1] if 'pair-wise' not in files[i] else files[i][12:-1]

fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, roll_vals[i][0]/100, height=0.45, linestyle='-', color='b', xerr=roll_vals[i][1]/100)
plt.yticks(xticks, labels,  rotation=0)
plt.title("Roll")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()


fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, pitch_vals[i][0], height=0.45, linestyle='-', color='b', xerr=pitch_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Pitch")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()


fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, x_vals[i][0], height=0.45, linestyle='-', color='b', xerr=x_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("X Position")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()



fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, y_vals[i][0], height=0.45, linestyle='-', color='b', xerr=y_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Y Position")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()



fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, alt_vals[i][0], height=0.45, linestyle='-', color='b', xerr=alt_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Altitude")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()


fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, course_vals[i][0], height=0.45, linestyle='-', color='b', xerr=course_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Course")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()


fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, speed_vals[i][0], height=0.45, linestyle='-', color='b', xerr=speed_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Speed (X,Y)")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()

fig, ax = plt.subplots()
for i in range(len(files)):
	b1 = ax.barh(i, climb_vals[i][0], height=0.45, linestyle='-', color='b', xerr=climb_vals[i][1])
plt.yticks(xticks, labels,  rotation=0)
plt.title("Speed (X,Y)")
#ax.axes.get_yaxis().set_visible(False)
#plt.xlim(left=0)
ax.set_xscale('log', basex=10)
#plt.subplots_adjust(left=0.55)
plt.show()
