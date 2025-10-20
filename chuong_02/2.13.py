import requests

def main():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    print("🔄 Đang tải dữ liệu từ API...")

    response = requests.get(url)
    if response.status_code == 200:
        comments = response.json()
        print("✅ Danh sách các bài post nổi bật (3 bài đầu):\n")

        # Giới hạn chỉ 3 bài đầu
        for comment in comments[:3]:
            print(f"postId: {comment['postId']}")
            print(f"id: {comment['id']}")
            print(f"name: {comment['name']}")
            print(f"email: {comment['email']}")
            print(f"body: {comment['body']}")
            print("-" * 40)
    else:
        print("❌ Lỗi khi tải dữ liệu từ API:", response.status_code)

if __name__ == "__main__":
    main()
