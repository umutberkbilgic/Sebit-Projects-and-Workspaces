import urllib2
import os
import json

API_URL = "https://swapi.co/api/starships/"

number = raw_input("> ") 

result = os.popen("curl " + API_URL + number + "/").read()
os.system("clear")
print ("Name: " + json.loads(result)["name"])

	
