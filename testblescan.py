
import blescan
import socket
import sys

import bluetooth._bluetooth as bluez

dev_id = 0

dgramSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM
                          )

try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 20)
	print "----------"
	for beacon in returnedList:
                Mac =beacon[0:17]
		Rssi = beacon[19:]

		print 'mac %s' %Mac
		print 'Rssi %s' %Rssi
