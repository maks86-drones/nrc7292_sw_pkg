#!/usr/bin/python

import sys
import os
import time
import commands
 
def run_newrapeek():
	os.system("sudo killall -9 wireshark-gtk")
	os.system("sudo rmmod nrc")

	os.system("sudo insmod ./nrc.ko fw_name=uni_s1g.bin hifspeed=16000000")
	time.sleep(5)

	os.system('sudo ifconfig wlan1 down; sudo iw dev wlan1 set type monitor; sudo ifconfig wlan1 up')

	regstr = "sudo iw reg set " + str(sys.argv[1])
	os.system(regstr)

	cmdstr = "sudo iw dev wlan1 set channel " + str(sys.argv[2])
	os.system(cmdstr)
	time.sleep(3)

	os.system('sudo ./rpcapd -4 -n -p 1234')

total = len(sys.argv)
cmdargs = str(sys.argv)

if total < 3:
	print ("NewraPeek Usage: run_remote.py countrycode channelnumber")
else:
	print ("NewraPeek country code:   %s " % str(sys.argv[1]))
	print ("NewraPeek channel number: %s " % str(sys.argv[2]))
	run_newrapeek()
