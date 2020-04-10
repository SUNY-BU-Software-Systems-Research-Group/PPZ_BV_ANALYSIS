File: /paparazzi/sw/airborne/firmwares/rotorcraft/stabilization/stabilization_attitude_ref_euler_int.c
Line: 135
Function: RATES_BOUND
var: ref-> accel
status: DIFFERENT
Notes: Removing can cause the UAV to flip while under RC command, by allowing larger roll changes than should be.
