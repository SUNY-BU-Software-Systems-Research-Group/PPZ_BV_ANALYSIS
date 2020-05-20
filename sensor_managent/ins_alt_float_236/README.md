* File: /paparazzi/sw/airborne/subsystems/ins/ins_alt_float.c
* Line: 236
* Function: Bound 
* Var: dt 
* Status: SAME 
* Pre-simulation preparation: manually set dt to a very large constant (modified source code is attached in this folder)
* Simulation detail: click "Vertical Test" button after taking off
* Notes: no difference because alt_kalman() uses kalman filter, an adaptive algorithm, whose estimation result isn't impacted by time interval dt