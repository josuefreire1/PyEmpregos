import os
import urllib.request
from bs4 import BeautifulSoup as soup

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

def search_by_category(cat):
	maxsize = 2
	i = 1

	while i < maxsize +1:

		myurl = 'https://www.net-empregos.com/listagem_livre2_2.asp?page=' + str(i) + '&CHAVES=maia&ZONA=2&CATEGORIA='+ str(cat)

		req = urllib.request.Request(myurl)
		with urllib.request.urlopen(req) as response:
			page_html = response.read()

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
		print("\n")

## simple menu [FIX]
menu=True
cat= 99
while menu:
	print ("""Menu:
	1.Analise de Sistemas
	2.Formação
	3.Gestão de Redes
	4.Internet
	5.Multimedia
	6.Programação
	7.Técnico de Hardware
	8.Comercial/Gestor de Conta
	""")
	menu = input("List (ENTER to exit):")
	if menu=="1":
		cat = 38
	elif menu=="2":
		cat = 34
	elif menu=="3":
		cat = 38
	elif menu=="4":
		cat = 37
	elif menu=="5":
		cat = 36
	elif menu=="6":
		cat = 5
	elif menu=="7":
		cat = 49
	elif menu=="8":
		cat = 56
	elif menu !="":
		print("\n Not Valid Choice Try again")
		cat = 99

	if cat != 99:
		cls()
		search_by_category(cat)
		print("\n\nENTER to go back to menu!")
		input()
		cls()
