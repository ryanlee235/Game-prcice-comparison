from bs4 import BeautifulSoup
from flask import Flask
import requests
from time import sleep
#from models import CdKeys, InstantGaming, G2A
from flask_sqlalchemy import SQLAlchemy




PATH ="C:\Program Files (x86)\chromedriver.exe"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-langauge': 'en-US,en;q=0.9'
}

def instant_gaming(db, link):
    #gets website, added headers so website doesnt know its a python script
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, features='html.parser')
    #finding the page numbers at the bottom of the page
    pages = soup.find_all(class_='pagination')

    for page in pages:
         page_number = page.find_all("a")

    #grabs the page number
    page_number = int(page_number[1].text)

    #looping through each content on each page
    for pages in range(1, page_number + 1):

        #link loads the next page
        link = f"https://www.instant-gaming.com/en/search/?type%5B0%5D=steam&page={pages}"
        r = requests.get(link, headers=headers).text
        soup = BeautifulSoup(r, "html.parser")
        contanier = soup.find_all(class_="item force-badge")

        for items in contanier:
            title = items.find(class_="title").text
            price = items.find(class_="price").text
            links = items.find("a").get("href")
            pictures = items.find(class_="picture").get("data-src")



def cdkeys():

   for page_number in range(1, 400):
        link = f"https://www.cdkeys.com/pc?p={page_number}"
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        container = soup.find_all(class_="product-item-info")
 
        for name in container:
            game_name = name.find(class_="product-item-link").text
            game_price = name.find(class_="price").text
            game_link = name.find(class_="product-item-link").get("href")
            game_pictures =name.find(class_="product-image-photo").get("src")
            #user = CdKeys(name=game_name, price=game_price, link=game_link, picture=game_pictures)
            print(game_name, game_price, game_link, game_pictures)

            #db.session.add(user)
            #db.session.commit()

            
                  
def g2a(db):
    for page in range(1, 999):
        web_link = f"https://www.g2a.com/category/gaming-c1?f%5Bdrm%5D%5B0%5D=1&f%5Bregions%5D%5B0%5D=8355&page={page}"

        r = requests.get(web_link, headers=headers).text
        soup = BeautifulSoup(r,"html.parser")
        container = soup.find_all(class_="sc-eGJWMs hPxtgO indexes__StyledProductBox-wklrsw-81 dRNOEq")
        
        for items in container:
            name = items.find(class_="sc-iqAclL sc-dIsUp dJFpVb eHDAgC sc-kHWWYL kfrcst").text
            game_price = items.find(class_="sc-iqAclL sc-crzoAE dJFpVb eqnGHx sc-bqGGPW fIHClq").text
            link_name = "https://www.g2a.com" + items.find("a").get('href')
            picture = items.find("img").get("src")
            
            #games = G2A(name=name, price=game_price, link=link_name, picture=picture)
    

            #db.session.add(games)
            #db.session.commit()


