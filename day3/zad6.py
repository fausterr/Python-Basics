import requests
from bs4 import BeautifulSoup

# res = requests.get("http://scanme.nmap.org/")
# page = BeautifulSoup(res.text, "html.parser")
#
# links = page.find_all("a")
# for link in links:
#    print(link.get("href"))

res2 = requests.get("https://hackeru.com")
page2 = BeautifulSoup(res2.text, "html.parser")

jsLinks = page2.find_all("script")
for link in jsLinks:
    link2 = link.get("src")
    if link2 != None:
        if link2.endswith("js"):
            print(link2)

