from os import write
import requests
from bs4 import BeautifulSoup
import csv

url = "https://market.csgo.com/?t=all&p=1&sd=desc"

req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, 'lxml')

# with open("index.html", encoding="UTF=8") as file:
#     src = file.read()

total_amounts = soup.find(id = "total_pages").text
total_amounts = int(total_amounts)
with open("data.csv", "w", encoding="utf=8") as file:
        writer = csv.writer(file)
        writer.writerow(("name", "price"))
for total_amount in range(1, 2):
    url = f"https://market.csgo.com/?t=all&p={total_amount}&sd=desc"
    req = requests.get(url)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    price = soup.find(id = "applications").find_all(class_="price")
    div_block = soup.find(id = "applications")
    gun_name = soup.find_all(class_="name")  
    spisok = []
    spisok_cs = []
    for item_gun in gun_name:
        item_gun = item_gun.text
        spisok_cs.append(item_gun)
    for item_price in price:
        item_price = item_price.text
        spisok.append(item_price)

    # def prices():
    #     for item_price in price:
    #         item_price = item_price.text
    #         spisok.append(item_price)
    #     str = ''
    #     price_amount = str.join(spisok)
    #     return price_amount
    # price_fun = prices()

    # def guns():
    #     for item_gun in gun_name:
    #         item_gun = item_gun.text
    #         spisok_gun.append(item_gun)
    #     str = ''
    #     guns_name = str.join(spisok_gun)
    #     return guns_name
    # guns_fun = guns()

    with open("data.csv", "a", encoding="utf=8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for i in range(len(spisok)):
            # print(spisok_cs[i], spisok[i])
            writer.writerow((spisok_cs[i], spisok[i]))
    print(f'{total_amount} сделано')


