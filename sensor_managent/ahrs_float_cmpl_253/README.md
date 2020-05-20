* File: paparazzi/sw/airborne/subsystems/ahrs/ahrs_float_cmpl.c 
* Line: 253
* Function: Bound 
* Var: ahrs_fc.weight
* Status: DIFFERENT
* Simulation detail: click "Vertical Test" button after taking off
* Notes: According to log plotter on rate attitudes, without BF, there's a sharp decrement on rate attitude on p and r before changing back to normal value when the UAV is about to turn around; with BF, it only declines slightly.