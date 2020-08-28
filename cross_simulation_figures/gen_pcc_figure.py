from glob import glob
files = glob("./*/")
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
plt.rcParams["figure.figsize"] = (3.5,3.5)
i = 0
files.remove('./pair-wise/')
files.extend(glob("./pair-wise/*/"))
import sys
roll_vals_norm = []
pitch_vals_norm = []
x_vals_norm = []
y_vals_norm = []
alt_vals_norm = []
course_vals_norm = []
speed_vals_norm = []
climb_vals_norm = []

roll_vals_abnorm = []
pitch_vals_abnorm = []
x_vals_abnorm = []
y_vals_abnorm = []
alt_vals_abnorm = []
course_vals_abnorm = []
speed_vals_abnorm = []
climb_vals_abnorm = []

pcc_roll = []
pcc_pitch = []
pcc_x = []
pcc_y = []
pcc_alt = []
pcc_course = []
pcc_speed = []
pcc_climb = []

def mean(data):
    """Return the sample arithmetic mean of data."""
    if data == "undefined":
        return "undefined"
    n = len(data)
    if n < 1:
        raise ValueError("mean requires at least one data point")
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

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

def autolabel(rects, files):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0,
                " " + (files[idx][2:-5] if 'pair-wise' not in files[idx] else files[idx][2:-1]),
                ha='center', va='bottom', rotation=90)


for i in range(0,len(files)):
	print files[i]
	norm = files[i] +"normal/"
	abnorm = files[i] + "abnormal/"
	normal_csv =  open(norm + files[i][2:-1] + "_normal.csv") if 'pair-wise' not in files[i] else open(norm + files[i][12:-1] + "_normal.csv")
	abnormal_csv =  open(abnorm + files[i][2:-1] + "_abnormal.csv") if 'pair-wise' not in files[i] else open(abnorm + files[i][12:-1] + "_abnormal.csv")
	normal_lines = normal_csv.readlines()
	abnormal_lines = abnormal_csv.readlines()
	for j in range(0, min(len(normal_lines),len(abnormal_lines))):
		normal = normal_lines[j].split(',')
		abnormal = abnormal_lines[j].split(',')
		roll_vals_norm.append(float(normal[0]))
		roll_vals_abnorm.append(float(abnormal[0]))
		pitch_vals_norm.append(float(normal[1]))
		pitch_vals_abnorm.append(float(abnormal[1]))
		x_vals_norm.append(float(normal[2]))
		x_vals_abnorm.append(float(abnormal[2]))
		y_vals_norm.append(float(normal[3]))
		y_vals_abnorm.append(float(abnormal[3]))
		alt_vals_norm.append(float(normal[4]))
		alt_vals_abnorm.append(float(abnormal[4]))
		course_vals_norm.append(float(normal[5]))
		course_vals_abnorm.append(float(abnormal[5]))
		speed_vals_norm.append(float(normal[6]))
		speed_vals_abnorm.append(float(abnormal[6]))
		climb_vals_norm.append(float(normal[7]))
		climb_vals_abnorm.append(float(abnormal[7]))

	pcc_roll.append(pearson_correlation(roll_vals_norm,roll_vals_abnorm,ddof=0))
	pcc_pitch.append(pearson_correlation(pitch_vals_norm,pitch_vals_abnorm,ddof=0))
	pcc_x.append(pearson_correlation(x_vals_norm,x_vals_abnorm,ddof=0))
	pcc_y.append(pearson_correlation(y_vals_norm,y_vals_abnorm,ddof=0))
	pcc_alt.append(pearson_correlation(alt_vals_norm,alt_vals_abnorm,ddof=0))
	pcc_course.append(pearson_correlation(course_vals_norm,course_vals_abnorm,ddof=0))
	pcc_speed.append(pearson_correlation(speed_vals_norm,speed_vals_abnorm,ddof=0))
	pcc_climb.append(pearson_correlation(climb_vals_abnorm,speed_vals_abnorm,ddof=0))


xticks = [0, 1, 2, 3, 4, 5, 6]
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_roll)), pcc_roll, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Roll")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_pitch)), pcc_pitch, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Pitch")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_x)), pcc_x, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("X Position")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_y)), pcc_y, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Y Position")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_alt)), pcc_alt, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Altitude")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_course)), pcc_course, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Course")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_speed)), pcc_speed, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Speed (X,Y)")
plt.show()

fig, ax = plt.subplots()
bar_plot = plt.bar(range(len(pcc_climb)), pcc_climb, linestyle='-', color='b', tick_label=labels)
#autolabel(bar_plot, files)
#ax.axes.get_xaxis().set_visible(False)
plt.title("Speed (Z)")
plt.show()
