## Bac Area Update Plugin

### Giới thiệu
**Bac Area Update Plugin** là một công cụ hỗ trợ tính toán diện tích cho các đối tượng trong một lớp bản đồ của QGIS. Plugin này cho phép người dùng dễ dàng thêm trường diện tích (theo đơn vị mét vuông và hecta) vào bảng thuộc tính của lớp và tự động điền diện tích của mỗi đối tượng dựa trên hình học của chúng.

Plugin này đặc biệt hữu ích cho các nhà phân tích GIS và các chuyên gia môi trường, quy hoạch đô thị, hoặc quản lý đất đai, những người cần thực hiện các phép tính diện tích nhanh chóng và chính xác.

---

### Tính năng chính
- **Thêm trường diện tích**: Tự động tạo các trường diện tích trong bảng thuộc tính, với đơn vị tính là mét vuông và hecta.
- **Cập nhật diện tích theo yêu cầu**: Cho phép người dùng chọn tính diện tích cho tất cả các đối tượng hoặc chỉ các đối tượng được chọn.
- **Hiển thị tiến trình và tùy chọn hủy**: Cung cấp thanh tiến trình hiển thị % hoàn thành và nút "Cancel" để hủy tiến trình bất cứ lúc nào.

---

### Hướng dẫn cài đặt
1. **Di chuyển plugin vào thư mục plugins của QGIS**:
   - Tải plugin về máy tính và di chuyển thư mục `Bac_updatearea` vào thư mục plugins của QGIS:
     - **Windows**: `C:\Users\<TênNgườiDùng>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Bac_updatearea`
     - **macOS**: `/Users/<TênNgườiDùng>/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/Bac_updatearea`
     - **Linux**: `/home/<TênNgườiDùng>/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Bac_updatearea`

2. **Khởi động lại QGIS** để QGIS nhận diện plugin mới.

3. **Kích hoạt plugin**:
   - Vào `Plugins > Manage and Install Plugins…`.
   - Tìm "Bac Area Update Plugin" trong danh sách và chọn `Install` hoặc `Enable`.

---

### Hướng dẫn sử dụng

1. **Mở lớp bản đồ cần cập nhật diện tích**:
   - Chọn lớp bản đồ (layer) mà bạn muốn tính toán diện tích cho các đối tượng trong đó.

2. **Chạy Bac Area Update Plugin**:
   - Sau khi plugin đã được kích hoạt, biểu tượng của plugin sẽ xuất hiện trên thanh công cụ của QGIS hoặc trong menu plugin.
   - Nhấp vào biểu tượng `Update Area Fields` để khởi động plugin.

3. **Sử dụng hộp thoại nhập liệu**:
   - Một hộp thoại mới sẽ mở ra với các mục sau:
     - **Area (m²) Field**: Nhập tên của trường sẽ lưu diện tích theo mét vuông (m²). Bạn có thể dùng mặc định là `area_sq`.
     - **Area (ha) Field**: Nhập tên của trường sẽ lưu diện tích theo hecta (ha). Bạn có thể dùng mặc định là `area_ha`.
     - **Selected Features Only**: Chọn tùy chọn này nếu bạn chỉ muốn tính diện tích cho các đối tượng đã chọn trong lớp.

4. **Bắt đầu tính toán diện tích**:
   - Nhấn `OK` để bắt đầu tiến trình cập nhật diện tích.
   - **Thanh tiến trình** sẽ hiển thị % hoàn thành và có nút `Cancel` để hủy tiến trình nếu cần.

5. **Hoàn tất**:
   - Sau khi hoàn tất, một thông báo sẽ xuất hiện cho biết số lượng đối tượng đã được cập nhật diện tích.
   - Nếu bạn nhấn `Cancel` trong quá trình tính toán, tiến trình sẽ dừng ngay lập tức và các thay đổi sẽ được hoàn tác.

---

### Lưu ý
- Plugin yêu cầu lớp bản đồ phải ở chế độ chỉnh sửa (`editable`) để có thể cập nhật dữ liệu.
- Đảm bảo chọn tên trường khác biệt cho diện tích để tránh xung đột với các trường đã tồn tại.
