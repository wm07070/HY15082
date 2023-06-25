from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Daum 영화 예매 순위 페이지로 이동
# url = 'https://www.naver.com/'
# driver.get(url)
# driver.page_source[1:1000]

# driver.find_element(By.CLASS_NAME, value = 'search_input').send_keys('퀀트 투자 포트폴리오 만들기')
# # 영화 데이터를 저장할 빈 리스트 생성
movies = []
url = 'https://movie.daum.net/ranking/reservation'
driver.get(url)
driver.page_source[1:1000]
elements = driver.find_elements(By.CLASS_NAME, value = 'list_movieranking>li')
for element in elements:
	title= element.find_element(By.CLASS_NAME, value = 'link_txt').text
	rating = element.find_element(By.CLASS_NAME, value = 'txt_grade').text
	r = element.find_elements(By.CLASS_NAME, value = 'txt_num')
	reservationRate = r[0].text
	date =r[1].text
	# date = element.find_element(By.CLASS_NAME, value = 'txt_num').text
	movies.append([title,rating,reservationRate,date])


# print(movies)
df = pd.DataFrame(movies, columns=['제목', '평점', '예매율', '개봉'])
df.index = range(1, len(df) + 1)
print(df)
df.to_csv('moive.csv',sep='\t', index=True)

driver.quit()
