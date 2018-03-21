import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html"  # PTT NBA
response = requests.get(url)  # get為抓網頁
html_doc = response.text  # text屬性為html檔
soup = BeautifulSoup(html_doc, "lxml")  # 指定lxml為解析器
print(soup.title.string)  # title的內容
print(soup.a)  # 抓標籤<a></a>
print(soup.a.string)  # 抓標籤內容
# 檢查一下類別屬性
print(type(soup))  # 轉換成bs4物件
print(type(soup.a))  # Tag 標籤
print(type(soup.a.string))  # NavigableString 標籤中的內容

print(soup.find("div", class_="r-ent").a.string)  # 加入參數class_=指定CSS類別
posts = soup.find_all("div", class_="r-ent")  # 試著全抓下來
print(type(posts))  # ResultSet

aut_ids = []  # 建立一個空list，來裝作者id
po_dates = []  # 放發文日期
po_titles = []  # 放文章標題
recommends = []  # 放推文數

# append整包加入最後一格，extend打開依序加入最後
for post in posts:
	aut_ids.append(post.find("div", class_="author").string)
	po_dates.append(post.find("div", class_="date").string)
	try:
		po_titles.append(post.find("a").string)
	except:
		po_titles.append(np.nan)  # 考慮被刪除的文章
# 推文數的class類別不一樣
recommendations = soup.find_all("div", class_="nrec")
for recommendation in recommendations:
	try:
		recommends.append(int(recommendation.find("span").string))
	except:
		recommends.append(np.nan)

# 將抓下來的資料製成表格
pttnba_dict = {"title": po_titles,
				"date": po_dates,
				"author": aut_ids,
				"recommends": recommends
				}
pttnba_df = pd.DataFrame(pttnba_dict)
print(pttnba_df)
