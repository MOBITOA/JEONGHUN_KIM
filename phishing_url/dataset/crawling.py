# # 라이브러리 준비하기
# import csv
# import requests
# from bs4 import BeautifulSoup
# import cloudscraper

# header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# url ="https://www.phishtank.com/phish_archive.php"
# response = requests.get(url, headers=header)

# html = response.text
# soup = BeautifulSoup(html, "html.parser")

# words = soup.select_one("h1")
# print(words)
# for word in words:
#     print(word.text)


from selenium import webdriver
from bs4 import BeautifulSoup
import time

cookie = {'PHPSESSID':'volt1s7neq33apv1mjrjcf65bumjoung'}
header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# Chrome 드라이버 서비스 생성
driver_service = webdriver.chrome.service.Service('C:\chromedriver-win64/chromedriver.exe')

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")

# Chrome 드라이버 생성
driver = webdriver.Chrome(service=driver_service, options=chrome_options)
url = "https://www.phishtank.com/phish_search.php"
driver.get(url)

time.sleep(7)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 원하는 요소를 추출합니다
words = soup.select("td:nth-child(2)")
for word in words:
    print(word.text)

# 드라이버 종료
driver.quit()

