from common.update_danhmuc import update_danhmuc

def test_update():
    print("=== TEST UPDATE DANH MỤC ===")

    id = int(input("Nhập ID cần update: "))

    ten = input("Tên danh mục mới (Enter bỏ qua): ")
    mo_ta = input("Mô tả mới (Enter bỏ qua): ")
    trang_thai = input("Trạng thái mới (1/0, Enter bỏ qua): ")

    ten = ten if ten.strip() != "" else None
    mo_ta = mo_ta if mo_ta.strip() != "" else None
    trang_thai = int(trang_thai) if trang_thai.strip() != "" else None

    ok = update_danhmuc(id, ten, mo_ta, trang_thai)
    print("✅ Kết quả:", ok)


if __name__ == "__main__":
    test_update()
