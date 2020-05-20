File: /paparazzi/sw/airborne/subsystems/actuators/motor_mixing.c
Line: 232
Function: BoundAbs
var: bounded_yaw_cmd
status: Same
Notes: Removing this bound appeared to have no change on behavior but it did have an affect on the yaw values. Printing showed that this value is does fall outside the bounds.
