import sys

import socket

host = "google.com"
ports = [21, 22, 23, 25, 80, 3306, 121]

for port in ports:
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.5)
		code = client.connect_ex((host, port))
		if code == 0:
			print("\033[32m[+] {} open".format(port))
	except:
		print("Ocorreu um erro")
