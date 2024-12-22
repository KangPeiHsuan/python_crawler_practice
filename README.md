## 爬蟲練習
參考影片：[【 Python 爬蟲 】2 小時初學者課程 ：一次學會 PTT 爬蟲、Hahow 爬蟲、Yahoo 電影爬蟲！](https://youtu.be/1PHp1prsxIM?si=qqmTt5agW67bNMbF)  
實作筆記：[ [NOTE] Python 爬蟲練習](https://hackmd.io/@kangpei/BJpAnUFNJe)

### 下載後指令
- 安裝套件：`$ pip install -r requirements.txt`  
- 執行爬蟲程式：  
    - `$ python ptt_crawler_koreadrama.py`  
    - `$ python hahow_crawler_courses.py`

### PTT 爬蟲 - 韓劇版(KoreaDrama)
#### URL：https://www.ptt.cc/bbs/KoreaDrama/index.html
#### 使用套件：
- Requests 套件：用來發送 HTTP 請求，適用於靜態網頁
- BeautifulSoup 套件：用來解析 HTML 和 XML 文件
- JSON 套件：用來處理 JSON 資料
- Pandas 套件：用來處理和分析資料
- Openpyxl 套件：用來處理 Excel 檔案
- Selenium 套件：用來模擬瀏覽器行為，適用於動態網頁
- Webdriver_manager 套件：Selenium 相關套件，用來管理瀏覽器驅動 ChromeDriver，會自動匹配瀏覽器版本

#### 實作步驟：
1. 發送 HTTP 請求，取得網頁原始碼
2. 解析網頁原始碼，提取資料(標題、人氣、日期)，並儲存到 data_list 中
3. 將 data_list 儲存成 JSON 檔案
4. 將 data_list 儲存成 Excel 檔案

### AJAX 爬蟲 - Hahow 已開課課程
#### URL：https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING
#### 使用套件：
- Requests 套件：用來發送 HTTP 請求
- Pandas 套件：用來處理和分析資料
- Openpyxl 套件：用來處理 Excel 檔案

#### 實作步驟：
1. 找到請求的 API URL，發送 HTTP 請求
2. 解析 JSON 資料，提取資料(課程名稱、平均評分、價格、購課人數)，並儲存到 course_list 中
3. 將 course_list 儲存成 Excel 檔案

### 多頁式爬蟲 - 威秀電影(熱售中)
> 註：威秀頁面可以不用使用到 Selenium，純粹是練習使用，主要是多頁式爬蟲的用法
#### URL：https://www.vscinemas.com.tw/vsweb/film/index.aspx
#### 使用套件：
- BeautifulSoup 套件：用來解析 HTML 和 XML 文件
- Selenium 套件：用來模擬瀏覽器行為，適用於動態網頁
- Webdriver_manager 套件：Selenium 相關套件，用來管理瀏覽器驅動 ChromeDriver，會自動匹配瀏覽器版本

#### 實作步驟：
1. 確認為多頁式分頁，使用 for 迴圈，取得每個頁面的網頁原始碼
2. 使用 BeautifulSoup 解析網頁原始碼，提取資料(電影名稱、上映日期)
