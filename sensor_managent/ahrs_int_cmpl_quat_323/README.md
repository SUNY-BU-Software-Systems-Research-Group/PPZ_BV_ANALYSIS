* File: /paparazzi/sw/airborne/subsystems/ahrs/ahrs_int_cmpl_quat.c 
* Line: 323 
* Function: Bound 
* Var: ahrs_icq.weight
* Status: DIFFERENT 
* Simulation detail: click "Vertical Test" button after taking off
* Notes: Without Bounding Function, the UAV starts with a relatively higher speed and cannot stop at waypoint H2 before flying to the next waypoint H3, but would stop at H5 when turning around (refer to "vertical_test_weight_abnormal.JPG"); with BF, the UAV can fly towards and stop at H2, but can't stop at H5 when turning around (refer to "vertical_test_weight_normal.JPG").
