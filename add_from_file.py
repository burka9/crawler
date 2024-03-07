from sys import argv
from add_service import add_service
from urllib import parse


try:
	_, file = argv
	count = 0
	skip = 0
 
	with open(file, 'r') as file:
		urls = file.read()
		for url in urls.split('\n'):
			url = parse.unquote(url.strip())
			try:
				add_service(url)
				count += 1
			except:
				skip += 1
  
	print(f'Added {count} services')
	print(f'Skipped {skip} services')
except Exception as ex:
	print(ex)
	exit(1)
