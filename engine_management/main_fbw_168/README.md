* File: sw/airborne/firmwares/fixedwing/main_fbw.c
* Line: 168
* Function: ClipAbs 
* Var: command_pitch_trim
* Status: Same
* Code change: instead of directly comment out the whole statement containing the BF, we do the code change as shown below
	- Original: trimmed_commands[COMMAND_PITCH] += ClipAbs(command_pitch_trim, MAX_PPRZ / 10);
	- New: trimmed_commands[COMMAND_PITCH] += command_pitch_trim;
* Simulation detail: firstly set "Settings"->"mode"->"autopilot.launch" and "autopilot.kill_throttle" to 1 and 0 respectively. then execute "python rc_sim.py -i 13 -p plan.csv" under path "paparazzi/sw/ground_segment/joystick"
* Notes: the simulation results show no difference between with and without BF cases. The reason is that command_pitch_trim is assigned by ap_state->command_pitch_trim, whose value is probably only set when running "ap" target but for simulation we have to run "nps" target. Therefore, command_pitch_trim is always a constant number (788 in this case) and will never exceed the range [-MAX_PPRZ / 10, MAX_PPRZ / 10].