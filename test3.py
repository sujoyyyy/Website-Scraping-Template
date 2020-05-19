import bs4 as bs
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url= 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on&page=2'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html , "html.parser")
containers=page_soup.findAll("div",{"class" : "_3O0U0u"})
print(len(containers))
filename="products2.csv"
f=open(filename,"w",encoding='utf-8-sig')
headers= "Name, Rating, Price\n"
f.write(headers)

for i in containers:
    products= i.findAll("a",{"class": "_2cLu-l"})
    prod= products[0].text.strip()
    print(prod)
    pricings=i.findAll("div",{"class": "_1vC4OE"})
    price = pricings[0].text.strip()
    try:
        ratings= i.findAll("div",{"class": "hGSR34"})
        rate= ratings[0].text.strip()
    except:
        rate=""
    print(rate)
    print(price)
    f.write(prod.replace(",","|")+","+rate+","+price.replace(",","")+"\n")












f.close()