#A program to ask user input of news category for the NY Times
#output is the top 5 'latest news' articles from that category
from bs4 import BeautifulSoup
import requests
def latest_news(cat_input):
    html_file=requests.get("https://www.nytimes.com/section/"+cat_input).text
    soup=BeautifulSoup(html_file, "lxml")
    #print (soup.prettify("utf-8"))
    i = 1
    for article in soup.find_all("div", class_="css-1l4spti"):
        headline=article.h2.text
        print ("Headline:", headline)
        summary=article.p.text
        print ("Summary:", summary)
        link="https://www.nytimes.com"+article.a.attrs["href"]
        print ("Click here to read this story:", link)
        print ("\r\n")
        i+=1
        if i<6:
            continue
        else: break

cat_input=input("Please enter the news category you wish to view: \n")
latest_news(cat_input)
