import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com')

content = response.content

# Site
site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

	# Título
	titulo = noticia.find('p', attrs={'class': 'feed-post-link'})

	print(titulo.text)
 