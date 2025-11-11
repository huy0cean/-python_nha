from common.insert_danhmuc import insert_danhmuc

def test_insert():
    print("=== TEST INSERT DANH MỤC ===")

    ten = input("Nhập tên danh mục: ")
    mo_ta = input("Nhập mô tả (Enter bỏ qua): ")
    trang_thai = input("Nhập trạng thái (1/0, Enter = 1): ")

    trang_thai = int(trang_thai) if trang_thai.strip() != "" else 1
    mo_ta = mo_ta if mo_ta.strip() != "" else None

    new_id = insert_danhmuc(ten, mo_ta, trang_thai)
    print("✅ New ID:", new_id)


if __name__ == "__main__":
    test_insert()
