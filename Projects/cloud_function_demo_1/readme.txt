Runs a simple calculation function using the google cloud function named "testfunc". 

################################

To run it,	
	1) Open a console at "~/Desktop/Projects/cloud_function_demo_1"
	2) Run the command "python cloudf.py"

################################

opID list: 

1 -> addition -> op1 + op2
2 -> subtraction -> op1 - op2
3 -> multiplication -> op1 * op2 
4 -> division -> op1 / op2

################################

Deploying gcloud functions (node.js with "npm init")to Google Cloud live servers (takes time): 
	Run console at the directory your nodejs file is at as super user and run the command: 
		"gcloud beta functions deploy <FUNCTIONNAME> --stage-bucket <BUCKETNAME> --trigger-http"

		A usable bucket for "sebit-gcloud-test-1" is "sebit-gcloudtest-1-bucket-1"
