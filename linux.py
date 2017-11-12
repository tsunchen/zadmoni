
from generic import BaseService

class cpu(BaseService):
    def __init__(self):
        super(cpu, self).__init__()
        self.interval = 30
        self.name = 'linux_cpu'
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
           'idle': {
              'func': 'avg',
              'last': 600,
              'count': 1,
              'operator': 'lt',
              'warning': 20,
              'critical': 5,
              'data_type': float
           },
           'iowait': {
              'func': 'hit',
              'last': 15*60,
              'count': 5,
              'operator': 'gt',
              'warning': 40,
              'critical': 50,
              'data_type': float
           }
        }


class memory(BaseService):
    def __init__(self):
        super(memory, self).__init__()
        self.interval = 20
        self.name = 'linux_memory'
        self.plugin_name = 'get_memory_info'
        self.triggers = {
            'MemUsage_p': {
              'func': 'avg',
              #'minutes': 15,
              'last': 5*60,
              'count': 1,
              'operator': 'gt',
              'warning': 80,
              'critical': 90,
              #'data_type': 'percentage',
              'data_type': float
            }     
        }



class network(BaseService):
    def __init__(self):
        super(network, self).__init__()
        self.interval = 60
        self.name = 'linux_network'
        self.plugin_name = 'get_network_info'
        self.triggers = {
           'in': {
              'func': 'hit',
              'last': 10*60,
              'count': 5,
              'operator': 'gt',
              'warning': 8*1024*1024,
              'critical': 16*1024*1024,
              'data_type': float
             },
           'out': {
              'func': 'hit',
              'last': 10*60,
              'count': 5,
              'operator': 'gt',
              'warning': 8*1024*1024,
              'critical': 16*1024*1024,
              'data_type': float

             }
        }


# projectname: lunar knight, 2017 Nov.09 
# design for switchers
class ifport(BaseService):
    def __init__(self):
        super(ifport, self).__init__()
        self.interval = 30
        self.name = 'linux_ifportlookup'
        self.plugin_name = 'get_ifport_info'
        self.triggers = {
           'ifIn': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning': 300000,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             },
           'ifOut': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning': 300000,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             }
        }

class ifports(BaseService):
    def __init__(self):
        super(ifports, self).__init__()
        self.interval = 47
        self.name = 'linux_ifportpeek'
        self.plugin_name = 'get_ifport_s_info'
        self.triggers = {

           'ifIn::FastEthernet0_14': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning': 300000,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             },
           'ifOut::FastEthernet0_14': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning': 300000,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             },

           'ifIn::FastEthernet0_15': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning':  1 * 1024 * 1024,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             },
           'ifOut::FastEthernet0_15': {
              'func': 'avg',
              'last': 5*60,
              'count': 5,
              'operator': 'gt',
              'warning':  1 * 1024 * 1024,
              'critical': 8 * 1024 * 1024,
              'data_type': float
             }
        }

