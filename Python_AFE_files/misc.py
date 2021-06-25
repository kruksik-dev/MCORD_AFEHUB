# misc.py
import time
import pyb
import afedrv
import hub
import os 

def HVon(id):
	pyb.Pin.cpu.E12.init(pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
	pyb.Pin.cpu.E12.value(1)
	afedrv.SetAllHV(id)

def HVoff(id):
	pyb.Pin.cpu.E12.init(pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
	pyb.Pin.cpu.E12.value(0)
	afedrv.ClrAllHV(id)

    
def init(id):
	afedrv.SetDac(id, 53, 53)
	afedrv.SetDigRes(id, 0, 200)
	afedrv.SetDigRes(id, 1, 200)
	
def start(*args):
#init, turn on and set voltage in bulk
	for arg in args:
		init(arg)
		print("\n         ##### INIT {} #####\n".format(arg))
		HVon(arg)
		print("\n         ##### HVON {} #####\n".format(arg))
		afedrv.SetDac(arg,55,55)
		afedrv.SetDac(arg,59,59)
		print("\n         ##### AFE DAC 59V RAISED {} #####\n".format(arg))
	print(10*'#')
	print("WSZYSTKO ODPALONE")
	print(10*'#')

def stop(*args):
#take out voltage in bulk
	for arg in args:
		afedrv.SetDac(arg,55,55)
		afedrv.SetDac(arg,53,53)
		HVoff(arg)
		print("\n         ##### HVOFF {} #####\n".format(arg))
	print("FAJRANT, NAPIECIE ZDJETE ZE WSZYSTKIEGO")

def test():
	print(os.linesep)
	
def dhcptest():
	import network 
	lan = network.LAN() 
	lan.active(True)
	lan.ifconfig('dhcp') 
	print(lan)
	
	


								
	
		
		
	
