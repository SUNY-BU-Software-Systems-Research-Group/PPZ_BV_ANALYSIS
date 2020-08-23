* File: paparazzi/sw/airborne/firmwares/rotorcraft/stabilization/stabilization_attitude_rc_setpoint.c
* Line: 77,107
* Function: DeadBand 
* Var: pitch
* Status: Multi-BF DIFFERENT
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: With BF, the UAV keeps climbing consistently; without BF, the UAV flies downwards and crashes on ground soon.