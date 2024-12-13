import requests
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING"
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    
    data = response.json()
    products = data['data']['courseData']['products']
    
    course_list = []

    # 要爬取的資料(課程名稱/平均評分/價格/購課人數)
    for product in products:
        
        course_data = [
            product['title'],
            product['averageRating'],
            product['price'],
            product['numSoldTickets']
        ]
        course_list.append(course_data)

    df = pd.DataFrame(course_list, columns = ['課程名稱', "評分", "價格", "購課人數"])
    df.to_excel('hahow_courses.xlsx', index=False, engine='openpyxl')
    print("資料已存入 excel 檔案")

else:
    print("未成功爬取頁面")
