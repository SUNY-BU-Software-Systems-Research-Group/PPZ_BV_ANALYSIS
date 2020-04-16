File: /paparazzi/sw/airborne/firmwares/fixedwing/guidance/energy_ctrl.c
Line: 434
Function: BoundAbs
var: sp
status: Same
Notes: This is a good example of redundant bounding. v_ctl_altitude_setpoint, the desired location (or carrot) of the drone is bounded, and used to compute sp, which is bounded. sp is then used to compute incr, which guides the drones acceleration. This appeared to keep the value within a range for the UAV to behave normally.
