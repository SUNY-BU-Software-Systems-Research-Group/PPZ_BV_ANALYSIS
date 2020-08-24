* File: paparazzi/sw/airborne/subsystems/radio_control/rc_datalink.c
* Line: 86
* Function: Bound 
* Var: out[RADIO_MODE]
* Status: Same
* Simulation detail: click "Start Engine" and then execute "python rc_sim.py -i 203 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: because only when radio mode is set to 0 can we do simulation with RC normally; with other mode number, we cannot even do the simulation. Therefore, the computed out[RADIO_MODE] is not possible to exceed the range