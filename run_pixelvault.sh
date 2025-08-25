#!/bin/bash
export PATH=$PATH:/usr/bin
export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
export PYTHONPATH=$HOME/.local/lib/python3.13/site-packages:$PYTHONPATH
python3 /home/php/Desktop/stuff/projects/pixelvault/main.py

# change to your path of the script
