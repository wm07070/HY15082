from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import time

# 웹 드라이버 경로 설정
driver_path = '웹 드라이버 경로를 입력하세요'

# 웹 드라이버 시작
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 유튜브 영상 페이지로 이동
video_url = 'https://www.youtube.com/watch?v=CIeJ5mpqyDY'
driver.get(video_url)

# 댓글창까지 스크롤 다운
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 댓글 추출
comments = []
comment_elements = driver.find_elements(By.CSS_SELECTOR,value ='#content-text')
for comment_element in comment_elements:
    comment = comment_element.text
    comments.append(comment)

# 웹 드라이버 종료
driver.quit()

# 댓글 출력
for comment in comments:
    print(comment)
