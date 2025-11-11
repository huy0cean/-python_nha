from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def delete_danhmuc(id):
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối DB")
        return False

    try:
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Xoá danh mục ID={id} thành công")
            return True
        else:
            print(f"⚠ Không tìm thấy danh mục ID={id}")
            return False

    except Error as e:
        print("❌ Lỗi delete:", e)
        return False

    finally:
        cursor.close()
        conn.close()
