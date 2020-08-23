* File: paparazzi/sw/airborne/firmwares/rotorcraft/stabilization/stabilization_attitude_rc_setpoint.c
* Line: 88
* Function: DeadBand 
* Var: yaw
* Status: Single-BF DIFFERENT
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: With BF, the UAV turns southeastward; without BF, the UAV turns in an uncertain direction (mostly turns eastward or westward)