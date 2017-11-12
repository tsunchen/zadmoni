from conf import host

import json,time,operator


def push_all_config_redis(main_instance, host_group):
    host_conf_dic = {}

    for group in host_group:
        print group.name
        for h in group.host:
            #print host, group.services
            if h not in host_conf_dic:
                 host_conf_dic[h] = {}

            for s in group.services:
                 host_conf_dic[h][s.name] = [s.plugin_name, s.interval]

    for h, v in host_conf_dic.items():
        #print h, v
        host_config_key = "HostConfig::%s" % h
        main_instance.r.set(host_config_key, json.dumps(v))
        print "towrite config into redis: %s" % host_config_key



def fetch_all_config(host_group):
    host_conf_dic = {}

    for group in host_group:
        print group.name
        for h in group.host:
            #print host, group.services
            if h not in host_conf_dic:
                 host_conf_dic[h] = {}

            for s in group.services:
                 host_conf_dic[h][s.name] = s

    for h, v in host_conf_dic.items():
        print h, v
    return host_conf_dic    


def data_process(main_instance):
    print '--- to handle monitor data ---'
    all_host_config = fetch_all_config(host.monitor_group)
    #for i in range(15):
    while True:
      for ip, service_dic in all_host_config.items():
        for service_name, s_instance in service_dic.items():
            service_redis_key = "ServiceData::%s::%s" % (ip, service_name)
            s_data = main_instance.r.get(service_redis_key)
            if s_data:
                 s_data = json.loads(s_data)
                 print '###>'  , s_data
                 time_stamp = s_data['time_stamp']
                 if time.time() - time_stamp < s_instance.interval:
                    if s_data['data']['status']==0: # data valid
                      print "\033[32;1m Host[%s] Service[%s] data valid\033[0m" % (ip, service_name)
                      #print service_name, s_data['data']
                      for item_key, item_dic in s_instance.triggers.items():
                        service_item_handler(main_instance, item_key, item_dic, s_data)
                      #pass
                    else:
                         print "\033[31;1m Host[%s] Service[%s] plugin error\033[0m" % (ip, service_name)
                 else: #data expried
                    expired_time = time.time() - time_stamp - s_instance.interval
                    print "\033[31;1m Host[%s] Service[%s] data expired[%s] secs\033[0m" % (ip, service_name, expired_time)          
            else:
                 print "\033[31;1m No data found in redis of service [%s] hostname [%s]\033[0m" % (service_name, ip)
    time.sleep(1)


def service_item_handler(main_instance, item_key, item_dic, client_s_data):
    #print '===>', item_key, client_s_data['data'][item_key]
    item_data = client_s_data['data'][item_key]
    warning_val = item_dic['warning']
    #print type(item_data)
    critical_val = item_dic['critical']
    oper = item_dic['operator']
    
    oper_func = getattr(operator,oper)

    if item_dic['data_type'] is float:
        item_data = float(item_data)
        warning_res = oper_func(item_data, warning_val)
        critical_res = oper_func(item_data, critical_val)
        print "warning: [%s] critical: [%s]" % (warning_val, critical_val)
        print 'warning, critical ', warning_res, critical_res
        if critical_res:
            print u"\033[41;1mCritical::\033[0mHost[%s] Service[%s] Threshold[%s] Current[%s] of [%s]" % (client_s_data['hostname'], client_s_data['service_name'], critical_val, item_data, item_key)
        elif warning_res:
            print u"\033[43;1mWarning::\033[0mHost[%s] Service[%s] Threshold[%s] Current[%s] of [%s]" % (client_s_data['hostname'], client_s_data['service_name'], warning_val, item_data, item_key)       
        else:
            print u"\033[42;1mNormal::\033[0mHost[%s] Service[%s] Current[%s] of [%s]" % (client_s_data['hostname'], client_s_data['service_name'], item_data, item_key)
