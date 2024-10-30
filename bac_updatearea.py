from PyQt5.QtGui import QIcon
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QAction, QDialog, QMessageBox, QApplication
from qgis.PyQt.QtCore import QVariant, Qt
from qgis.core import QgsField
from qgis.utils import iface

class AreaUpdateDialog(QDialog):
    def __init__(self, parent=None):
        super(AreaUpdateDialog, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'AreaUpdateDialog.ui')
        uic.loadUi(ui_path, self)
        
        # Cờ hủy tiến trình
        self.canceled = False
        
        # Kết nối các nút với các phương thức
        self.btnUpdate.clicked.connect(self.start_update)
        self.btnStopSave.clicked.connect(self.save_and_close)
        self.btnClose.clicked.connect(self.close_dialog)
        self.btnDefault.clicked.connect(self.set_default_values)


    def set_default_values(self):
        self.lineEdit_area_sq.setText("area_sq")
        self.lineEdit_area_ha.setText("area_ha")

    def get_field_names(self):
        area_sq_field = self.lineEdit_area_sq.text()
        area_ha_field = self.lineEdit_area_ha.text()
        selected_features = self.checkBox_selected_features.isChecked()
        return area_sq_field, area_ha_field, selected_features

    def start_update(self):
        # Đặt lại cờ hủy
        self.canceled = False

        # Lấy thông tin trường từ người dùng
        area_sq_field, area_ha_field, selected_features_only = self.get_field_names()
        
        # Lấy layer hiện tại
        layer = iface.activeLayer()
        if not layer.isEditable():
            layer.startEditing()
        
        # Thêm các trường diện tích nếu chưa có
        if area_sq_field not in [field.name() for field in layer.fields()]:
            layer.dataProvider().addAttributes([QgsField(area_sq_field, QVariant.Double, "double", 10, 2)])
            layer.updateFields()

        if area_ha_field not in [field.name() for field in layer.fields()]:
            layer.dataProvider().addAttributes([QgsField(area_ha_field, QVariant.Double, "double", 10, 2)])
            layer.updateFields()

        # Chuyển đổi các đối tượng đã chọn thành danh sách và thiết lập tiến trình
        selected_features = list(layer.selectedFeatures()) if selected_features_only and layer.selectedFeatureCount() > 0 else list(layer.getFeatures())
        total_features = len(selected_features)
        self.progressBar.setMaximum(total_features)
        
        count = 0
        for i, feature in enumerate(selected_features):
            # Kiểm tra nếu tiến trình bị hủy
            if self.canceled:
                QMessageBox.information(self, "Canceled", "Update was canceled.")
                break

            # Cập nhật diện tích
            feature[area_sq_field] = feature.geometry().area()
            feature[area_ha_field] = feature.geometry().area() / 10000
            layer.updateFeature(feature)
            count += 1

            # Cập nhật thanh tiến trình
            self.progressBar.setValue(i + 1)
            QApplication.processEvents()  # Cập nhật giao diện ngay lập tức

        # Thông báo hoàn tất
        if not self.canceled:
            layer.commitChanges()
            QMessageBox.information(self, "Completed", f"{count} features updated.")
        else:
            layer.rollBack()  # Hủy các thay đổi nếu bị hủy

    def save_and_close(self):
        # Đặt cờ hủy và đóng hộp thoại
        self.canceled = True
        self.close()

    def close_dialog(self):
        # Đóng hộp thoại mà không lưu
        self.close()

class AreaUpdatePlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Update Area Fields", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Bac Area Update Plugin", self.action)

    def unload(self):
        self.iface.removePluginMenu("Bac Area Update Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        if not self.dialog:
            self.dialog = AreaUpdateDialog()
        self.dialog.show()
