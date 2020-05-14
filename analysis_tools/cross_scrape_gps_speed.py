

import sys 
import math

INFILE_1 = sys.argv[1]
INFILE_2 = sys.argv[2]

if (len(sys.argv) > 4):
	TIME_BEGIN_1 = float(sys.argv[3])
	TIME_END_1 = float(sys.argv[4])
	TIME_BEGIN_2 = float(sys.argv[5])
	TIME_END_2 = float(sys.argv[6])
else:
	TIME_BEGIN_1 = 0.0
	TIME_END_1 = float('inf')
	TIME_BEGIN_2 = 0.0
	TIME_END_2 = float('inf')


flight_log_1 = 0
flight_log_2 = 0
lines_1 = 0
lines_2 = 0

if ".data" in INFILE_1:
	flight_log_1 = open(INFILE_1)
	flight_log_2 = open(INFILE_2)
	lines_1 = flight_log_1.readlines()
	lines_2 = flight_log_2.readlines()
	csv_output = open("nps_rate_attitude.csv", "w")
	results_output = open("nps_rate_attitude.results", "w")
else:
	flight_log_1 = open(INFILE_1+".data")
	flight_log_2 = open(INFILE_2+".data")
	lines_1 = flight_log_1.readlines()
	lines_2 = flight_log_2.readlines()
	csv_output = open("nps_rate_attitude.csv", "w")
	results_output = open("nps_rate_attitude.results", "w")


def remove_out_of_bound_data(lines, t1, t2):
	new_data_points = []
	for i in lines:
		if float(i.split(' ')[0]) < t2 and t1 < float(i.split(' ')[0]):
			new_data_points.append(str(float(i.split(' ')[0]) - t1) + " " + i[i.index(' ')+1:])
			
	return new_data_points


def compute_pose_error(phi_1, psi_1, theta_1, phi_2, psi_2, theta_2):
	print "|\t\t\t\t\t\t|"
	ret_val = (((phi_1-phi_2)**2)+((psi_1-psi_2)**2)+((theta_1-theta_2)**2))**0.5
	print "|\t\tPOSE ERR: ", ret_val, " \t\t|"
	print "|\t\t\t\t\t\t|"
	return ret_val



new_data_points_1 = remove_out_of_bound_data(lines_1, TIME_BEGIN_1, TIME_END_1)
new_data_points_2 = remove_out_of_bound_data(lines_2, TIME_BEGIN_2, TIME_END_2)
desired_vals = []
actual_vals = []
pose_error_vals = []
position_error_vals = []
airdata_error_vals = []

def stddev(lst):
    mean = float(sum(lst)) / len(lst)
    return math.sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, lst))) / len(lst))

def run_average_report():
	print "************AVERAGE ERROR REPORT************"
	results_output.write("************AVERAGE ERROR REPORT************\n")
	averages = []
	values = []

	sum_var = 0
	avg_range = min(len(desired_vals), len(actual_vals))
	for j in range(avg_range):
		sum_var += abs(actual_vals[j]-desired_vals[j])
		values.append(abs(actual_vals[j] - desired_vals[j]))
	averages.append(sum_var/float(avg_range))


	print "VALUE\t\t\tMEAN\t\t\tSD"
	results_output.write("VALUE\t\t\tMEAN\t\t\tSD\n")
	
	print "SPEED_ERR\t\t\t", averages[0], "\t", stddev(values)
	results_output.write("SPEED_ERR\t\t\t" + str(averages[0]) +  "\t\t" + str(stddev(values)) +"\n")


def main():
	data_point_ctr_1 = 0
	for i in range(len(new_data_points_1)):
		line = new_data_points_1[i]
		if "GPS" == line.split(' ')[2]:
			data_point_ctr_1 += 1
			d_val_list = line.split(' ')

			# roll pitch yaw phi theta psi			
			d_time = float(d_val_list[0])
			d_speed = float(d_val_list[8])/100		#GPS->speed
			desired_vals.append(d_speed)

	data_point_ctr_2 = 0
	for i in range(len(new_data_points_2)):
		line = new_data_points_2[i]
		if "GPS" == line.split(' ')[2]:
			data_point_ctr_2 += 1
			a_val_list = line.split(' ')		
			
			# roll pitch yaw phi theta psi			
			a_time = float(d_val_list[0])
			a_speed = float(d_val_list[8])/100		#GPS->speed
			actual_vals.append(d_speed)

	#i = 0
	#while i < len(desired_vals) and i < len(actual_vals):
	#	print "|==============DATA POINT", i, "\t================|"
	#	print "|PARAM\t|\tDESIRED\t\t|\tACTUAL\t|"
	#	print "|SPEED\t|\t", d_speed, "\t| ", a_speed, "\t|"
	#	i += 1


main()
run_average_report()
