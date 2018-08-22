'''

This script searches google for a name and then 
returns the Pure profile URL if the researcher has one, 
and returns FALSE if they do not. 

This depends on the Pure profile being the first thing that comes up 
if you search "site:https://kclpure.kcl.ac.uk/ FIRST_NAME, LAST_NAME on Google 

'''

import requests 

GOOGLE_SEARCH_TERM = "https://www.google.com/search?btnI=1&q=site%3Ahttps%3A%2F%2Fkclpure.kcl.ac.uk%2F+"
# bntI=1 makes it the "i'm feeling lukcy search"

class Researcher():
	def __init__(self, name):
		self.name = str(name)
		self.url = None

	def get_pure_url(self):
		search_term = GOOGLE_SEARCH_TERM + self.name
		print(search_term)
		res = requests.get(search_term)
		if res.url[:15] == "https://kclpure": #if the result is a pure page
			self.url = res.url
		else:
			self.url = None