#!/bin/python3
import time
import os,subprocess

while(1):
    os.system("bash -c  \"echo \`awk '/^Mem/' <(free -h)\`> memory.html\"")
    time.sleep(3)
