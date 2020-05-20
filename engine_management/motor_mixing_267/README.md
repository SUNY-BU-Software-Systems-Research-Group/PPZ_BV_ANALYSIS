File: /paparazzi/sw/airborne/subsystems/actuators/motor_mixing.c
Line: 267
Function: BoundAbs
var: saturation_offset
status: Diff
Notes: The source code was eddited as shown below. By removing the bounded variable the UAV is unable to hold its altitute. When it performs its takeoff it just continues slowly losing altitude. These findings confirm the comments found in the source code.


Lines 260 to 270...


    if (max_cmd > MOTOR_MIXING_MAX_MOTOR) {
      int32_t saturation_offset = MOTOR_MIXING_MAX_MOTOR - max_cmd;
      BoundAbs(saturation_offset, MOTOR_MIXING_MAX_SATURATION_OFFSET);
      offset_commands(saturation_offset);
      motor_mixing.nb_saturation++;
    } else if (min_cmd < MOTOR_MIXING_MIN_MOTOR) {
      int32_t saturation_offset = MOTOR_MIXING_MIN_MOTOR - min_cmd;
      BoundAbs(saturation_offset, MOTOR_MIXING_MAX_SATURATION_OFFSET);
      offset_commands(saturation_offset);
      motor_mixing.nb_saturation++;
    }

are changed to...

    //if (max_cmd > MOTOR_MIXING_MAX_MOTOR) {
      int32_t saturation_offset = MOTOR_MIXING_MAX_MOTOR - max_cmd;
      BoundAbs(saturation_offset, MOTOR_MIXING_MAX_SATURATION_OFFSET);
      offset_commands(saturation_offset);
      motor_mixing.nb_saturation++;
    //} else if (min_cmd < MOTOR_MIXING_MIN_MOTOR) {
      int32_t saturation_offset = MOTOR_MIXING_MIN_MOTOR - min_cmd;
      BoundAbs(saturation_offset, MOTOR_MIXING_MAX_SATURATION_OFFSET);
      offset_commands(saturation_offset);
      motor_mixing.nb_saturation++;
    //}

to ensure the bounding condition is used.
