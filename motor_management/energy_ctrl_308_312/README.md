File: sw/airborne/firmwares/fixedwing/guidance/energy_ctrl.c
Vars: sp, incr
Lines: 308,312
Type: Multi-BF Different
Notes: When removing both of these bounds we achieve a higher speed during takeoff. Since these variables are related to vertical speed and acceleration, removing these bounds directly impacts their functionality.


