import json
from datetime import datetime

# Danh sách lưu trữ giao dịch
giao_dich_list = []

# Hàm nhập giao dịch
def nhap_giao_dich():
    while True:
        print("\n--- Nhập Giao Dịch ---")
        loai = input("Nhập loại giao dịch (tien/vang): ").strip().lower()
        if loai not in ["tien", "vang"]:
            print("❌ Loại giao dịch không hợp lệ. Chỉ nhận 'tien' hoặc 'vang'.")
            continue

        ma_gd = input("Mã giao dịch: ").strip()
        ngay = input("Ngày giao dịch (dd/mm/yyyy): ").strip()
        don_gia = float(input("Đơn giá: "))
        so_luong = float(input("Số lượng: "))

        if loai == "tien":
            loai_tien = input("Loại tiền (USD, VND, EUR...): ").strip().upper()
            ty_gia = float(input("Tỷ giá: "))
            giao_dich = {
                "loai": "tien",
                "ma_giao_dich": ma_gd,
                "ngay": ngay,
                "don_gia": don_gia,
                "so_luong": so_luong,
                "loai_tien": loai_tien,
                "ty_gia": ty_gia
            }
        else:  # giao dịch vàng
            loai_vang = input("Loại vàng (SJC, PNJ...): ").strip().upper()
            giao_dich = {
                "loai": "vang",
                "ma_giao_dich": ma_gd,
                "ngay": ngay,
                "don_gia": don_gia,
                "so_luong": so_luong,
                "loai_vang": loai_vang
            }

        giao_dich_list.append(giao_dich)

        # Hỏi người dùng có muốn tiếp tục nhập
        tiep_tuc = input("Bạn có muốn nhập thêm giao dịch không? (y/n): ").strip().lower()
        if tiep_tuc != "y":
            break

# Ghi vào JSON
def ghi_vao_json(data):
    # Lấy thời gian hiện tại để đặt tên file
    now = datetime.now()
    ten_file = now.strftime("%Y-%m-%d-%H-%M-%S") + ".json"

    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Đã ghi dữ liệu vào tập tin: {ten_file}")

# Chạy chương trình
nhap_giao_dich()

# Hỏi người dùng có muốn ghi file không
while True:
    ghi_file = input("Bạn có muốn ghi giao dịch vào tập tin JSON không? (1: Có / 0: Không): ").strip()
    if ghi_file == "1":
        ghi_vao_json(giao_dich_list)
        break
    elif ghi_file == "0":
        print("❌ Bạn đã chọn không ghi dữ liệu.")
        break
    else:
        print("❗ Vui lòng nhập 1 hoặc 0.")
