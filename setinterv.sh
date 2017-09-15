#!/bin/bash
#
while true; do
    RES=`sar 1 3| grep "^Average:" | sed -e 's/.*: \(.*\)$/\1/' | awk '{print $7}'`
    rrdtool update zadmoni_cpu_idle.rrd N:$RES
    rrdtool graph idle.png --step 5 -s 1505432685 -t cpu_idle -v idle_val --watermark zadmoni_cpu  DEF:idle_val=zadmoni_cpu_idle.rrd:cpu_idle:AVERAGE AREA:idle_val#00FF00:idle_line
    cp  -n /root/rrdtest/idle.png /ngx-html/idle.png
done
