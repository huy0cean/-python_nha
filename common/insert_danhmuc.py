from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def insert_danhmuc(ten_danh_muc, mo_ta=None, trang_thai=1):
    """
    Thêm 1 danh mục vào bảng danhmuc.
    Trả về: ID mới tạo hoặc None nếu lỗi.
    """
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối DB")
        return None

    try:
        sql = """
            INSERT INTO danhmuc (ten_danh_muc, mo_ta, trang_thai)
            VALUES (%s, %s, %s)
        """
        cursor = conn.cursor()
        cursor.execute(sql, (ten_danh_muc, mo_ta, trang_thai))
        conn.commit()

        new_id = cursor.lastrowid
        print(f"✅ Thêm danh mục thành công! ID = {new_id}")
        return new_id

    except Error as e:
        print("❌ Lỗi insert:", e)
        return None

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
