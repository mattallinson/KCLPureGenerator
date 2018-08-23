'''

This script searches google for a name and then 
returns the Pure profile URL if the researcher has one, 
and returns FALSE if they do not. 

This depends on the Pure profile being the first thing that comes up 
if you search "site:https://kclpure.kcl.ac.uk/ FIRST_NAME, LAST_NAME on Google 

'''

import requests 
import sys

GOOGLE_SEARCH_TERM = "https://www.google.com/search?btnI=1&q=site%3Ahttps%3A%2F%2Fkclpure.kcl.ac.uk%2F+"
# bntI=1 makes it the "i'm feeling lukcy search"



class Researcher():
	def __init__(self, name):
		self.name = str(name)
		self.url = " "

	def get_pure_url(self):
		search_term = GOOGLE_SEARCH_TERM + self.name		
		
		res = requests.get(search_term) #make a gooogle I'm Feeling Lucky search of the researcher's name of KCLPure
		if res.url[:15] == "https://kclpure": #if the result is a pure page
			self.url = res.url #sets the URL as the Pure page found
		elif res.url[:29] == "https://www.google.com/sorry/": #if you run this code too often, google will block you
			raise Exception('YOU HAVE ANGERED GOOGLE \n Try again in a few hours')
		else:
			self.url = " " #leaves blank

def main():
	NAME_FILE = sys.argv[1]
	with open(NAME_FILE, 'r') as name_file:
		names = name_file.readlines()

	output = []

	for count, name in enumerate(names,1): 
		print(count,"/",len(names)) #makes the output show where we are
		
		name = name.rstrip() #use rstrip() to remove training newline
		
		researcher = Researcher(name)
		researcher.get_pure_url()
		
		with open("pure-profiles.txt","a") as output:
			output.write(researcher.name + " " + researcher.url)

if __name__ == '__main__':
	main()