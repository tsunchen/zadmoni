#!/bin/bash
cd ~/download/kcptun/
./server_linux_amd64 -c /etc/kcptun.json > kcptun.log 2>&1 &
echo "Kcptun started."
