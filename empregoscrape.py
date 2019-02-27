import requests
from bs4 import BeautifulSoup

url = 'https://www.net-empregos.com/listagem_livre2_2.asp?page=1&CHAVES=Maia&ZONA=2&CATEGORIA=5'
linker ='https://www.net-empregos.com'
# tier_dict = {}
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# Bundle Tiers
main_block = soup.findAll("div",{"style":"background-color:#FFFFFF;border:1px solid #C3D9FF"})
titles = main_block[1].findAll("font",{"style":"FONT-SIZE: 15px; LINE-HEIGHT: 14px"})
blocks = main_block[1].findAll("table",{"width":"738"})
blocks_size = len(blocks)

print(titles[1].find('a').get('href'))

for block in range(blocks_size):
    title = titles[block].text.strip()
    company = blocks[block].findAll('td')[3].text.strip()
    date = blocks[block].findAll('td')[5].text.strip()
    catgory = blocks[block].findAll('td')[7].text.strip()
    link = linker + titles[block].find('a').get('href')
    print (date,title,company,catgory,link, '\n\n')  


# for tier in tiers:
#     # Only for sections that have a headline
#     if tier.select(".dd-header-headline"):
#         # Grab tier name (and price)
#         tiername = tier.select(".dd-header-headline")[0].text.strip()
        
#         # Grab tier product names
#         product_names = tier.select(".dd-image-box-caption")
#         product_names = [prodname.text.strip() for prodname in product_names]
        
#         # Add one product tier to our datastructure
#         tier_dict[tiername] = { "products": product_names }


# # After we build our datastructure...
# for tiername,tierinfo in tier_dict.items():
#     print(tiername)
#     print("########################")
#     print("\n".join(tierinfo['products']))
#     print("\n\n")