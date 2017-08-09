My first application that uses the Datastore API. Works like a backend peek tool
	more than a frontend application. Users can be added, updated, deleted, filtered and queried based on any property, 
	searched for with non-case-sensitive names. 

################################

To run it,
	1) Open a console at "~/Desktop/Projects/datastore_demo_console_1"
	2) Run the command "python datastore_demo_console_1.py"

################################

[1]: Display spesific user -> need to write the exact name of the user to view its info that is saved
				at datastore (kind="users")
[2]: Add or update user -> Adds a new user to datastore (or updates it if the name already exists.)

[3]: Delete user -> deletes the user with the given name

[4]: Filter -> uses direct gQuery commands. for example "id" ">" "0" would list every user
				or "name" "=" "umut" would list every user with the name "umut"
				exactly.

[5]: Search -> Search for a username. For exampel searching for "umut" can find "UMUT STRING STRING" or "UmuTtt"
				since it finds the query in non case sensitive form in every user.

[0]: Exit: exits the app.

#################################

useridcount.txt saves the current user id. This could easily be stored at datastore but
	it is probably not worth the connection latency and overhead.
