File: paparazzi/sw/airborne/modules/nav/nav_smooth.c
Line: 174
Function: Bound
Var: ground_speeds[i]
Status: DIFFERENT
Aircraft & target: Microjet - sim
Pre-simulatyion preparation: changed from sqrt(delta) to sqrt(fabs(delta)) in the computation of ground_speeds[i] to avoid NaN error; increased the windspeed arguments passed to compute_ground_speed() in snav_on_time() by 100 times (the modified version of source code is attached in this folder)
Simulation process: launch->takeoff->Smooth nav
Notes: the changes of radius are different according to log plotter
