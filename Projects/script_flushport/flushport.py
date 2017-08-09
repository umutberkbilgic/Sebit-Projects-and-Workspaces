import os

port = 0
MAX_PORT = 65,535	

port = int(input("Port to be cleansed of ongoing processes: "))

while((port < 0) and (port > MAX_PORT)):
	print("Please enter a valid port to continue... \n")
	port = int(input("Port to be flushed of ongoing processes: "))

if(port < 1028):
	sure = ""

	while(sure != "y" or sure != "Y" or sure != "n" or sure != "N"):
		print("\nThis port is only available for processes with root access.")
		sure = str(raw_input("Are you sure you want to flush the processes on this port anyway?(y/n): "))

		if(sure == "y" or sure == "Y"):
			os.system("\nfuser -k " + str(port) + "/tcp\n")
			break
		elif(sure == "n" or sure == "N"):
			print("\nINFO (FLUSHPORT) - Canceled operations. No change has been made.\n")
			exit()
		else:
			print("\nPlease enter a valid response.\n")
else:
	os.system("\nfuser -k " + str(port) + "/tcp\n")

print("\nINFO (FLUSHPORT) - Port " + str(port) + " has been flushed.\n")

prompt = ""

while(prompt != "y" or prompt != "Y" or prompt != "n" or promt != "N"):
	prompt = str(raw_input("Would you like to host new app.yaml on localhost:8080? (y/n): "))

	if(prompt == "y" or prompt == "Y"):
		print("INFO (FLUSHPORT) - Starting hosting new Google Cloud App.")
		print("INFO (FLUSHPORT) - Starting dev_appserver on the app.yaml on the current directory.")
		os.system("\ndev_appserver.py ./")
		exit()
	elif(prompt == "n" or prompt == "N"):
		print("Exitted without hosting new Google Cloud App.")
		exit()
	else:
		print("\nPlease enter a valid response.\n")
	
	


