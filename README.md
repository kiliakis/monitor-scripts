## monitor-scripts
Scripts that monitor variable performance counters composed in python

### Scripts list

1. cpu_usage.py
> Daemon tool that calculates and prints overall cpu usage, using statistics found in /proc/stat file.
  
* Optional Arguments
    1. -i/--interval INTERVAL: INTERVAL is a float that specifies the time interval between each measurement in seconds. Min = 0.2 sec, default= 1 sec.
    2. -o/--output OUTPUT: OUTPUT is the file in which the measurements will be printed. Default output is stdout.

* Usage: Just run `python2 cpu_usage.py`
