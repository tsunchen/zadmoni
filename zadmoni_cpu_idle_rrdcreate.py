#!/usr/bin/python
import rrdtool

rrdb=rrdtool.create('zad_cpu_idle_rc.rrd','--step','5','--start','N',
    'DS:zad_cpu_idle:GAUGE:120:U:U',
    'RRA:LAST:0.5:1:600',
    'RRA:AVERAGE:0.5:5:600',
    'RRA:MAX:0.5:5:600',
    'RRA:MIN:0.5:5:600')
if rrdb:
  print rrdtool.error()
