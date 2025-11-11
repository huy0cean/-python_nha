import mysql.connector
from mysql.connector import Error

def connect_mysql(host="localhost", user="root", password="", database="db_ghuy"):
    """
    Kết nối tới MySQL.
    Trả về: đối tượng connection nếu thành công, None nếu thất bại.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return conn
    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
