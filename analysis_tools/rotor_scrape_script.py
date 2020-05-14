

import sys 
import math

INFILE = sys.argv[1]
if (len(sys.argv) > 2):
	TIME_BEGIN = float(sys.argv[2])
	TIME_END = float(sys.argv[3])
else:
	TIME_BEGIN = 0.0
	TIME_END = float('inf')

if ".data" in INFILE:
	flight_log = open(INFILE)
	lines = flight_log.readlines()
	csv_output = open(INFILE[:-5]+".csv", "w")
	results_output = open(INFILE[:-5]+".results", "w")
else:
	flight_log = open(INFILE+".data")
	lines = flight_log.readlines()
	csv_output = open(INFILE+".csv", "w")
	results_output = open(INFILE+".results", "w")

def compute_positional_error(x_1, y_1, z_1, x_2, y_2, z_2):
	print "|\t\t\t\t\t\t|"
	ret_val = (((x_1-x_2)**2)+((y_1-y_2)**2)+((z_1-z_2)**2))**0.5
	print "|\t\tPOSITION ERR: ", ret_val," \t|"
	print "|\t\t\t\t\t\t|"
	return ret_val


def compute_pose_error(phi_1, psi_1, theta_1, phi_2, psi_2, theta_2):
	print "|\t\t\t\t\t\t|"
	ret_val = (((phi_1-phi_2)**2)+((psi_1-psi_2)**2)+((theta_1-theta_2)**2))**0.5
	print "|\t\tPOSE ERR: ", ret_val, " \t|"
	print "|\t\t\t\t\t\t|"
	return ret_val


def remove_out_of_bound_data():
	new_data_points = []
	for i in lines:
		if float(i.split(' ')[0]) < TIME_END and TIME_BEGIN < float(i.split(' ')[0]):
			new_data_points.append(i)
	return new_data_points

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
	values = [[],[],[],[],[],[],[],[]]
	for i in range(8):
		sum_var = 0
		for j in range(len(desired_vals)):
			sum_var += abs(actual_vals[j][i]-desired_vals[j][i])
			values[i].append(abs(actual_vals[j][i] - desired_vals[j][i]))
		averages.append(sum_var/float(len(actual_vals)))
		#print(averages[i])
	

	print "VALUE\t\t\tMEAN\t\t\tSD"
	results_output.write("VALUE\t\t\tMEAN\t\t\tSD\n")

	print "ROLL_ERR\t\t", averages[0], "\t\t", stddev(values[0])
	results_output.write("ROLL_ERR\t\t" + str(averages[0]) +  "\t\t" + str(stddev(values[0])) +"\n")

	print "YAW_ERR\t\t\t", averages[1],  "\t\t", stddev(values[1])
	results_output.write("YAW_ERR\t\t\t" + str(averages[1]) +  "\t\t" + str(stddev(values[1])) +"\n")

	print "PITCH_ERR\t\t", averages[2],  "\t\t", stddev(values[2])
	results_output.write("PITCH_ERR\t\t" + str(averages[2]) +  "\t\t" + str(stddev(values[2])) +"\n")

	print "POS_X_ERR\t\t", averages[3],  "\t\t", stddev(values[3])
	results_output.write("POS_X_ERR\t\t" + str(averages[3]) +  "\t\t" + str(stddev(values[3])) +"\n")

	print "POS_Y_ERR\t\t", averages[4],  "\t\t", stddev(values[4])
	results_output.write("POS_Y_ERR\t\t" + str(averages[4]) +  "\t\t" + str(stddev(values[4])) +"\n")

	print "ALT_ERR\t\t\t", averages[5],  "\t\t", stddev(values[5])
	results_output.write("ALT_ERR\t\t\t" + str(averages[5]) +  "\t\t" + str(stddev(values[5])) +"\n")

	print "CLIMB_ERR\t\t", averages[6],  "\t\t", stddev(values[6])
	results_output.write("CLIMB_ERR\t\t" + str(averages[6]) +  "\t\t" + str(stddev(values[6])) +"\n")

	print "SPEED_ERR\t\t", averages[7],  "\t\t", stddev(values[7])
	results_output.write("SPEED_ERR\t\t" + str(averages[7]) +  "\t\t" + str(stddev(values[7])) +"\n")

	print "POSE_ERR\t\t", sum(pose_error_vals)/len(pose_error_vals), "\t\t", stddev(pose_error_vals)
	results_output.write( "POSE_ERR\t\t" + str(sum(pose_error_vals)/len(pose_error_vals)) + "\t\t" + str(stddev(pose_error_vals)) + "\n")

	print "POSITION_ERR\t\t", sum(position_error_vals)/len(position_error_vals), "\t\t", stddev(position_error_vals)
	results_output.write( "POSITION\t\t" + str(sum(position_error_vals)/len(position_error_vals)) + "\t\t" + str(stddev(position_error_vals)) + "\n")
	
		
			

def main():
	data_point_ctr = 0
	
	new_data_points = remove_out_of_bound_data()
	for i in range(len(new_data_points)):
		line = new_data_points[i]
		if "ROTORCRAFT_FP" in line:
			data_point_ctr += 1
			d_x = float(line.split(' ')[12])*0.0039063		#ROTORCRAFT_FP->carrot_east
			d_y = float(line.split(' ')[13])*0.0039063		#ROTORCRAFT_FP->carrot_north
			d_altitude = float(line.split(' ')[14])*0.0039063	#ROTORCRAFT_FP->carrot_up
			d_roll = float(line.split(' ')[9])*0.0139882		
			d_pitch = float(line.split(' ')[11])*0.0139882
			d_yaw = float(line.split(' ')[10])*0.0139882
			d_climb = float(line.split(' ')[6])*0.0000019
			d_airspeed = (float(line.split(' ')[6]) + float(line.split(' ')[7]))*0.0000019
			j = i+1


			a_x = float(line.split(' ')[3])*0.0039063		#ROTORCRAFT_FP->east	
			a_y = float(line.split(' ')[4])*0.0039063		#ROTORCRAFT_FP->north
			a_altitude = float(line.split(' ')[5])*0.0039063	#ROTORCRAFT_FP->up
			
			while j < len(new_data_points) and new_data_points[j].split(' ')[2] != "NPS_SPEED_POS":
				j+=1
			if (j >= len(new_data_points)):
				return
			#a_x = float(new_data_points[j].split(' ')[9])
			#a_y = float(new_data_points[j].split(' ')[10])
			#a_altitude = float(new_data_points[j].split(' ')[11])
			a_climb = float(new_data_points[j].split(' ')[8])
			a_airspeed = float(new_data_points[j].split(' ')[6]) + float(new_data_points[j].split(' ')[7])
			j = i+1
			while  j < len(new_data_points) and new_data_points[j].split(' ')[2] != "NPS_RATE_ATTITUDE":
				j+=1
			if (j >= len(new_data_points)):
				return

			a_roll =  float(new_data_points[j].split(' ')[6])
			a_pitch =  float(new_data_points[j].split(' ')[8])
			a_yaw =  float(new_data_points[j].split(' ')[7])
			
			print "|==============DATA POINT", data_point_ctr, "\t================|"
			print "|PARAM\t|\tDESIRED \t|\tACTUAL\t|"
			print "|ROLL\t|\t", d_roll, "\t| ", a_roll, "\t|"
			print "|PITCH\t|\t", d_pitch, "\t| ", a_pitch, "\t|"
			print "|YAW\t|\t", d_yaw, "\t| ", a_yaw, "\t|"
			pose_error = compute_pose_error( d_roll, d_pitch, d_yaw, a_roll, a_pitch, a_yaw)
			print "|POS_X\t|\t", d_x, "\t| ", a_x, "\t|"
			print "|POS_Y\t|\t", d_y, "\t| ", a_y, "\t|"
			print "|POS_Z\t|\t", d_altitude, "\t| ", a_altitude, "  \t|"
			position_error = compute_positional_error( d_x, d_y, d_altitude,a_x, a_y, a_altitude)
			print "|CLIMB\t|\t", d_climb, "\t| ", a_climb, "\t|"
			print "|SPEED\t|\t", d_airspeed, "\t| ", a_airspeed, "\t|"
			
			desired_vals.append((d_roll, d_pitch, d_yaw, d_x, d_y, d_altitude, d_climb, d_airspeed))
			actual_vals.append(( a_roll, a_pitch, a_yaw, a_x, a_y, a_altitude, a_climb, a_airspeed))
			pose_error_vals.append(pose_error)
			position_error_vals.append(position_error)
		
			csv_output.write(str(d_roll)+ ","+ str(d_pitch) + "," + str(d_yaw) + "," + str(d_x)+ "," + str(d_y) + "," + str(d_altitude) + "," + str(d_climb) + "," + str(d_airspeed) + ',' + str(pose_error)+ ","+ str(position_error))
			csv_output.write("\n")


main()
flight_log.close()		
csv_output.close()
run_average_report()
