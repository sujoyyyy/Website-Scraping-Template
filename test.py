import bs4 as bs
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url= 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38'
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html , "html.parser")
#print(page_soup.body.p)
containers=page_soup.findAll("div",{"class" : "item-container"})
#print(len(containers))
#print(soup.prettify(containers[0]))
#i=containers[0]
#print(i.div.div.a)

filename="products.csv"
f=open(filename,"w")
headers= "Brand, Product_Name, Shipping_details\n"
f.write(headers)


for i in containers:
    prod = i.a.img["alt"]
    brand_container=  i.findAll("a",{"class":"item-brand"})
    brand= brand_container[0].img["title"].strip()
    ship_contain= i.findAll("li",{"class":"price-ship"})
    shipping= ship_contain[0].text.strip()
    print("Brand:",brand)
    print("\nProduct name:",prod)
    print("\nShipping details:",shipping)
    print("\n")
    f.write(brand+","+prod.replace(",","|")+","+shipping+"\n")

f.close()