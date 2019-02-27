import requests
import csv
from bs4 import BeautifulSoup

csv_file = open('cms_scrape.csv', 'w',  newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['DATE', 'TITLE', 'COMPANY', 'CATGORY', 'LINK'])

page_index = 1
page_limit = 2
while page_index <= page_limit:
    url = 'https://www.net-empregos.com/listagem_livre2_2.asp?page='+ str(page_index) +'&CHAVES=Maia&ZONA=2&CATEGORIA=5'
    linker ='https://www.net-empregos.com'


    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    page_info = soup.find("center")
    page_limit = len(page_info.get_text().replace('\n','').replace(' ',''))

    main_block = soup.findAll("div",{"style":"background-color:#FFFFFF;border:1px solid #C3D9FF"})
    titles = main_block[1].findAll("font",{"style":"FONT-SIZE: 15px; LINE-HEIGHT: 14px"})
    blocks = main_block[1].findAll("table",{"width":"738"})
    blocks_size = len(blocks)

    #For loop that iterates betwen the the job offers 
    for block in range(blocks_size):
        title = titles[block].text.strip()
        company = blocks[block].findAll('td')[3].text.strip()
        date = blocks[block].findAll('td')[5].text.strip()
        catgory = blocks[block].findAll('td')[7].text.strip()
        link = linker + titles[block].find('a').get('href')
        
        #writes all the data to the csv file
        csv_writer.writerow([date,title,company,catgory,link])

    page_index+=1

csv_file.close()