#!/bin/bash
cd ~/download/kcptun/
sh kcptunstop.sh
echo "Restarting Kcptun..."
sh kcptunc_start.sh
