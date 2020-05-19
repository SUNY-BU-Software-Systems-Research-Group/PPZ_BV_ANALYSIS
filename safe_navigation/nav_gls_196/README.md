File: paparazzi/sw/airborne/modules/nav/nav_gls.c
Line: 196
Function: Bound
Var: nav_intercept_progress
Status: SAME
Aircraft & target: Microjet - sim
Pre-simulation preparation: set wind->x to 17.0, set wind->y to -6.0 (modified source code is attached in this folder)
Simulation process: launch->takeoff->GLS Test
Notes: no difference because nav_intercept_progress only impacts the value of alt_intercept and pre_climb_intercept, which are assigned to alt and pre_climb only during the segment between SD and intercept. However, nav_interceptl_progress is impossible to exceed the range -1~1 on this segment
