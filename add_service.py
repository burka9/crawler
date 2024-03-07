template = """

  {crawler_name}:
    extends:
      service: crawler_base
    container_name: {crawler_name}
    environment:
      spider_name: {spider_name}
      start_url: {url}
    depends_on:
      - database

"""
ignore_urls = [
	'https://bbc.com',
	'https://fanabc.com',
 	'https://www.ethiopianreporter.com',
 	'https://ethiopianreporter.com',
  'https://am.wikipedia.org'
]


def render_template(_template, **kwargs):
	return _template.format(**kwargs)




from sys import argv
import string
from urllib import parse

def add_service(url):
	file_path = 'docker-compose.yml'

	with open(file_path, 'r+') as file:
		file_content = file.read()

		# Generate spider_name from the url by removing all punctuations
		url = f'https://{url}' if not url.startswith('http') else url
		_url = parse.urlparse(url)
		spider_name = url.translate(str.maketrans('', '', string.punctuation)).replace('https', '').replace('http', '')
		crawler_name = _url.netloc.replace('.', '_')

		for _ in ignore_urls:
			if _url.netloc == parse.urlparse(_).netloc:
				print(f'skipped existing spider {spider_name}')
				exit(1)


		if file_content.__contains__(_url.netloc):
			print(f'skipped existing spider {spider_name}')
			exit(1)
		else:
			file.write(render_template(
				template,
				crawler_name=crawler_name,
				spider_name=spider_name,
				url=url
			))
			print(f'added spider {spider_name} to docker-compose.yml')


def main(args):
	try:
		add_service(args[1])
	except Exception as ex:
		print(ex)
		print('Usage: python add_service.py <url>')
		exit(1)

if __name__ == '__main__':
	main(argv)
