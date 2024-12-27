from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

import time
import wget
import os
from dotenv import load_dotenv

load_dotenv()

instagram_url = "http://www.instagram.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(instagram_url)

# 等待 name 為 username / password 的標籤出現後再執行，將回傳的標籤賦值給變數 username / password
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

# 先將欄位清空
username.clear()
password.clear()

# 輸入帳號密碼
username.send_keys(os.getenv("insta_username"))
password.send_keys(os.getenv("insta_password"))

# 登入
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
login.click()

# 因為無法使用點擊方式成功搜尋，暫時先使用網址進入搜尋頁面
keyword = input("請輸入要搜尋的關鍵字：")
try:
    driver.get(instagram_url + "explore/search/keyword/?q=%23" + keyword)
    print("成功進入搜尋頁面")
except Exception as e:
    print("失敗")
    print(f"錯誤訊息：{str(e)}")

# 等待頁面完全加載
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script('return document.readyState') == 'complete'
)

time.sleep(5)

# class=_aagv > img
containers = driver.find_elements(By.CLASS_NAME, "_aagv")
imgs = []
for container in containers:
    img = container.find_element(By.TAG_NAME, "img")
    imgs.append(img)
    print("img:", img)

print(f"找到 {len(imgs)} 張圖片")

# 創建資料夾
path = os.path.join(keyword)
os.makedirs(path, exist_ok=True)

# 成功/失敗下載的圖片數量
success_count = 0
fail_count = 0

for index, img in enumerate(imgs, 1):
    try:
        # 取得圖片網址
        img_url = img.get_attribute("src")
        print("img_url:", img_url)
        if not img_url:
            print(f"第 {index} 張圖片沒有 src 屬性")
            fail_count += 1
            continue

        # 建立檔案名稱(加上時間戳記)
        timestamp = time.strftime("%Y%m%d%H%M%S")
        save_as = os.path.join(path, f"{keyword}_{timestamp}_{index}.jpg")

        # 下載圖片
        wget.download(img_url, save_as)
        print(f"成功下載第 {index} 張圖片")
        success_count += 1

        time.sleep(1)
        continue

    except Exception as e:
        print(f"第 {index} 張圖片下載失敗：{str(e)}")
        fail_count += 1
        continue

print(f"成功下載 {success_count} 張圖片，失敗 {fail_count} 張圖片")
print(f"圖片下載路徑：{os.path.abspath(path)}")

driver.quit()
# ------------------------------
# # 點擊出現搜尋視窗
# try:    

#     search_box = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'))
#     )
    
#     # ActionChains 點擊，滑鼠移動到元素上，點擊
#     ActionChains(driver).move_to_element(search_box).click().perform()

#     # 等待搜尋頁面出現，selenium 的 click 方法
#     # search_box.click()
#     # JS 點擊
#     # driver.execute_script("arguments[0].click();", search_box)
    
#     time.sleep(3)
#     print("找到搜尋頁面")
# except Exception as e:
#     print("失敗")
#     print(f"錯誤訊息：{str(e)}")
# ------------------------------

# document.readyState 的值有以下幾種：
    # loading - 正在加載頁面
    # interactive - 頁面已經加載完成，但頁面中的資源（如圖片、腳本等）可能還在加載中
    # complete - 頁面和所有資源都已經加載完成
# try:
#     WebDriverWait(driver, 20).until(
#         lambda d: d.execute_script('return document.readyState') == 'complete'
#     )
#     print("頁面完全加載")
# except TimeoutException:
#     print("頁面加載超時")

# ------------------------------

# # 輸入搜尋關鍵字
# try: 
#     # 等待頁面完全載入
#     WebDriverWait(driver, 20).until(
#         lambda d: d.execute_script('return document.readyState') == 'complete'
#     )
    
#     # 等待搜尋欄位出現
#     search = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="x1lugfcp x1hmx34t x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]'))
#     )
#     search.clear()
#     search.send_keys("ateez")
#     search.send_keys(Keys.ENTER)
#     time.sleep(5)
#     print("成功輸入關鍵字")
# except TimeoutException:
#     print("等待超時")
# except ElementClickInterceptedException:
#     print("元素無法點擊")
# except Exception as e:
#     print("失敗")
#     print(f"錯誤訊息：{str(e)}")

# driver.quit()