
import redishelper

import serialize

from conf import host


class MoniServer(object):
    def __init__(self):
       #pass
       # connect to redis
       self.r = redishelper.RedisHelper()
       self.r.set("zadmoni", 'tsunc20170801-')
       print self.r.get("name3")
       self.save_config_into_redis()


    def start(self):
       pass
       # 

    def save_config_into_redis(self):
    	 serialize.push_all_config_redis(self,host.monitor_group)

