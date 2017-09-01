#!/usr/bin/env python
#coding:utf-8

import redis

#MoniServer need setting from conf
from conf import setting


class RedisHelper:
   def __init__(self):
     self.__conn = redis.Redis(host=setting.RedisServer, port=setting.RedisPort, password='tsrds')
     self.channel_sub = setting.RedisSubChannel
     self.channel_pub = setting.RedisPubChannel
     #self.__conn = redis.Redis(host='172.93.35.245', password='tsrds')
     #self.channel_sub = 'fm090.9'
     #self.channel_pub = 'fm160.6'

   def get(self, key):
     return self.__conn.get(key)

   def set(self, key, value):
     self.__conn.set(key, value)

   def keys(self, pattern = '*'):
     return self.__conn.keys(pattern)

   def publish(self, msg):
     self.__conn.publish(self.channel_pub, msg)

   def subscribe(self):
     pub = self.__conn.pubsub()
     pub.subscribe(self.channel_sub)
     pub.parse_response()
     return pub


'''
if __name__=='__main__':
  t = RedisHelper()
  t.publish('testsrv2017')
  t.subscribe()
  t.subscribe().parse_response()
'''

