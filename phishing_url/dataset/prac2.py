import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}

url = ("https://www.coupang.com/np/search?component=&q=%EB%A7%A5%EB%AF%B8%EB%8B%88&channel=user")
response = requests.get(url, headers = header)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.select("#\37 122226122 > a > dl > dd > div > div.name")
print(links)
# for link in links:
#     title = link.text
#     print(title)