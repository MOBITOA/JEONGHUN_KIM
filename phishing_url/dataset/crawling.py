# # 라이브러리 준비하기
# import csv
# import requests
# from bs4 import BeautifulSoup
# import cloudscraper

# cookies = {'cf_clearance' : ' PHPSESSID=volt1s7neq33apv1mjrjcf65bumjoung'}
# header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# url ="https://www.phishtank.com/phish_detail.php?phish_id=8422170"
# response = requests.get(url, headers=header, cookies = cookies)

# html = response.text
# print(html)
# soup = BeautifulSoup(html, "html.parser")

# words = soup.select_one("h1")
# print(words)
# for word in words:
#     print(word.text)

# ---------------------------------------------------------------------
# v2

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# cookie = {'PHPSESSID':'volt1s7neq33apv1mjrjcf65bumjoung'}
# header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# # Chrome 드라이버 서비스 생성
# driver_service = webdriver.chrome.service.Service('C:\chromedriver-win64/chromedriver.exe')

# # Chrome 옵션 설정
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")

# # Chrome 드라이버 생성
# driver = webdriver.Chrome(service=driver_service, options=chrome_options)
# url = "https://www.phishtank.com/phish_search.php"
# driver.get(url)

# time.sleep(7)


# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# # 원하는 요소를 추출합니다
# words = soup.select("td:nth-child(2)")
# for word in words:
#     print(word.text)

# # 드라이버 종료
# driver.quit()

# ---------------------------------------------------------------------
# v3

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time

# # Chrome 드라이버 설정
# service = Service('C:\chromedriver-win64/chromedriver.exe')
# options = Options()
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# # 로그 레벨 변경 (옵션)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

# # 드라이버 초기화
# driver = webdriver.Chrome(service=service, options=options)

# # 웹사이트 접속
# url = "https://www.phishtank.com/phish_search.php"
# driver.get(url)

# # 페이지가 완전히 로드될 때까지 기다림
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td:nth-child(2)")))

# # 페이지 소스 가져오기
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# # 원하는 요소 추출
# words = soup.select("td:nth-child(2)")
# for word in words:
#     print(word.text)

# # 드라이버 종료
# driver.quit()



# https://phpschool.com/gnuboard4/bbs/board.php?bo_table=qna_function&wr_id=444023&sfl=wr_subject%7C%7Cwr_content&stx=curl+fsockopen&sst=wr_hit&sod=desc&sop=or&page=4%29
# https://gist.github.com/yasinkuyu/bb3e1abe15ebdc099201724f4cbd2100 

# -------------------------------------------------------------------

# import cloudscraper
# from bs4 import BeautifulSoup

# scraper = cloudscraper.create_scraper()  # Cloudscraper 인스턴스 생성
# scraper.headers.update({
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# })
# url = "https://www.phishtank.com/phish_search.php"
# info = scraper.get(url)
# print(info.status_code)


# html = scraper.get(url).text  # 웹페이지 가져오기

# soup = BeautifulSoup(html, "html.parser")
# words = soup.select("td:nth-child(2)")  # 셀렉터 검토 필요
# for word in words:
#     print(word.text)


# --------------------------------------------------------

from zenrows import ZenRowsClient

client = ZenRowsClient("e59b15ba65ee8f944947f6f230cfaf4fb734f599")
url = "https://www.phishtank.com/phish_search.php&wait_for=.background-load"  # JavaScript rendering 옵션을 URL에 포함

response = client.get(url)

print(response.text)

# import requests
# response_specific = requests.get("https://api.zenrows.com/v1/?apikey=e59b15ba65ee8f944947f6f230cfaf4fb734f599&url=https%3A%2F%2Fwww.phishtank.com%2Fphish_search.php&js_render=true&wait_for=.content") 
# print(response_specific.text)

# response_specific = requests.get("https://api.zenrows.com/v1/?apikey=e59b15ba65ee8f944947f6f230cfaf4fb734f599&url=https%3A%2F%2Fwww.phishtank.com%2Fphish_detail.php?phish_id=8422170&js_render=true&wait_for=.content") 
# print(response_specific.text)

# ------------------------------------------------------------

# import undetected_chromedriver as uc 
# driver = uc.Chrome() 
# response = driver.get('https://www.phishtank.com/phish_search.php')
# print(response.text)

