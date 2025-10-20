# Bài 2.5: Lấy danh sách các phần tử <name> và in ra nội dung
from pydoc import doc

name_elements = doc.getElementsByTagName("name")

print("\n📋 Danh sách các phần tử <name> và nội dung:")
for i, elem in enumerate(name_elements, start=1):
    if elem.firstChild is not None:
        print(f"{i}. {elem.firstChild.data}")
    else:
        print(f"{i}. (Không có nội dung)")