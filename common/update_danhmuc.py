from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(id, ten_danh_muc=None, mo_ta=None, trang_thai=None):
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối DB")
        return False

    try:
        fields = []
        values = []

        if ten_danh_muc is not None:
            fields.append("ten_danh_muc = %s")
            values.append(ten_danh_muc)

        if mo_ta is not None:
            fields.append("mo_ta = %s")
            values.append(mo_ta)

        if trang_thai is not None:
            fields.append("trang_thai = %s")
            values.append(trang_thai)

        if not fields:
            print("⚠ Không có dữ liệu cần update!")
            return False

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE id = %s"
        values.append(id)

        cursor = conn.cursor()
        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Cập nhật danh mục ID={id} thành công")
            return True
        else:
            print(f"⚠ ID={id} không tồn tại")
            return False

    except Error as e:
        print("❌ Lỗi update:", e)
        return False
    finally:
        cursor.close()
        conn.close()
