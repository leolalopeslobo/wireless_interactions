#!\usr\bin\env python
from scapy.all import *
import os
#import timeit

print("Kindly Enter a Interface")
i=input()
os.system("sudo airmon-ng start "+i)
os.system("sudo xterm -e airodump-ng "+i+"&")
count=0


interface=''+i
try:

  print("\n Scan conducted by WLSR\n")

  def sniffReq(p):
    print("\n")
    if p.haslayer(Dot11Deauth):
      print("Deauthentication Attack found on Ap With Mac ID (Source Mac address of sender) ",p[Dot11].addr2,"Destination mac",p[Dot11].addr1,"Mac Address Of Ap", p[Dot11].addr3,end="\n\n")
      global count
      count +=1
      print("The count is ",count)



    elif p.haslayer(Dot11AssoReq):
      print("Asso req found")
    
    
    elif p.haslayer(Dot11Beacon):
      print("")
      summary=Dot11.mysummary
      time=Dot11.time
      Update_sent_time=Dot11.update_sent_time
      get_field=Dot11Beacon.get_field
      show=Dot11Beacon.show
      show2=Dot11Beacon.show2
      wirelength=Dot11Beacon.wirelen
      fragments=Dot11Beacon.fragment




    elif p.haslayer(Dot11Disas):
      print("Disassociation Attack found on Ap With Mac ID (Source Mac address of sender) ",p[Dot11].addr2,"Destination mac",p[Dot11].addr1,"Mac Address Of Ap", p[Dot11].addr3,end="\n\n")


    elif p.haslayer(Dot11EltVendorSpecific):
      print("")

    elif p.haslayer(Dot11ProbeReq):
      print("Probe Request")

    elif p.haslayer(Dot11ProbeResp):
      print("Probe response")

    elif p.haslayer(Dot11Encrypted):
      print("Encryption")

    





except:
	
  	print("Could not find your wifi adapter")

sniff(iface=interface,prn=sniffReq)









