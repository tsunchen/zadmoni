import json


def push_all_config_redis(main_instance, host_group):
    host_conf_dic = {}

    for group in host_group:
        #print group.name
        for h in group.host:
            #print host, group.service
            if h not in host_conf_dic:
                 host_conf_dic[h] = {}

            for s in group.services:
                 host_conf_dic[h][s.name] = [s.plugin_name, s.interval]

    for h, v in host_conf_dic.items():
        #print h, v
        host_config_key = "HostConfig::%s" % h
        main_instance.r.set(host_config_key, json.dumps(v))
        print "towrite config into redis: %s" % host_config_key
