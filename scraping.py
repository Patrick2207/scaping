from bs4 import BeautifulSoup

import requests

html = requests.get("https://ge.globo.com/futebol/brasileirao-serie-a/").content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

tabela = soup.find("span", class_="glb-grid")

print(tabela.string)
