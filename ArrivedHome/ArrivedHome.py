import os
import time
import sys
import subprocess

from decouple import config

os.system('clear')
deviceIP = config('IP_DEVICE')
cacheFolder = "cache/"
cacheFileName = time.time()
filePath = cacheFolder + str(cacheFileName)

def checkForDevice():
	# See if the device has connected to the network
	systemCommand = "sudo arp-scan -l > " + filePath
	os.system(systemCommand)
	with open(filePath) as fileObj:
		for line in fileObj.readlines():
			if deviceIP in line:
				return True
	return False

def connectionDaemon():
    while True:
		# Keep on searching, yo! (Indefinitely)
        connected = checkForDevice()
        if (connected == True):
            os.system('clear')
            os.system("say 'someone is home'")
            break
        else:
            print("Device is OFFLINE")

connectionDaemon()