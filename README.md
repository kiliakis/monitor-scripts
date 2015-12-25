## monitor-scripts
Scripts that monitor variable performance counters composed in python

### Scripts list
1. cpu_usage.py
  * Daemon tool that calculates and prints overall cpu usage, using statistics found in /proc/stat file.
  * (Optional) Give a command line argument that specifies the time interval between each measurement. Default interval is 1 sec.
  * Usage: just run python cpu_usage.py (time_interval)
