from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QTableWidget,
    QGridLayout,
    QPushButton,
    QMessageBox,
    QFileDialog,
)

from PIL import Image, ImageQt

from displayed_image import DisplayedImage
from exceptions import FileFormatError


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.displayed_image = None

        self.setWindowTitle("Image EXIF Viewer")

        self.image_group = QGroupBox(title="Image")
        self.select_image_button = QPushButton("Select an image")
        self.select_image_button.clicked.connect(self.__load_image)
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

    def __change_image(self, image: Image) -> None:
        pixmap = QPixmap(ImageQt.ImageQt(image))
        self.image_label.setPixmap(pixmap)

    @Slot()
    def __load_image(self) -> None:
        try:
            # TODO: deal with string "" being returned when open dialog cancelled
            self.displayed_image = DisplayedImage(
                QFileDialog.getOpenFileName(
                    self, "Open File", "/home", "Images (*.png *.xpm *.jpg)"
                )[0]
            )
        except FileFormatError:
            QMessageBox.warning(
                self,
                "Image Load Failed",
                "Failed to load the image. Is it a valid image format?",
            )
        else:
            self.__change_image(self.displayed_image.image)
            pass


if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec()
