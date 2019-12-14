from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import csv

url = "https://www.encuentra24.com/costa-rica-es/bienes-raices-alquiler-apartamentos/cartago-provincia?q=f_rent.-400|f_currency.USD|number.50"

uClient = ureq(url)
page_html = uClient.read()
uClient.close()

#parsing
page_soup = soup(page_html, "html.parser")
objects = page_soup.findAll("article")
print(len(objects))

#.xsl file
filename = "Apartamentos.csv"
with open(filename, "w", encoding='utf-8', newline="") as f:
    thewriter = csv.writer(f)

    headers = ["Title","Description","Price","Link"]
    thewriter.writerow(headers)
    
    #Loop to aquire basic info
    i = 1
    for object in objects:
        Price = str(object.find("div",{"class":"ann-box-details"}).span.text)
        Title = str(object.find("div",{"class":"ann-box-details"}).a.text)
        Link = "https://www.encuentra24.com/"+object.find("div",{"class":"ann-box-details"}).a["href"]
        try:
            Desc = str(object.find("span",{"class":"ann-box-desc"}).text)
        except:
            Desc = "No Description"
        i = i+1
        thewriter.writerow([Title, Desc, Price, Link])