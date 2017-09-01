import template

web_cluster = template.LinuxGenericTemplate()
web_cluster.host = [
    '172.93.35.245',
    '10.0.0.1',
    '192,168.1.100'

]


mysql_group = template.LinuxGenericTemplate2()
mysql_group.host = [
    '172.93.35.245',
    '192.168.0.1',
    '10.0.0.2'
 
]


monitor_group = [web_cluster, mysql_group]

host_conf_dic = {}

if __name__=="__main__":
    for group in monitor_group:
        #print group.name
        for h in group.host:
            #print host, group.service
            if h not in host_conf_dic:
                 host_conf_dic[h] = {}

            for s in group.services:
                 host_conf_dic[h][s.name] = [s.plugin_name, s.interval]


    for h, v in host_conf_dic.items():
        print h, v


