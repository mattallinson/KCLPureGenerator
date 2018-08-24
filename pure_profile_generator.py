'''

This script searches google for a name and then 
returns the Pure profile URL if the researcher has one, 
and returns FALSE if they do not. 

This depends on the Pure profile being the first thing that comes up 
if you search "site:https://kclpure.kcl.ac.uk/ FIRST_NAME, LAST_NAME on Google 

'''

from namecleaner import namecleaner
import requests 
import sys
from bs4 import BeautifulSoup

PURE_SEARCH_TERM = "https://kclpure.kcl.ac.uk/portal/en/persons/search.html?search="

class Researcher():
	def __init__(self, name):
		self.name = str(name)
		self.url = " "

	def pure_search(self):
		search_term = PURE_SEARCH_TERM + self.name

		res = requests.get(search_term)
		soup = BeautifulSoup(res.text,'html.parser')
		try:
			self.url = "https://kclpure.kcl.ac.uk" + str(soup.find('a', class_ = "link person").get('href'))
			print(self.name, "\n\tURL Found 👍")
		except: 
			self.url = " --not found -- "
			print(self.name, "\n\tNO URL FOUND ⚠️")


def main():
	NAME_FILE = sys.argv[1]
	with open(NAME_FILE, 'r') as name_file:
		names = name_file.readlines()

	output = []

	for count, name in enumerate(names,1): 
		print(count,"/",len(names)) #makes the output show where we are
		
		name = namecleaner(name).rstrip() #use rstrip() to remove training newline
		
		researcher = Researcher(name)
		researcher.pure_search()
		
		with open("pure-profiles.txt","a") as output:
			output.write(researcher.name + ", " + researcher.url + "\n")

if __name__ == '__main__':
	main()