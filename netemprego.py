from urllib.request import urlopen as uRed
from bs4 import BeautifulSoup as soup


maxsize = 2
i = 1

while i < maxsize +1:

	myurl = 'https://www.net-empregos.com/listagem_livre2_2.asp?page=' + str(i) + '&CHAVES=maia&ZONA=2&CATEGORIA=38'

	uClient = uRed(myurl)
	page_html =uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("font",{"style":"FONT-SIZE: 15px; LINE-HEIGHT: 14px"})
	tam = len(containers)
	pag = page_soup.find("table", {"height": "6","width": "0"})

	print("Pag:", i, "Items:", tam)

	if pag == None:
		i=3
	else:
		maxsize = len(pag.get_text().replace('\n','').replace(' ',''))
		i+=1

	for y in range(tam):
		print(containers[y].get_text())
input()