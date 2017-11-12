from plugin import cpu,load,memory,ifportlookup,ifportpeek


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
    data = ifportpeek.runit()
    return data

