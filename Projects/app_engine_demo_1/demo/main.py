import webapp2
import os
import urllib2

from google.appengine.ext.webapp import template

GCLOUD_FUNC_URL = "https://us-central1-sebit-gcloudtest-1.cloudfunctions.net/helloname?name=umut"

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), "index.html") 
        self.response.out.write(template.render(path, {}))

	response_from_gcloud_function = get_markup_from_url(GCLOUD_FUNC_URL)
	print response_from_gcloud_function

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True) 

def get_markup_from_url(url):
	response = urllib2.urlopen(url)
	page_source = response.read()
	return page_source
