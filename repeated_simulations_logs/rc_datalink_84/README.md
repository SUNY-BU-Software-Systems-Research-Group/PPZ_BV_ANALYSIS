* File: paparazzi/sw/airborne/subsystems/radio_control/rc_datalink.c
* Line: 84
* Function: Bound 
* Var: out[RADIO_THROTTLE]
* Status: Single-BF DIFFERENT
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: According to log plotter, in with BF cases, both ENERGY:throttle and ROTORCRAFT_FP:thrust drop to 0, while in without BF cases, the former climbs to 160 and the latter drop to -9600.