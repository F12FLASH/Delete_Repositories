# Delete Repositories

## 📌 Mô tả
Script Python này giúp bạn xóa hàng loạt repository trên GitHub một cách tự động thông qua GitHub API.

## 🛠️ Yêu cầu hệ thống
- Python 3.6+
- Thư viện `requests` (cài đặt bằng `pip install requests`)

## 🔐 Chuẩn bị GitHub Token
1. Đăng nhập GitHub và truy cập [Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Tạo token mới với các quyền:
   - `repo` (để xóa repositories cá nhân)
   - `admin:org` (nếu cần xóa repositories trong tổ chức)

## 🚀 Cách sử dụng

### 1. Tải script
Lưu mã nguồn vào file `Delete_Repositories.py`

### 2. Chạy script
```bash
python Delete_Repositories.py
```

### 3. Nhập thông tin
- Nhập username GitHub của bạn
- Nhập Personal Access Token (nội dung sẽ được ẩn)

### 4. Chọn repositories để xóa
Script sẽ hiển thị danh sách repositories. Bạn có thể:
- Nhập số thứ tự (vd: `1`)
- Nhập tên repository (vd: `my-repo`)
- Nhập nhiều repository cách nhau bằng dấu phẩy (vd: `1,3,my-repo`)
- Nhập `all` để chọn tất cả

### 5. Xác nhận
Nhập `y` để xác nhận xóa hoặc `n` để hủy

## ⚠️ Lưu ý quan trọng
❗ Hành động xóa là VĨNH VIỄN và không thể hoàn tác  
❗ Đảm bảo bạn đã sao lưu dữ liệu quan trọng  
❗ Token cần có đủ quyền truy cập  

## 🐛 Xử lý lỗi
| Mã lỗi | Nguyên nhân | Cách khắc phục |
|--------|------------|----------------|
| 401 | Token không hợp lệ | Kiểm tra lại token |
| 403 | Thiếu quyền truy cập | Cấp thêm quyền cho token |
| 404 | Repository không tồn tại | Kiểm tra lại tên repository |

## 📜 Giấy phép
MIT License - Sử dụng tự do

---

📌 **Lưu ý**: Luôn kiểm tra kỹ danh sách repository trước khi xóa!