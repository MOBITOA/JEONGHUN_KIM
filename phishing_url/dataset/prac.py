import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요:  ")
url = (f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.select(".news_tit")
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title , url)