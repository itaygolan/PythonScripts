import os
import subprocess  # spawn new subprocesses
import sys

from decouple import config


"""
Simple python script that detects when someone joins the home network and notifes via
say() command
"""

IP_NETWORK = config("IP_NETWORK")
IP_DEVICE = config("IP_DEVICE")

# execute pring in a new process and pipe to current config
proc = subprocess.Popen(["ping", IP_NETWORK], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    connected_ip = line.decode("utf-8").split()[3]
    if connected_ip == IP_DEVICE:
        subprocess.Popen("say", "Someone just entered the network")
