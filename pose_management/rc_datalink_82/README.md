* File: paparazzi/sw/airborne/subsystems/radio_control/rc_datalink.c
* Line: 82
* Function: Bound 
* Var: out[RADIO_YAW]
* Status: Same
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: because yaw value from RC is required to be in [-128,127], which makes it impossible for the computed out[RADIO_YAW] exceeding the range [MIN_PPRZ,MAX_PPRZ]