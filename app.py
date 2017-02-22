#coding:utf-8

import time
import datetime
import commands

print("ISRA application monitoring started")

while True:
    sysctl = str(commands.getoutput("systemctl status isra-cu.service"))
    date = str(datetime.datetime.today())    
    print(date)
    print(sysctl)
    time.sleep(20)
