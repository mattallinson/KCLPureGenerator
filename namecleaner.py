'''
Takes a list of names and removes titles, as these appear to ruin the effectiveness of a PURE search
Can be used standalone on a textfile of names

'''

import sys

TITLES = ["dr ", "mr ", "ms ", "prof ", "professor ", "ms ", "miss ", "mrs "]

def namecleaner(name):

	for title in TITLES:
		
		if title in name.lower():
			name = name.lower().replace(title, "")

	return name.lower() #returns it as lower bc I'm superstitious that this helps the KCLPure search
	
		

def main():
	
	NAMEFILE = sys.argv[1]
	CLEANED_NAMEFILE = "cleaned_" + NAMEFILE

	with open(NAMEFILE, 'r') as namefile:
		names = namefile.readlines()

	for name in names:
		clean_name = (namecleaner(name)).title()
		
		with open(CLEANED_NAMEFILE,'a') as cleaned_namefile:
			cleaned_namefile.write(clean_name)

if __name__ == '__main__':
	main()