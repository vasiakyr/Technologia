import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap

class DrugSearchPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ΚΑΛΩΣ ΗΡΘΕΣ "ΟΝΟΜΑ ΧΡΗΣΤΗ"')

        # Vertical menu bar
        self.menu_layout = QVBoxLayout()
        self.menu_layout.addWidget(QPushButton('ΑΡΧΙΚΗ'))
        self.menu_layout.addWidget(QPushButton('CHAT'))
        self.menu_layout.addWidget(QPushButton('ΒΟΗΘΕΙΑ'))
        self.menu_layout.addWidget(QPushButton('ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ'))
        self.menu_layout.addWidget(QPushButton('ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ'))
        self.menu_layout.addWidget(QPushButton('ΕΠΙΚΟΙΝΩΝΙΑ'))
        self.menu_layout.addWidget(QPushButton('ΕΞΟΔΟΣ'))
        self.menu_layout.addStretch()  # Add stretch to push menu items to the top

        # Create a widget to contain the menu
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        # Set the menu widget's minimum width to cover 1/5 of the window
        menu_width = self.frameGeometry().width() // 5
        self.menu_widget.setMinimumWidth(menu_width)

        # Set background color of menu widget to light green
        self.menu_widget.setStyleSheet("background-color: #CDEAC0;")

        # Content layout
        content_layout = QVBoxLayout()

        # Profile photo
        profile_photo_label = QLabel(self)
        profile_photo_pixmap = QPixmap('profile_photo.png')  # Replace 'profile_photo.png' with the actual file path
        profile_photo_label.setPixmap(profile_photo_pixmap)
        content_layout.addWidget(profile_photo_label)

        # Greeting message
        greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")  # Set font size and weight
        content_layout.addWidget(greeting_label)



        # Two boxes at the bottom center
        bottom_layout = QHBoxLayout()
        box1 = QLineEdit(self)
        box1.setFixedSize(1550, 800)  # Adjust the width and height as needed
        box2 = QTextEdit(self)
        box2.setFixedSize(1550, 800)  # Adjust the width and height as needed
        bottom_layout.addWidget(box1)
        bottom_layout.addWidget(box2)
        content_layout.addLayout(bottom_layout)

        # Combine menu and content layouts using QHBoxLayout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.menu_widget)
        main_layout.addLayout(content_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Set the fixed size of the window
        self.setFixedSize(1200, 600)  # Adjust the width and height as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrugSearchPage()
    window.show()
    sys.exit(app.exec_())
