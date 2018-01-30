#!/usr/bin/env python
#coding=utf8  
import psutil  

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json

cpu = {'user' : 0, 'system' : 0, 'idle' : 0, 'percent' : 0}  
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}  
  
#磁盘名称  
disk_id = []  
#将每个磁盘的total used free percent 分别存入到相应的list  
disk_total = []  
disk_used = []  
disk_free = []  
disk_percent = []  


  
#获取CPU信息  
def get_cpu_info():  
    cpu_times = psutil.cpu_times()  
    cpu['user'] = cpu_times.user  
    cpu['system'] = cpu_times.system  
    cpu['idle'] = cpu_times.idle  
    cpu['percent'] = psutil.cpu_percent(interval=2)  


#获取内存信息  
def get_mem_info():  
    mem_info = psutil.virtual_memory()  
    mem['total'] = mem_info.total  
    mem['available'] = mem_info.available  
    mem['percent'] = mem_info.percent  
    mem['used'] = mem_info.used  
    mem['free'] = mem_info.free  


#获取磁盘  
def get_disk_info():  
    for id in psutil.disk_partitions():  
        if 'cdrom' in id.opts or id.fstype == '':  
            continue  
        disk_name = id.device.split(':')  
        s = disk_name[0]  
        disk_id.append(s)  
        disk_info = psutil.disk_usage(id.device)  
        disk_total.append(disk_info.total)  
        disk_used.append(disk_info.used)  
        disk_free.append(disk_info.free)  
        disk_percent.append(disk_info.percent)  


def monitor(first_invoke=1):
    #shell_command = 'sar 1 3| grep "^Average:"'
    #status, result = commands.getstatusoutput(shell_command)
    #if status != 0:
    #    value_dic = {'status': status}
    #else:

    value_dic = {}
    #user,nice,system,iowait,steal,idle = result.split()[2:]

    v_disk_percent = []
    for i in range(len(disk_id)):  
        v_disk_percent.append(100 - disk_percent[i])  

    disks = zip (disk_id, v_disk_percent)
    #disks_dic = {}
    disks_dic = dict(disks)
    value_dic = {
        'cpu_prt': cpu['percent'],
        'mem_prt': mem['percent'],
        'disk_prt': disks_dic,
            #'iowait': iowait,
            #'steal': steal,
            #'idle':  idle,
            #'status': status
        }
    return value_dic
          
  
if __name__ == '__main__':  
    ##http://blog.csdn.net/yanggd1987/article/details/48051893
    get_cpu_info()  
    cpu_status = cpu['percent']  
    print u"CPU使用率: %s %%" % cpu_status  
    get_mem_info()  
    mem_status = mem['percent']  
    print u"内存使用率: %s %%" % mem_status  
    get_disk_info()  
    for i in range(len(disk_id)):  
        print u'%s盘空闲率: %s %%' % (disk_id[i],100 - disk_percent[i])  
    #raw_input("Enter enter key to exit...")    
    #print monitor()
    data = monitor()
    print data
    jdata = json.dumps(data)

    print jdata
    ldata = json.loads(jdata)
    
    print ldata.keys()
    print ldata["disk_prt"]["C"]
    print ldata["disk_prt"]["D"]
    print ldata["disk_prt"]["E"]



