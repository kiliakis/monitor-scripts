#!/usr/bin/python2
from subprocess import check_output
import time
import sys
import argparse


parser = argparse.ArgumentParser(description='Monitor CPU Usage')
parser.add_argument('-i','--interval',type=float, default=1,
        help='Time interval between each measurement, in seconds (min = 0.2)')
parser.add_argument('-o','--output',type=str, default='',
        help='Output file')
args = parser.parse_args()
interval = args.interval
output = args.output

if output:
    out_file = open(output,'w')
else:
    out_file = sys.stdout

#out_file.write('Hello World!\n')

#print (interval)

out = check_output(['cat','/proc/stat'])
out = out.splitlines()[0]
#print (out.split(' '))
puser,pnice,psystem,pidle,piowait, \
        pirq,psoftirq,psteal,pguest,pguest_nice \
        = [float(x) for x in out.split(' ')[2::]]

while True:
    time.sleep(interval)
    out = check_output(['cat','/proc/stat'])
    out = out.splitlines()[0]
    user, nice, system, idle, iowait, \
            irq, softirq, steal, guest, guest_nice \
            = [float(x) for x in out.split(' ')[2::]]
    prev_idle = pidle + piowait
    cur_idle = idle + iowait
    prev_active = puser + pnice + psystem + pirq + \
            psoftirq + psteal
    cur_active = user + nice + system + irq + \
            softirq + steal
    prev_total = prev_idle + prev_active
    cur_total = cur_idle + cur_active

    dtotal = cur_total - prev_total
    didle = idle - pidle

    puser,pnice,psystem,pidle,piowait, \
        pirq,psoftirq,psteal,pguest,pguest_nice, \
        user, nice, system, idle, iowait, \
        irq, softirq, steal, guest, guest_nice = \
        user, nice, system, idle, iowait, \
        irq, softirq, steal, guest, guest_nice, \
        puser,pnice,psystem,pidle,piowait, \
        pirq,psoftirq,psteal,pguest,pguest_nice

    try:
        cpu_usage = 100*(dtotal - didle)/dtotal
    except ZeroDivisionError as e:
        continue

    out_file.write('CPU Usage is %d percent\n' % cpu_usage)


