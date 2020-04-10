File: /paparazzi/sw/airborne/modules/guidance/gvf/gvf.c
Line: 199
Function: BoundAbs
var: h_ctl_setpoint
status: DIFFERENT
Notes: Removing directly dissrupts behavior of gvf navigation. Roll values break bounds and cause over correction in horizontal navigation, causing the drone to oscillate when holding a circle course for example. The flight plan logs are provided to replay the example. Also images are attached to show the expected behavior.
