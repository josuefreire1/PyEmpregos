from urllib.request import urlopen as uRed
from bs4 import BeautifulSoup as soup


maxsize = 3
i = 1

while i < maxsize +1:

	myurl = 'https://www.net-empregos.com/listagem_livre2_2.asp?page='+ str(i) +'&CATEGORIA=38%2C+37%2C+35%2C+5%2C+49&ZONA=2&cidade=Maia'

	uClient = uRed(myurl)
	page_html =uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("font",{"style":"FONT-SIZE: 15px; LINE-HEIGHT: 14px"})
	pag = page_soup.find("table", {"height": "6","width": "0"})
	maxsize = len(pag.get_text().replace('\n','').replace(' ',''))
	print("Page:", i)
	
	tam = len(containers)
	for y in range(tam):
		print(containers[y].a.get_text())
	i+=1