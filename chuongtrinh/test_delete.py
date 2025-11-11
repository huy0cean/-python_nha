from common.delete_danhmuc import delete_danhmuc

def test_delete():
    print("=== TEST DELETE DANH MỤC ===")

    id = int(input("Nhập ID cần xoá: "))
    ok = delete_danhmuc(id)

    print("✅ Kết quả:", ok)


if __name__ == "__main__":
    test_delete()
