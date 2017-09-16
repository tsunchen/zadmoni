#!/usr/bin/env python

import commands,time,sys
import rrdtool

def monitor(first_invoke=1):
    shell_command = 'sar 1 3| grep "^Average:"'
    status, result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        user,nice,system,iowait,steal,idle = result.split()[2:]
        value_dic = {
            'user': user,
            'nice': nice,
            'system': system,
            'iowait': iowait,
            'steal': steal,
            'idle':  idle,
            'status': status
        }
    return value_dic

if __name__ == '__main__':
    #print monitor()
    result = monitor()
    print result['idle']
    res_idle = float(result['idle'])
    print res_idle

    #print 'bash start running...'
    #shell_command3 = 'bash -x setinterv.sh '
    #status, resultcmd3 = commands.getstatusoutput(shell_command3)
    #if status != 0:
    #    value_dic = {'status': status}
    #else:
    #    print resultcmd3

    #rrdtool update
    rrdval_idle = rrdtool.updatev('zad_cpu_idle_rc.rrd','N:%f' % (res_idle))

    print rrdval_idle
