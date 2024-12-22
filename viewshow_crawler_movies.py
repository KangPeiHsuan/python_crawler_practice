from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 設定 chromedriver 路徑
# service = Service(executable_path='/Users/kangpei/Chromedriver_114.0.5735.90_Mac_Arm64/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(1, 4):
    driver.get(f"https://www.vscinemas.com.tw/vsweb/film/index.aspx?p={i}")
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    movies = soup.find('ul', class_='movieList', recursive=True).find_all('li')
    print(f"---第 {i} 頁---")

    if movies:
        for movie in movies:

            # 電影名稱
            movie_title_element = movie.find('section', class_='infoArea').find('h2').find('a')
            movie_title = movie_title_element.text if movie_title_element else "無此電影名稱"

            # 上映日期
            movie_time_element = movie.find('section', class_='infoArea').find('time')
            movie_time = movie_time_element.text if movie_time_element else "無此電影上映日期"
        
            print(f"電影名稱: {movie_title}, 上映日期: {movie_time}")
    