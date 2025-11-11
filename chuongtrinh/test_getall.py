from common.getall_danhmuc import get_all_danhmuc

def test_get_all():
    print("=== LIST DANH MỤC ===")
    data = get_all_danhmuc()
    if len(data) == 0:
        print("⚠ Không có dữ liệu")
    else:
        for row in data:
            print(row)

if __name__ == "__main__":
    test_get_all()
