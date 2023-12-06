# Aidan Kim
# 10/16/23
 

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QWidget
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from image_info import image_info
from hw3functions import neg, greyscale, sepia, thumbnail

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.image_label = QLabel()
        self.setCentralWidget(self.image_label)  

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

class SelectWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.image_data = image_info
        self.filtered_image_data = []

        self.search_box = QLineEdit()
        self.my_combo_box = QComboBox()
        self.image_id = None  

        self.my_button = QPushButton("Open Image Window")

        self.my_combo_box.addItem("None")
        self.my_combo_box.addItem("Greyscale")
        self.my_combo_box.addItem("Negative")
        self.my_combo_box.addItem("Sepia")
        self.my_combo_box.addItem("Thumbnail")

        vbox = QVBoxLayout()
        vbox.addWidget(self.search_box)
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_button)

        self.setLayout(vbox)

        self.image_window = None  
        self.selected_index = None

        self.my_button.clicked.connect(self.open_image_window)
        self.my_combo_box.activated.connect(self.slot_combo_box_activated)
        self.search_box.textChanged.connect(self.update_ui)

    def update_ui(self):
        search_text = self.search_box.text().lower()
        self.filtered_image_data = [item for item in self.image_data if
                                    search_text in item["title"].lower() or
                                    any(search_text in tag.lower() for tag in item["tags"])]

        if len(self.filtered_image_data) == 1:
            self.image_id = self.filtered_image_data[0].get("id")
        else:
            self.image_id = None

    def open_image_window(self):
        if self.image_id:
            if self.image_window is None:
                self.image_window = ImageWindow()

            image_path = f"{self.image_id}.jpg"
            
            if self.my_combo_box.currentText() == "Greyscale":
                image = greyscale(QPixmap(image_path))
            elif self.my_combo_box.currentText() == "Negative":
                image = neg(QPixmap(image_path))
            elif self.my_combo_box.currentText() == "Sepia":
                image = sepia(QPixmap(image_path))
            elif self.my_combo_box.currentText() == "Thumbnail":
                image = thumbnail(QPixmap(image_path))
            else:
                image = QPixmap(image_path)

            self.image_window.display_image(image)
            self.image_window.show()
        else:
            print("No image selected")


    @Slot(int)
    def slot_combo_box_activated(self, index):
        self.selected_index = index

if __name__ == "__main__":
    app = QApplication([])
    my_win = SelectWindow()
    my_win.show()
    app.exec()
