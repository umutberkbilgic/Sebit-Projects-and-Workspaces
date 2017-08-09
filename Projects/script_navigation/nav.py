import os

def display():
	print("--------------------------------------")
	print("|| Options                          ||")
	print("|| [1] : guestbook web app          ||")
	print("|| [2] : tomcat directory           ||")
	print("|| [3] : helloworld web app         ||")
	print("|| [4] : gcloud functions directory ||")
	print("|| [5] : helloworld simple function ||")
	print("|| [0] : Exit                       ||")
	print("--------------------------------------")

user = -1
lut = [ "/home/umut/guestbook",
        "/home/umut/tomcat",
	"/home/umut/pygitsamples/appengine/standard/hello_world",
	"/home/umut/gcloud_func_test",
	"/home/umut/helloworld" ]
	
display()

while(user != 0):
	user = int(input("\n> "))
	if((user > 0) and (user < len(lut) + 1)): # is valid
		os.chdir(lut[user - 1])
		print("")
		os.system("sudo -s") # sudo -s for root powers
	
	
	
