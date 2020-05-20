File: paparazzi/sw/airborne/firmwares/rotorcraft/navigation.c
Line: 599
Function: Bound
Var: nav_leg_progress
Status: DIFFERENT
Aircraft & target: bebop - nps
Pre-simulation preparation: forced conversion of nav_leg_length to type int32_t in the computation of nav_leg_progress 
Simulation process: Execute "Oval Test"
Notes: Without forced conversion, the UAV would fly away before entering the oval routine in absence of BF; with forced conversion, the carrot would move over the routine in absence of BF
