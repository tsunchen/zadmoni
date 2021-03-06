from service import linux


class BaseTemplate(object):
    def __init__(self):
       self.name = 'template name'
       self.hosts = []
       self.services = []


class LinuxGenericTemplate(BaseTemplate):
    def __init__(self):
       super(LinuxGenericTemplate, self).__init__()
       self.name = "LinuxCommonServices"
       self.services = [
          linux.cpu(),
          linux.memory()
       ]
       #self.service[0].interval = 90


class LinuxGenericTemplate2(BaseTemplate):
    def __init__(self):
       super(LinuxGenericTemplate2, self).__init__()
       self.name = "LinuxCommonServices2"
       self.services = [
          linux.cpu(),
          linux.network()
       ]
