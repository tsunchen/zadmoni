
from plugin import ifportlookup,ifportpeek


#print cpu, load

def get_cpu_status():
    data = cpu.monitor()
    #print data
    return data


def get_network_info():
    data = load.monitor()
    #print data
    return data


def get_memory_info():
    data =  memory.monitor()
    return data
    #return 'get_memory_info under construction'

'''
def cisco_cpu_status():
    return cisco_cpu.monitor()

'''

def get_ifport_info():
    data = ifportlookup.runit()
    return data


def get_ifport_s_info():
    #data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '15')
    #data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '16')
    #runit(1, 'publ1c', '211.152.50.254', '1')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '2')
    #runit(1, 'publ1c', '211.152.50.254', '3')
    #runit(1, 'publ1c', '211.152.50.254', '4')
    #runit(1, 'publ1c', '211.152.50.254', '5')
    #runit(1, 'publ1c', '211.152.50.254', '6')
    #runit(1, 'publ1c', '211.152.50.254', '7')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '8')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '9')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '10')
    #runit(1, 'publ1c', '211.152.50.254', '11')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '12')
    #runit(1, 'publ1c', '211.152.50.254', '13')
    #runit(1, 'publ1c', '211.152.50.254', '14')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '15')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '16')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '17')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '18')
    data = ifportpeek.runit(1, 'publ1c', '211.152.50.254', '19')
    #runit(1, 'publ1c', '211.152.50.254', '20')
    #runit(1, 'publ1c', '211.152.50.254', '21')
    #runit(1, 'publ1c', '211.152.50.254', '22')
    #runit(1, 'publ1c', '211.152.50.254', '23')
    #runit(1, 'publ1c', '211.152.50.254', '24')
    #runit(1, 'publ1c', '211.152.50.254', '25')
    return data
