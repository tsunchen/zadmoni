import redishelper


class MoniServer(object):
    def __init__(self):
       #pass
       # connect to redis
       self.r = redishelper.RedisHelper()
       self.r.set("name3", 'tsunc20170901-1550')
       print self.r.get("name3")


    def start(self):
       pass
       # 
