import re
import uuid

import requests
from bs4 import BeautifulSoup

target_url = 'https://tokubai.co.jp/%E8%A5%BF%E5%8F%8B/6386'

r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")

special_sales = []

item_names = soup.select('.name.hoverable_link')

for name in item_names:
    special_sales.append({"name": name.text.strip("\n")})

units = soup.select('.price_unit_and_production_area')

for i in (range(len(units))):
    if i < len(special_sales):
        unit = units[i]
        special_sales[i]["unit"] = unit.text.strip("\n")

prices = soup.select('.number')

for i in range(len(prices)):
    if i < len(special_sales):
        price = prices[i]
        special_sales[i]["price"] = price.text.strip("\n")

# TODO: LazyLoadの画像が取れていない
# images = soup.find_all('img', src=re.compile('^https://image.tokubai.co.jp/images/bargain_images/'))
# print(images)

# for img in images:
#     print(img['src'])
#     r = requests.get(img['src'])
#     with open(str('./picture/')+str(uuid.uuid4())+str('.jpeg'), 'wb') as file:
#         file.write(r.content)

print(special_sales)
