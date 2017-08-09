This application lives at Google Cloud Platform servers.

To see it in action, visit "35.195.58.189" (this ip can be tied to an owned domain or subdomain)

	* It uses  HTML nad python (cgi) on an apache 2 server hosted on Compute Engine (which runs Debian 8.0)

	* The latest source code is available here in this directory, but the live and latest code is 
		is always at the server. 

Some important things to know about the debian/apache platform:
	
	* Connect via SSH: 

		ssh -i ~/.ssh/my-ssh-key umut@35.195.58.189
		or webapp: https://ssh.cloud.google.com/projects/sebit-gcloudtest-1/zones/europe-west1-b/instances/instance-sebit-gcloudtest-1?authuser=0&hl=en_US&projectNumber=794201115669

	* HTML location:
	
		/var/www/html/index.html

	* Error log location:

		/var/log/apache2/error.log

	* cgi scripts location:

		/usr/lib/cgi-bin/

	* restart apache2

		sudo service apache2 restart

###################################

when ssh'ed to the server run the following commands in order:

	1) "sudo -s" or "sudo su"
	2) "cd /"

Since the live code lives on the web and the console development using vim is not particularly great,
	I have written a custom Python script to sync the code between the server and raw code files. This python script
	can be found in this directory as "sync.py"

I have chosen pastebin to host the raw code files since the raw links do no change everytime the files is updated
	like gist. In a production environment, a safe and expandable solution would be to write a custom Python script
	that retrieves the code from a google cloud NoSQL file storage. This was simply overkill for my purposes.

Later I have found that raw project file URLs at github (not gist) do not change too. So pastebin links in the sync.py 
	can just be swapped with corresponding github pages in my case, however it doesnt realy matter.

####################################

File structure:
	
	"html" directory contains the html files including the index.html (which is the home html page)
	"script_cgi" directory contains the Python scripts. display.py is the script that displays the entered values.
							    table.py   is the script that shows all of the cars in the datastore(kind="cars")
	"scripts_custom" directory contains the sync.py file.

####################################


