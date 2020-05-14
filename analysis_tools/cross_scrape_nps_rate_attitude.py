

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
	values = [[],[],[],[],[],[]]
	for i in range(6):
		sum_var = 0
		avg_range = min(len(desired_vals), len(actual_vals))
		for j in range(avg_range):
			sum_var += abs(actual_vals[j][i]-desired_vals[j][i])
			values[i].append(abs(actual_vals[j][i] - desired_vals[j][i]))
		averages.append(sum_var/float(len(actual_vals)))
	

	print "VALUE\t\t\tMEAN\t\t\tSD"
	results_output.write("VALUE\t\t\tMEAN\t\t\tSD\n")
	
	print "P_ERR\t\t\t", averages[0], "\t", stddev(values[0])
	results_output.write("P_ERR\t\t\t" + str(averages[0]) +  "\t\t" + str(stddev(values[0])) +"\n")

	print "Q_ERR\t\t\t", averages[1],  "\t", stddev(values[1])
	results_output.write("Q_ERR\t\t\t" + str(averages[1]) +  "\t\t" + str(stddev(values[1])) +"\n")

	print "R_ERR\t\t\t", averages[2],  "\t", stddev(values[2])
	results_output.write("R_ERR\t\t\t" + str(averages[2]) +  "\t\t" + str(stddev(values[2])) +"\n")

	print "ROLL_ERR\t\t", averages[3], "\t", stddev(values[3])
	results_output.write("ROLL_ERR\t\t" + str(averages[3]) +  "\t\t" + str(stddev(values[3])) +"\n")

	print "YAW_ERR\t\t\t", averages[4],  "\t", stddev(values[4])
	results_output.write("YAW_ERR\t\t\t" + str(averages[4]) +  "\t\t" + str(stddev(values[4])) +"\n")

	print "PITCH_ERR\t\t", averages[5],  "\t", stddev(values[5])
	results_output.write("PITCH_ERR\t\t" + str(averages[5]) +  "\t\t" + str(stddev(values[5])) +"\n")



def main():
	data_point_ctr_1 = 0
	for i in range(len(new_data_points_1)):
		line = new_data_points_1[i]
		if "NPS_RATE_ATTITUDE" in line:
			data_point_ctr_1 += 1
			d_val_list = line.split(' ')

			# roll pitch yaw phi theta psi			
			d_time = float(d_val_list[0])
			d_p = float(d_val_list[3])		#NPS_RATE_ATTITUDE->p
			d_q = float(d_val_list[4])		#NPS_RATE_ATTITUDE->q
			d_r = float(d_val_list[5])		#NPS_RATE_ATTITUDE->r		
			d_roll = float(d_val_list[6])		#NPS_RATE_ATTITUDE->phi
			d_pitch = float(d_val_list[7])		#NPS_RATE_ATTITUDE->theta
			d_yaw = float(d_val_list[8])		#NPS_RATE_ATTITUDE->psi
			desired_vals.append((d_p,d_q,d_r, d_roll, d_pitch, d_yaw))

	data_point_ctr_2 = 0
	for i in range(len(new_data_points_2)):
		line = new_data_points_2[i]
		if "NPS_RATE_ATTITUDE" in line:
			data_point_ctr_2 += 1
			a_val_list = line.split(' ')		
			
			# roll pitch yaw phi theta psi			
			a_time = float(d_val_list[0])
			a_p = float(d_val_list[3])		 #NPS_RATE_ATTITUDE->p
			a_q = float(d_val_list[4])	  	 #NPS_RATE_ATTITUDE->q
			a_r = float(d_val_list[5])		 #NPS_RATE_ATTITUDE->r		
			a_roll = float(d_val_list[6])		 #NPS_RATE_ATTITUDE->phi
			a_pitch = float(d_val_list[7])		 #NPS_RATE_ATTITUDE->theta
			a_yaw = float(d_val_list[8])		 #DESIRED->course (or Yaw/psi)	
			actual_vals.append((a_p, a_q, a_r, a_roll, a_pitch, a_yaw))


	i = 0
	while i < len(desired_vals) and i < len(actual_vals):
		print "|==============DATA POINT", i, "\t================|"
		print "|PARAM\t|\tDESIRED\t\t|\tACTUAL\t|"
		print "|P\t|\t", d_roll, "\t| ", a_roll, "\t|"
		print "|Q\t|\t", d_pitch, "\t| ", a_pitch, "\t|"
		print "|R\t|\t", d_yaw, "\t| ", a_yaw, "\t| "
		print "|ROLL\t|\t", d_roll, "\t| ", a_roll, "\t|"
		print "|PITCH\t|\t", d_pitch, "\t| ", a_pitch, "\t|"
		print "|YAW\t|\t", d_yaw, "\t| ", a_yaw, "\t| "
		pose_error = compute_pose_error( d_roll, d_pitch, d_yaw, a_roll, a_pitch, a_yaw)
		pose_error_vals.append(pose_error)
		i += 1


main()
run_average_report()
