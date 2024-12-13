import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.ptt.cc/bbs/KoreaDrama/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

# 取得網頁原始碼
if response.status_code == 200:
    with open("ptt_koreadrama.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("網頁已成功儲存到 ptt_koreadrama.html 檔案中")
else:
    print("網頁爬取失敗")

# 解析網頁原始碼
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="r-ent")

data_list = []

# 提取資料(標題、人氣、日期)，並儲存到 data_list 中
for article in articles:
    
    data = {}
    
    title = article.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "無標題"
    data["標題"] = title
    
    popular = article.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular
    
    date = article.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    
    data_list.append(data)

# 將 data_list 儲存成 JSON 檔案
with open("ptt_koreadrama.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)

print("資料已成功儲存到 ptt_koreadrama_data.json 檔案中")

# 將 data_list 儲存成 Excel 檔案
df = pd.DataFrame(data_list)
df.to_excel("ptt_koreadrama.xlsx", index=False, engine="openpyxl")
print("資料已成功儲存到 ptt_koreadrama.xlsx 檔案中")