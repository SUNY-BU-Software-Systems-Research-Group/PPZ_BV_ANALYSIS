File: sw/airborne/firmwares/rotorcraft/stabilization/attitude_ref_saturate_naive.h
Line: 79, 82, 83, 84
Function: RATES_BOUND_BOX_ABS & SATURATE_SPEED_TRIM_ACCEL
var: accel, rate->p, rate→q, rate->r
status: Multi-BF Different
Notes: When removing all of these bounds, rate_attitude_r shows a sharper decrement according to the log plotter.
