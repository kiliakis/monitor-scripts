#!/usr/bin/python2
from subprocess import check_output
import time

out = check_output(['cat','/proc/stat'])
out = out.splitlines()[0]
print (out.split(' ')[2::])
puser,pnice,psystem,pidle,piowait, \
        pirq,psoftirq,psteal,pguest,pguest_nice \
        = [float(x) for x in out.split(' ')[2::]]

for i in range(100):
    time.sleep(1)
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

    print ('CPU Usage is %d percent' % cpu_usage)


