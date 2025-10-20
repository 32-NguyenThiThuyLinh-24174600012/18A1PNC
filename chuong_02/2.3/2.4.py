from xml.dom import minidom

# Bài 2.4: Load và phân tích file XML
try:
    doc = minidom.parse("sample.xml")  # Đảm bảo file sample.xml ở cùng thư mục
except FileNotFoundError:
    print("❌ Không tìm thấy file sample.xml.")
    exit()

print("✅ Đã phân tích file XML thành công.")

