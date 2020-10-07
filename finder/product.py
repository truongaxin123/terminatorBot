from os import name
from typing import Dict, List


class Product:

    def __init__(self, name: str, price: float, info: List[str], img: str, url: str) -> None:
        self.name = name
        self.info =  info
        self.img = img
        self.url = url
        self.price = price

    def getName(self):
        return self.name

    def getInfo(self):
        return self.info

    def getUrl(self):
        return self.url

    def getImg(self):
        return self.img

    def getPrice(self):
        return self.price

    