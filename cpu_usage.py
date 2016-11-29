#!/usr/bin/python2
from subprocess import check_output
import time
import sys
import argparse


parser = argparse.ArgumentParser(description='Monitor CPU Usage')
parser.add_argument('-i', '--interval', type=float, default=1,
                    help='Time interval between each measurement, in seconds (min = 0.2)')
parser.add_argument('-o', '--output', type=str, default='',
                    help='Output file')
args = parser.parse_args()

interval = args.interval
if(interval < 0.2):
    interval = 0.2

output = args.output

if output:
    out_file = open(output, 'w', buffering=1)
    # print "I just opened a file called" + output
    # out_file.write('CPU Usage is %d percent\n')
else:
    out_file = sys.stdout

#out_file.write('Hello World!\n')

#print (interval)

out = check_output(['cat', '/proc/stat'])
out = out.splitlines()[0]
# print(out.split(' ')[2:])
puser, pnice, psystem, pidle, piowait, \
    pirq, psoftirq \
    = [float(x) for x in out.split(' ')[2:9]]

while True:
    time.sleep(interval)
    out = check_output(['cat', '/proc/stat'])
    out = out.splitlines()[0]
    user, nice, system, idle, iowait, \
        irq, softirq \
        = [float(x) for x in out.split(' ')[2:9]]
    prev_idle = pidle + piowait
    cur_idle = idle + iowait
    prev_active = puser + pnice + psystem + pirq + \
        psoftirq
    cur_active = user + nice + system + irq + \
        softirq
    prev_total = prev_idle + prev_active
    cur_total = cur_idle + cur_active

    dtotal = cur_total - prev_total
    didle = idle - pidle

    puser, pnice, psystem, pidle, piowait, \
        pirq, psoftirq, \
        user, nice, system, idle, iowait, \
        irq, softirq = \
        user, nice, system, idle, iowait, \
        irq, softirq, \
        puser, pnice, psystem, pidle, piowait, \
        pirq, psoftirq

    try:
        cpu_usage = 100*(dtotal - didle)/dtotal
    except ZeroDivisionError as e:
        continue
    # print "I am going to write"
    out_file.write('CPU Usage is %d percent\n' % cpu_usage)
