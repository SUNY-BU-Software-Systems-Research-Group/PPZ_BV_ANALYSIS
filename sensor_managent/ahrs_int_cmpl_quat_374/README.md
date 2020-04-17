* File: /paparazzi/sw/airborne/subsystems/ahrs/ahrs_int_cmpl_quat.c 
* Line: 374
* Function: Bound 
* Var: inv_bias_gain 
* Status: SAME 
* Pre-simulation preparation: Removed the Bounding Function for ahrs_icq.weight in order to get inv_bias_gain exceed range
* Simulation detail: click "Vertical Test" button after taking off
* Notes: No difference according to simulator and log plotter, but don't know the reason yet