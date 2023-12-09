import requests
from bs4 import BeautifulSoup

Page = requests.get('https://books.toscrape.com/')

Soup = BeautifulSoup(Page.content, 'html.parser')

path = 'div.page div.page_inner div.row div.col-sm-8.col-md-9 section div ol.row li article.product_pod'

def name():
    Namelist = Soup.select(path+" h3 a")
    Name = [names.string for names in Namelist]

    return Name


def Rating():
    Stars = Soup.select(path+" p.star-rating")
    stars = [Star.attrs.get('class', []) for Star in Stars]
    star = [a[1] for a in stars]
    return star

def Link():
    Namelist = Soup.select(path+" h3 a")
    Name = [names.attrs['href'] for names in Namelist]

    return Name
i = 0
l = Link()
n = name()
s = Rating()
a = len(name())
for i in range(a):
    print(n[i])
    print(l[i])
    print(s[i], "stars")
    print("--------------------------")