#!/usr/bin/env python

import commands,time,sys
import rrdtool

def scout(first_invoke=1): # scout horseman
    #shell_command = 'snmpwalk -v2c 211.152.50.254 -cpubl1c ifInOctets | grep \'ifInOctets.15\' | awk \'{print $4}\''
    shell_command1 = 'snmpwalk -v2c 211.152.50.254 -cpubl1c ifInOctets | grep \'ifInOctets.15\' '
    status, result = commands.getstatusoutput(shell_command1)
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        f1, f2, f3, f4 = result.split()
        value_dic = {
            'f1': f1,
            'f2': f2,
            'f3': f3,
            'f4': f4,
            'status': status
        }
    return value_dic

def scout2(first_invoke=1): # scout horseman
    #shell_command = 'snmpwalk -v2c 211.152.50.254 -cpubl1c ifInOctets | grep \'ifInOctets.15\' | awk \'{print $4}\''
    shell_command2 = 'snmpwalk -v2c 211.152.50.254 -cpubl1c ifOutOctets | grep \'ifOutOctets.15\' '
    status2, result2 = commands.getstatusoutput(shell_command2)
    if status2 != 0:
        value_dic2 = {'status2': status2}
    else:
        value_dic2 = {}
        f21, f22, f23, f24 = result2.split()
        value_dic2 = {
            'f21': f21,
            'f22': f22,
            'f23': f23,
            'f24': f24,
            'status2': status2
        }
    return value_dic2

if __name__ == '__main__':
    while True:
        res = scout()
        result = int(res['f4'])
        res2 = scout2()
        result2 = int(res2['f24'])
        rrdval_9440 = rrdtool.updatev('w-2924-24-ct-08-share-50_traffic_in_9440.rrd','N:%d:%d' % (result, result2))
        print rrdval_9440
        print result, result2
    sleep(1)
