from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import datastore

def index(request):
	return render(request, "personal/home.html")

def contact(request):

	c = datastore.Client()

	kind = "comments"
					
	query = c.query(kind = "comments")
	query.add_filter("posttime", ">", 0)
	query.order = ["-posttime"]
				
	result_list = list(query.fetch())
				
	comment_id_list = []
				
	for r in result_list:
		r = str(r)
		index_start = r.find("u'comments', ") + 13
		index_end = r.find("L", index_start)
		comment_id_list.append(int(r[index_start : index_end]))
					
	comment_final_list = ["Comments: "]
		
	for id in comment_id_list:	
		comment_key = c.key(kind, id)
		ent = c.get(comment_key)
		
		comment = ent.get("comment")
		username = ent.get("username")

		comment_final_list.append(username + ": " + comment)

	return render(request, "personal/basic.html", {'content' : comment_final_list})
