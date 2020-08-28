# PPZ_BV_ANALYSIS
There are three main components in this repository:
* "analysis_tools": python-based paparazzi log data analysis tools
* "cross_simulation_figures": scripts for drawing figures of cross-simulation logs
* "rc_sim_tool": scripts for remote control simulation to generate identical inputs for repeated simulations
* "BV.xlsx": a detailed form of BV information
* other folders: stores case-by-case analysis of bounded variables in paparazzi codebase

Generating multi-variable figures for cross flight simulation can be done with...

```
$cd cross_sim_figures
$bash create_figures.sh
```
