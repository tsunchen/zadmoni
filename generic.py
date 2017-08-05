generic.py
-------
class DefaultService:
    name = 'DefalutService'
    interval = 300
    plugin_name = Unknown
    data_from = 'Agent'
    graph_index = {
        'index': [],
        'title': name,
    }
    lt_operator = [] #if this sets to empty, all the status 
    #will be caculated in > mode, gt = >
