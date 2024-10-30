from PyQt5.QtGui import QIcon
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QAction, QDialog, QMessageBox, QProgressDialog, QApplication
from qgis.PyQt.QtCore import QVariant, Qt
from qgis.core import QgsField
from qgis.utils import iface

class AreaUpdateDialog(QDialog):
    def __init__(self, parent=None):
        super(AreaUpdateDialog, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'AreaUpdateDialog.ui')
        uic.loadUi(ui_path, self)
        
        # Kết nối nút OK và nút "Mặc định"
        self.buttonBox.accepted.connect(self.accept)
        self.btnDefault.clicked.connect(self.set_default_values)

    def set_default_values(self):
        # Gán giá trị mặc định cho các ô nhập diện tích
        self.lineEdit_area_sq.setText("area_sq")
        self.lineEdit_area_ha.setText("area_ha")

    def get_field_names(self):
        # Lấy tên trường diện tích và trạng thái checkbox
        area_sq_field = self.lineEdit_area_sq.text()
        area_ha_field = self.lineEdit_area_ha.text()
        selected_features = self.checkBox_selected_features.isChecked()
        return area_sq_field, area_ha_field, selected_features

class ProgressDialog(QDialog):
    def __init__(self, total_steps, parent=None):
        super(ProgressDialog, self).__init__(parent)
        
        # Tải file giao diện cho hộp thoại tiến độ
        ui_path = os.path.join(os.path.dirname(__file__), 'ProgressDialog.ui')
        uic.loadUi(ui_path, self)

        # Thiết lập hộp thoại tiến độ
        self.setWindowTitle("Processing...")
        self.setWindowModality(Qt.WindowModal)
        
        # Thiết lập giá trị ban đầu cho progress bar và cờ hủy
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(total_steps)
        self.canceled = False
        
        # Kết nối nút Cancel
        self.btnCancel.clicked.connect(self.mark_canceled)

    def mark_canceled(self):
        # Đánh dấu tiến trình là đã hủy
        self.canceled = True

    def is_canceled(self):
        # Kiểm tra xem người dùng có hủy tiến trình không
        return self.canceled

    def update_progress(self, step):
        # Cập nhật thanh tiến độ
        self.progressBar.setValue(step)
        QApplication.processEvents()  # Cập nhật giao diện người dùng ngay lập tức

class AreaUpdatePlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
         print("Initializing GUI")
        # Đường dẫn đến icon của plugin
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Update Area Fields", self.iface.mainWindow())
        
        # Kết nối action với phương thức run
        self.action.triggered.connect(self.run)
        
        # Thêm plugin vào toolbar và menu
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Bac Update Area", self.action)

    def unload(self):
        # Xóa plugin khỏi toolbar và menu
        self.iface.removePluginMenu("Bac Update Area", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
   print("Plugin activated")
   if not self.dialog:
            self.dialog = AreaUpdateDialog()
        
 
