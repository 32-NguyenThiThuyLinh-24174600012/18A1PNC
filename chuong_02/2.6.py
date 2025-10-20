import requests
from xml.dom import minidom
import csv

# Bước 1: Tải RSS feed từ URL
rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
rss_file = "rss_feed.xml"

print("🔄 Đang tải RSS feed...")
response = requests.get(rss_url)

if response.status_code == 200:
    with open(rss_file, "w", encoding='utf-8') as file:
        file.write(response.text)
    print("✅ RSS feed đã được lưu vào", rss_file)
else:
    print("❌ Không thể tải RSS feed. Mã lỗi:", response.status_code)
    exit()

# Bước 2: Phân tích file XML và trích xuất tin tức
print("🔍 Đang phân tích file XML...")
doc = minidom.parse(rss_file)
items = doc.getElementsByTagName("item")

news_list = []

for item in items:
    title = item.getElementsByTagName("title")[0].firstChild.data if item.getElementsByTagName("title")[0].firstChild else ""
    link = item.getElementsByTagName("link")[0].firstChild.data if item.getElementsByTagName("link")[0].firstChild else ""
    pubDate = item.getElementsByTagName("pubDate")[0].firstChild.data if item.getElementsByTagName("pubDate")[0].firstChild else ""
    description = item.getElementsByTagName("description")[0].firstChild.data if item.getElementsByTagName("description")[0].firstChild else ""

    news = {
        "title": title,
        "link": link,
        "pubDate": pubDate,
        "description": description
    }

    news_list.append(news)

print(f"✅ Đã trích xuất {len(news_list)} mục tin tức.")

# Bước 3: Ghi dữ liệu ra file CSV
csv_file = "news_output.csv"
print("💾 Đang ghi dữ liệu vào file CSV...")

with open(csv_file, mode="w", encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link", "pubDate", "description"])
    writer.writeheader()
    for news in news_list:
        writer.writerow(news)

print(f"🎉 Hoàn thành! Tin tức đã được lưu vào '{csv_file}'")
