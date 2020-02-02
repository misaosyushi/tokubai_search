import requests
from bs4 import BeautifulSoup

target_url = 'https://tokubai.co.jp/%E8%A5%BF%E5%8F%8B/6386?content_type=product_summary&from' \
             '=widget_supermarket_300x250&shop_id=6386&target_type=see_more '
r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")

special_sales = []

elems = soup.select('.name.hoverable_link')
for elem in elems:
    print(elem.text)
    special_sales.append(elem.text)

print(special_sales)
