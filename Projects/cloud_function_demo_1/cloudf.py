import os
import urllib2

FUNCTION_URL = "https://us-central1-sebit-gcloudtest-1.cloudfunctions.net/"

def get_result_from_function(op1, op2, opid):
	response_html = urllib2.urlopen(FUNCTION_URL + "testfunc?op1=%s&op2=%s&opid=%s" % (op1, op2, opid))
	return response_html.read()

def clear_console():
	os.system("clear")

while True:
	print ""
	
	try:
		user_op1  = int(raw_input("First operand: "))
		user_op2  = int(raw_input("Second operand: "))
		user_opid = int(raw_input("Operation id: "))

	except ValueError:
		print "\nEnter an integer."

	else:
		clear_console()
		print get_result_from_function(user_op1, user_op2, user_opid)

	

	
