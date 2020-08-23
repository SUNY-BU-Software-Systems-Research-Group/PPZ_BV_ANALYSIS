* File: paparazzi/sw/airborne/firmwares/rotorcraft/stabilization/stabilization_attitude_rc_setpoint.c
* Line: 117
* Function: DeadBand 
* Var: yaw
* Status: Same
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: the simulation results don't show a consistent pattern across repeated simulations. The reason might be that the code indeed supports integer implementation but not float implementation