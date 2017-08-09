import urllib2
import os
import json

API_URL = "https://swapi.co/api/"

prompt_dict ={"1" : "people",
			  "2" : "planets",
			  "3" : "films",
			  "4" : "species",
			  "5" : "vehicles",
			  "6" : "starships"}

def clear():
	os.system("clear")

def print_dict(dict):
	for key in dict:
		print (str(key) + ": " + str(dict[key]) + "\n")
	
while True:
	print_dict(prompt_dict)
	prompt_key = raw_input("\n> ")

	query = prompt_dict[prompt_key]
		
	result = os.popen("curl " + API_URL + query + "/").read()
	os.system("clear")
	json_dict = json.loads( result )
		
	print_dict(json_dict)

