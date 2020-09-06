import os

"""
Use arp to determine all devices connected to a network
"""

devices = []
for device in os.popen('arp -a'): 
    print(device)