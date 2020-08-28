from glob import glob
import numpy as np
files = glob("./*/")
i = 0
files.remove('./pair-wise/')
files.extend(glob("./pair-wise/*/"))




for i in range(0,len(files)):
	print files[i]
	norm = files[i] +"normal/"
	abnorm = files[i] + "abnormal/"

	#PARSE "NORMAL" FILES
	output =  open(norm + files[i][2:-1] + "_normal.csv", 'w') if 'pair-wise' not in files[i] else open(norm + files[i][12:-1] + "_normal.csv", 'w')
	"""if ('pair-wise' not in files[i]):
		output = open(norm + files[i][2:-1] + "_normal.csv", 'w')
	else:
		output = open(norm + files[i][12:-1] + "_normal.csv", 'w')"""
	for file_index in range(1,6):
		f = None
		if ('pair-wise' not in files[i]):
			f = open(norm + files[i][2:-1] + "_normal_"+str(file_index)+".data")
		else:
			f = open(norm + files[i][12:-1] + "_normal_"+str(file_index)+".data")
		j = 0
		lines = f.readlines()
		

		UTM_EAST = None
		UTM_NORTH = None
		UTM_HEIGHT = None
		for l in lines:
			if ("NAVIGATION_REF" == l.split(' ')[2]):
				UTM_EAST = float(l.split(' ')[3])
				UTM_NORTH =  float(l.split(' ')[4])
				UTM_HEIGHT = float(l.split(' ')[6])
		if UTM_EAST == None:
			for l in lines:
				if ("GPS_INT" == l.split(' ')[2]):
					UTM_EAST = float(l.split(' ')[3])/100
					UTM_NORTH =  float(l.split(' ')[4])/100
					UTM_HEIGHT = float(l.split(' ')[5])/100
					print UTM_HEIGHT
					break

		while j < len(lines):
			line = lines[j]
			log_item = []
			if ("ATTITUDE" == line.split(' ')[2] or "NPS_RATE_ATTITUDE" == line.split(' ')[2]):
				curr_index = j
				if ("ATTITUDE" == line.split(' ')[2]):
					ATTITUDE_phi = line.split(' ')[3]					#ROLL
					log_item.append(float(ATTITUDE_phi)*57.3)
					ATTITUDE_theta = line.split(' ')[4]
					log_item.append(float(ATTITUDE_theta)*57.3)				#PITCH
				else:
					NPS_RATE_ATTITUDE_phi = line.split(' ')[6]				#ROLL
					log_item.append(float(NPS_RATE_ATTITUDE_phi))
					NPS_RATE_ATTITUDE_theta = line.split(' ')[7]
					log_item.append(float(NPS_RATE_ATTITUDE_theta))				#PITCH
				j = curr_index+1
				while j < len(lines):
					line = lines[j]
					if ("GPS" == line.split(' ')[2]):
						GPS_utm_east = line.split(' ')[4]
						log_item.append((float(GPS_utm_east)/100)-UTM_EAST)		#X
						GPS_utm_north = line.split(' ')[5]
						log_item.append((float(GPS_utm_north)/100)-UTM_NORTH)		#Y
						GPS_alt = line.split(' ')[7]
						log_item.append(float(GPS_alt)/1000)				#alt
						GPS_course = line.split(' ')[6]
						log_item.append(float(GPS_course)/10)				#Course
						GPS_speed = line.split(' ')[8]
						log_item.append(float(GPS_speed)/100)				#Speed
						GPS_climb = line.split(' ')[9]
						log_item.append(float(GPS_climb)/100)				#Climb
						j = len(lines)
					elif ("GPS_INT" == line.split(' ')[2]):
						GPS_INT_ecef_x = line.split(' ')[3]				#X
						log_item.append((float(GPS_INT_ecef_x)/100)-UTM_EAST)
						GPS_INT_ecef_y = line.split(' ')[4]				#Y
						log_item.append((float(GPS_INT_ecef_y)/100)-UTM_NORTH)
						GPS_INT_alt = line.split(' ')[5]
						log_item.append((float(GPS_INT_alt)/100)-UTM_HEIGHT)		#Alt

						if (float(line.split(' ')[10]) == 0):
							if float(line.split(' ')[11]) == 0:
								GPS_INT_course = 0
								log_item.append(GPS_INT_course)			#Course
							else:
								if float(line.split(' ')[11]) > 0:
									GPS_INT_course = 90
									log_item.append(GPS_INT_course)		#Course
								else:
									GPS_INT_course = 180
									log_item.append(GPS_INT_course)		#Course
						else:
							GPS_INT_course = np.arctan(float(line.split(' ')[11])/float(line.split(' ')[10]))
							log_item.append(GPS_INT_course)				#Course
				
						GPS_INT_speed = float(line.split(' ')[10])+float(line.split(' ')[11])
						log_item.append(float(GPS_INT_speed)/100)			#Speed
						GPS_INT_climb = line.split(' ')[12]
						log_item.append(float(GPS_INT_climb)/100)			#Climb
						j = len(lines)
					j+=1
				j = curr_index+1
				while j < len(lines):
					line = lines[j]
					if ("DESIRED" == line.split(' ')[2]):
						DESIRED_roll = line.split(' ')[3]
						log_item.append(float(DESIRED_roll)*57.3)			#ROLL
						DESIRED_pitch = line.split(' ')[4]
						log_item.append(float(DESIRED_pitch)*57.3)			#PITCH
						DESIRED_x = line.split(' ')[6]
						log_item.append(float(DESIRED_x))				#X
						DESIRED_y = line.split(' ')[7]
						log_item.append(float(DESIRED_y))				#Y
						DESIRED_alt = line.split(' ')[8]
						log_item.append(float(DESIRED_alt))				#Alt
						DESIRED_course = line.split(' ')[5]
						log_item.append(float(DESIRED_course)*57.3)			#Course
						DESIRED_speed = line.split(' ')[10]
						log_item.append(float(DESIRED_speed))				#Speed
						DESIRED_climb = line.split(' ')[9]
						log_item.append(float(DESIRED_climb))				#Climb
						j = len(lines)

					elif ("ROTORCRAFT_FP" == line.split(' ')[2]):
						ROTORCRAFT_FP_phi = line.split(' ')[9]				#ROLL
						log_item.append(float(ROTORCRAFT_FP_phi)*0.0139882)
						ROTORCRAFT_FP_theta = line.split(' ')[10]
						log_item.append(float(ROTORCRAFT_FP_theta)*0.0139882)		#PITCH
						ROTORCRAFT_FP_east = line.split(' ')[3]
						log_item.append(float(ROTORCRAFT_FP_east))			#X
						ROTORCRAFT_FP_north = line.split(' ')[4]
						log_item.append(float(ROTORCRAFT_FP_north))			#Y
						ROTORCRAFT_FP_up = line.split(' ')[5]
						log_item.append(float(ROTORCRAFT_FP_up)*0.0039063)		#alt
						if (float(line.split(' ')[6]) == 0):
							if float(line.split(' ')[7]) == 0:
								ROTORCRAFT_FP_course = 0
								log_item.append(ROTORCRAFT_FP_course)		#Course
							else:
								if float(line.split(' ')[7]) > 0:
									ROTORCRAFT_FP_course = 90
									log_item.append(ROTORCRAFT_FP_course)	#Course
								else:
									ROTORCRAFT_FP_course = 180
									log_item.append(ROTORCRAFT_FP_course)	#Course
						else:
							ROTORCRAFT_FP_course = np.arctan(float(line.split(' ')[7])/float(line.split(' ')[6]))
							log_item.append(ROTORCRAFT_FP_course)			#Course
						ROTORCRAFT_FP_speed = (float(line.split(' ')[6]) + float(line.split(' ')[7]))*0.0000019
						log_item.append(ROTORCRAFT_FP_speed)				#Speed
						ROTORCRAFT_FP_vup = line.split(' ')[8]
						log_item.append(float(ROTORCRAFT_FP_vup)*0.0000019)		#climb
						j = len(lines)
					j+=1
				j = curr_index+1
			if (len(log_item) == 16):
				output.write(str(log_item)[:len(str(log_item))-1][1:]+"\n")
			j+=1

	#PARSE "ABNORMAL" FILES
	output = output =  open(abnorm + files[i][2:-1] + "_abnormal.csv", 'w') if 'pair-wise' not in files[i] else open(abnorm + files[i][12:-1] + "_abnormal.csv", 'w')
	for file_index in range(1,6):
		f = None
		if ('pair-wise' not in files[i]):
			f = open(abnorm + files[i][2:-1] + "_abnormal_"+str(file_index)+".data")
		else:
			f = open(abnorm + files[i][12:-1] + "_abnormal_"+str(file_index)+".data")
		j = 0
		lines = f.readlines()
		
		while j < len(lines):
			line = lines[j]
			log_item = []
			if ("ATTITUDE" == line.split(' ')[2] or "NPS_RATE_ATTITUDE" == line.split(' ')[2]):
				curr_index = j
				if ("ATTITUDE" == line.split(' ')[2]):
					ATTITUDE_phi = line.split(' ')[3]					#ROLL
					log_item.append(float(ATTITUDE_phi)*57.3)
					ATTITUDE_theta = line.split(' ')[4]
					log_item.append(float(ATTITUDE_theta)*57.3)				#PITCH
				else:
					NPS_RATE_ATTITUDE_phi = line.split(' ')[6]				#ROLL
					log_item.append(float(NPS_RATE_ATTITUDE_phi))
					NPS_RATE_ATTITUDE_theta = line.split(' ')[7]
					log_item.append(float(NPS_RATE_ATTITUDE_theta))				#PITCH
				j = curr_index+1
				while j < len(lines):
					line = lines[j]
					if ("GPS" == line.split(' ')[2]):
						GPS_utm_east = line.split(' ')[4]
						log_item.append((float(GPS_utm_east)/100)-UTM_EAST)		#X
						GPS_utm_north = line.split(' ')[5]
						log_item.append((float(GPS_utm_north)/100)-UTM_NORTH)		#Y
						GPS_alt = line.split(' ')[7]
						log_item.append(float(GPS_alt)/1000)				#alt
						GPS_course = line.split(' ')[6]	
						log_item.append(float(GPS_course)/10)				#Course
						GPS_speed = line.split(' ')[8]
						log_item.append(float(GPS_speed)/100)				#Speed
						GPS_climb = line.split(' ')[9]
						log_item.append(float(GPS_climb)/100)				#Climb
						j = len(lines)
					elif ("GPS_INT" == line.split(' ')[2]):
						GPS_INT_ecef_x = line.split(' ')[3]				#X
						log_item.append((float(GPS_INT_ecef_x)/100)-UTM_EAST)
						GPS_INT_ecef_y = line.split(' ')[4]				#Y
						log_item.append((float(GPS_INT_ecef_y)/100)-UTM_NORTH)
						GPS_INT_alt = line.split(' ')[5]
						log_item.append((float(GPS_INT_alt)/100)-UTM_HEIGHT)				#Alt

						if (float(line.split(' ')[10]) == 0):
							if float(line.split(' ')[11]) == 0:
								GPS_INT_course = 0
								log_item.append(GPS_INT_course)			#Course
							else:
								if float(line.split(' ')[11]) > 0:
									GPS_INT_course = 90
									log_item.append(GPS_INT_course)		#Course
								else:
									GPS_INT_course = 180
									log_item.append(GPS_INT_course)		#Course
						else:
							GPS_INT_course = np.arctan(float(line.split(' ')[11])/float(line.split(' ')[10]))
							log_item.append(GPS_INT_course)				#Course
				
						GPS_INT_speed = float(line.split(' ')[10])+float(line.split(' ')[11])
						log_item.append(float(GPS_INT_speed)/100)			#Speed
						GPS_INT_climb = line.split(' ')[12]
						log_item.append(float(GPS_INT_climb)/100)			#Climb
						j = len(lines)
					j+=1
				j = curr_index+1
				while j < len(lines):
					line = lines[j]
					if ("DESIRED" == line.split(' ')[2]):
						DESIRED_roll = line.split(' ')[3]
						log_item.append(float(DESIRED_roll)*57.3)			#ROLL
						DESIRED_pitch = line.split(' ')[4]
						log_item.append(float(DESIRED_pitch)*57.3)			#PITCH
						DESIRED_x = line.split(' ')[6]
						log_item.append(float(DESIRED_x))				#X
						DESIRED_y = line.split(' ')[7]
						log_item.append(float(DESIRED_y))				#Y
						DESIRED_alt = line.split(' ')[8]
						log_item.append(float(DESIRED_alt))				#Alt
						DESIRED_course = line.split(' ')[5]
						log_item.append(float(DESIRED_course)*57.3)			#Course
						DESIRED_speed = line.split(' ')[10]
						log_item.append(float(DESIRED_speed))				#Speed
						DESIRED_climb = line.split(' ')[9]
						log_item.append(float(DESIRED_climb))				#Climb
						j = len(lines)

					elif ("ROTORCRAFT_FP" == line.split(' ')[2]):
						ROTORCRAFT_FP_phi = line.split(' ')[9]				#ROLL
						log_item.append(float(ROTORCRAFT_FP_phi)*0.0139882)
						ROTORCRAFT_FP_theta = line.split(' ')[10]
						log_item.append(float(ROTORCRAFT_FP_theta)*0.0139882)		#PITCH
						ROTORCRAFT_FP_east = line.split(' ')[3]
						log_item.append(float(ROTORCRAFT_FP_east))			#X
						ROTORCRAFT_FP_north = line.split(' ')[4]
						log_item.append(float(ROTORCRAFT_FP_north))			#Y
						ROTORCRAFT_FP_up = line.split(' ')[5]
						log_item.append(float(ROTORCRAFT_FP_up)*0.0039063)		#alt
						if (float(line.split(' ')[6]) == 0):
							if float(line.split(' ')[7]) == 0:
								ROTORCRAFT_FP_course = 0
								log_item.append(ROTORCRAFT_FP_course)		#Course
							else:
								if float(line.split(' ')[7]) > 0:
									ROTORCRAFT_FP_course = 90
									log_item.append(ROTORCRAFT_FP_course)	#Course
								else:
									ROTORCRAFT_FP_course = 180
									log_item.append(ROTORCRAFT_FP_course)	#Course
						else:
							ROTORCRAFT_FP_course = np.arctan(float(line.split(' ')[7])/float(line.split(' ')[6]))
							log_item.append(ROTORCRAFT_FP_course)			#Course
						ROTORCRAFT_FP_speed = (float(line.split(' ')[6]) + float(line.split(' ')[7]))*0.0000019
						log_item.append(ROTORCRAFT_FP_speed)				#Speed
						ROTORCRAFT_FP_vup = line.split(' ')[8]
						log_item.append(float(ROTORCRAFT_FP_vup)*0.0000019)		#climb
						j = len(lines)
					j+=1
				j = curr_index+1
			if (len(log_item) == 16):
				output.write(str(log_item)[:len(str(log_item))-1][1:]+"\n")
			j+=1
