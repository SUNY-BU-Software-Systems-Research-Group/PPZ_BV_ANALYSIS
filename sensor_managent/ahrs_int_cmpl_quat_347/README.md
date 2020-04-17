* File: /paparazzi/sw/airborne/subsystems/ahrs/ahrs_int_cmpl_quat.c 
* Line: 347
* Function: Bound 
* Var: inv_rate_scale
* Status: DIFFERENT 
* Pre-simulation preparation: Removed the Bounding Function for ahrs_icq.weight in order to get inv_rate_scale exceed range
* Simulation detail: click "Vertical Test" button after taking off
* Notes: With BF, the UAV will fly over waypoint H2 without stopping but would stop at H5 when turning around (refer to "vertical_test_inv_rate_scale_normal.JPG"); without BF, the UAV will stop at H2 before flying to H3 but can't stop at H5 when turning around (refer to "vertical_test_inv_rate_scale_abnormal.JPG").