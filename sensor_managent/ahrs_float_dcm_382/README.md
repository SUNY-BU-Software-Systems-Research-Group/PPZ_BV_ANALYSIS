* File: paparazzi/sw/airborne/subsystems/ahrs/ahrs_float_dcm.c
* Line: 382
* Function: Clip
* Var: 1 - 2 * fabsf(1 - Accel_magnitude)
* Status: SAME
* Simulation process: Circle around here" button after taking off
* Notes: it's used in DCM, which is an adaptive algorithm, so its impact would be compensated