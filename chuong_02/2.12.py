import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    print("🔄 Đang tải dữ liệu từ API...")

    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        print(f"✅ Tổng số bài post: {len(posts)}\n")

        for post in posts:
            print(f"userID: {post['userId']}")
            print(f"id: {post['id']}")
            print(f"title: {post['title']}")
            print(f"body: {post['body']}")
            print("-" * 40)
    else:
        print("❌ Lỗi khi tải dữ liệu từ API:", response.status_code)

if __name__ == "__main__":
    main()
