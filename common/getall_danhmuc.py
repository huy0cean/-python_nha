from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    """
    Lấy toàn bộ danh mục
    Trả về: list dict
    """
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối DB")
        return []

    try:
        sql = "SELECT id, ten_danh_muc, mo_ta, trang_thai, ngay_tao FROM danhmuc"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)

        rows = cursor.fetchall()
        print(f"✅ Lấy {len(rows)} danh mục thành công")
        return rows

    except Error as e:
        print("❌ Lỗi SELECT:", e)
        return []

    finally:
        cursor.close()
        conn.close()
