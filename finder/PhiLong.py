from bs4 import BeautifulSoup
import requests
from product import Product
from typing import List
from urllib.request import urlretrieve

class Finder:

    IMG_FOLDER = 'E:/truongaxin123/terminatorBot/imgs'
    ROOT_URL = 'https://philong.com.vn'
    
    def __init__(self, product: str) -> None:
        self.product = product
        self.founded = 0

    def find(self, number: int) -> List[Product]:
        product_result = []
        r = requests.get('https://philong.com.vn/tim?scat_id=', params={'q':self.product})
        soup = BeautifulSoup(r.text, 'lxml')

        founded = soup.find(class_='list-product-page product-list').div.div.div.div.h1.b.string
        print('tim thay {} san pham'.format(founded.string))

        products = soup.find_all(class_='col-md-3 col-xl-2 col-sm-6 col-xs-6')
        for _product in products:
            # download img of product
            img_url = str(_product.div.a.img['data-src'])
            print(img_url)
            img_name = img_url.split('/')[-1]
            urlretrieve(self.ROOT_URL+img_url, self.IMG_FOLDER+'/'+img_name)
            img_storage = self.IMG_FOLDER+'/'+img_name

            url = _product.div('h4', class_='p-name')[0].a['href']
            name = _product.div('h4', class_='p-name')[0].a['title']
            info = [p.string for p in _product.div('div', class_='p-summary')[0]('p')]
            price = _product.div('span', class_='p-price')[0].string
            product = Product(name,price, info, img= img_storage, url=url)
            product_result.append(product)
        return product_result



if __name__ == "__main__":
    a = Finder('AMD')
    products = a.find(number=2)
    for i in products:
        print(i.getName())
        print(i.getPrice())