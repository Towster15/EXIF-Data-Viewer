from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QTableWidget,
    QGridLayout,
    QPushButton,
)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.displayed_image = None

        self.setWindowTitle("Image EXIF Viewer")

        self.image_group = QGroupBox(title="Image")
        self.select_image_button = QPushButton("Select an image")
        self.image_label = QLabel("No Image Loaded!")
        self.image_label.setScaledContents(True)
        self.image_group.layout = QVBoxLayout(self.image_group)
        self.image_group.layout.addWidget(self.select_image_button)
        self.image_group.layout.addWidget(self.image_label)

        self.core_info_group = QGroupBox(title="Core Info")
        self.core_info_table = QTableWidget()
        self.core_info_group.layout = QVBoxLayout(self.core_info_group)
        self.core_info_group.layout.addWidget(self.core_info_table)

        self.os_info_group = QGroupBox(title="OS Information")
        self.os_info_table = QTableWidget()
        self.os_info_group.layout = QVBoxLayout(self.os_info_group)
        self.os_info_group.layout.addWidget(self.os_info_table)

        self.all_exif_group = QGroupBox(title="All EXIF Data")
        self.all_exif_table = QTableWidget()
        self.all_exif_group.layout = QVBoxLayout(self.all_exif_group)
        self.all_exif_group.layout.addWidget(self.all_exif_table)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.image_group, 0, 0, 2, 1)
        self.layout.addWidget(self.core_info_group, 0, 1)
        self.layout.addWidget(self.os_info_group, 1, 1)
        self.layout.addWidget(self.all_exif_group, 0, 2, 2, 1)


if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec()
