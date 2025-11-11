import tkinter as tk
from tkinter import ttk, messagebox
from common.insert_danhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.getall_danhmuc import get_all_danhmuc


class DanhMucUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Danh Mục")

        # Frame form
        frm = tk.Frame(self.root)
        frm.pack(pady=10)

        tk.Label(frm, text="ID:").grid(row=0, column=0)
        self.txt_id = tk.Entry(frm, width=25)
        self.txt_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frm, text="Tên danh mục:").grid(row=1, column=0)
        self.txt_ten = tk.Entry(frm, width=25)
        self.txt_ten.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frm, text="Mô tả:").grid(row=2, column=0)
        self.txt_mo_ta = tk.Entry(frm, width=25)
        self.txt_mo_ta.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frm, text="Trạng thái:").grid(row=3, column=0)
        self.txt_trangthai = tk.Entry(frm, width=25)
        self.txt_trangthai.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Thêm", width=12, command=self.them).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Sửa", width=12, command=self.sua).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Xóa", width=12, command=self.xoa).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Làm mới", width=12, command=self.hienthi).grid(row=0, column=3, padx=5)

        # Table
        cols = ("id", "ten", "mo_ta", "trang_thai", "ngay_tao")
        self.table = ttk.Treeview(self.root, columns=cols, show="headings", height=12)

        for c in cols:
            self.table.heading(c, text=c)

        self.table.pack(pady=10)
        self.table.bind("<ButtonRelease-1>", self.on_select)

        self.hienthi()

    # Load table
    def hienthi(self):
        for item in self.table.get_children():
            self.table.delete(item)
        data = get_all_danhmuc()
        for row in data:
            self.table.insert("", "end", values=(
                row["id"], row["ten_danh_muc"], row["mo_ta"], row["trang_thai"], row["ngay_tao"]
            ))

    # Select row
    def on_select(self, event):
        selected = self.table.focus()
        if not selected:
            return
        values = self.table.item(selected, "values")
        self.txt_id.delete(0, tk.END)
        self.txt_ten.delete(0, tk.END)
        self.txt_mo_ta.delete(0, tk.END)
        self.txt_trangthai.delete(0, tk.END)

        self.txt_id.insert(0, values[0])
        self.txt_ten.insert(0, values[1])
        self.txt_mo_ta.insert(0, values[2])
        self.txt_trangthai.insert(0, values[3])

    # Add
    def them(self):
        ten = self.txt_ten.get().strip()
        mo_ta = self.txt_mo_ta.get().strip() or None
        trang_thai = self.txt_trangthai.get().strip()
        trang_thai = int(trang_thai) if trang_thai else 1

        new_id = insert_danhmuc(ten, mo_ta, trang_thai)
        if new_id:
            messagebox.showinfo("Thông báo", "Thêm thành công!")
            self.hienthi()
        else:
            messagebox.showerror("Lỗi", "Không thêm được")

    # Update
    def sua(self):
        try:
            id_val = int(self.txt_id.get())
        except:
            messagebox.showerror("Lỗi", "ID không hợp lệ")
            return

        ten = self.txt_ten.get().strip() or None
        mo_ta = self.txt_mo_ta.get().strip() or None
        trang_thai = self.txt_trangthai.get().strip()
        trang_thai = int(trang_thai) if trang_thai else None

        ok = update_danhmuc(id_val, ten, mo_ta, trang_thai)
        if ok:
            messagebox.showinfo("Thông báo", "Cập nhật thành công!")
            self.hienthi()
        else:
            messagebox.showerror("Lỗi", "Không cập nhật được")

    # Delete
    def xoa(self):
        try:
            id_val = int(self.txt_id.get())
        except:
            messagebox.showerror("Lỗi", "ID không hợp lệ")
            return

        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xoá?"):
            ok = delete_danhmuc(id_val)
            if ok:
                messagebox.showinfo("Thông báo", "Xoá thành công!")
                self.hienthi()
            else:
                messagebox.showerror("Lỗi", "Không xoá được")


if __name__ == "__main__":
    root = tk.Tk()
    app = DanhMucUI(root)
    root.mainloop()
