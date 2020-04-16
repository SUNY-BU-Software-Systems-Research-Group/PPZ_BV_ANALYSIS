File: /paparazzi/sw/airborne/firmwares/fixedwing/guidance/energy_ctrl.c
Line: 308
Function: BoundAbs
var: sp
status: Same
Notes: This is a good example of "redundant" bounding. v_ctl_altitude_setpoint, the desired location (or carrot) of the drone is bounded, and used to compute sp. sp is then used to compute incr, which guides the drones acceleration. This is also bounded. It is worth noting that the simulation might not provide an environment in which removing these bounds makes a critical difference.
