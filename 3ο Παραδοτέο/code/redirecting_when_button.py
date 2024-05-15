import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

class ContentWidget(QWidget):
    def __init__(self, content):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel(content, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ΚΑΛΩΣ ΗΡΘΕΣ "ΟΝΟΜΑ ΧΡΗΣΤΗ"')

        # Main layout
        self.main_layout = QHBoxLayout()

        # Add the menu bar to the main layout
        self.menu_widget = self.create_menu()
        self.main_layout.addWidget(self.menu_widget)

        # Main content area
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()

        # Greeting message
        self.greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        self.greeting_label.setAlignment(Qt.AlignCenter)
        self.greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.content_layout.addWidget(self.greeting_label)

        # Two boxes at the bottom center
        self.bottom_layout = QHBoxLayout()
        self.box1 = QLineEdit(self)
        self.box2 = QTextEdit(self)
        self.box1.setMinimumSize(1500, 800)
        self.box2.setMinimumSize(1500, 800)
        self.bottom_layout.addWidget(self.box1)
        self.bottom_layout.addWidget(self.box2)
        self.content_layout.addLayout(self.bottom_layout)

        self.content_area.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_area)

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

        # Set the fixed size of the window
        self.setFixedSize(1200, 600)

    def create_menu(self):
        menu_layout = QVBoxLayout()
        self.add_menu_button(menu_layout, 'ΑΡΧΙΚΗ', 'Home Page', 'This is the home page content.')
        self.add_menu_button(menu_layout, 'CHAT', 'Chat Page', 'This is the chat page content.')
        self.add_menu_button(menu_layout, 'ΒΟΗΘΕΙΑ', 'Help Page', 'This is the help page content.')
        self.add_menu_button(menu_layout, 'ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ', 'Medical Profile Page', 'This is the medical profile page content.')
        self.add_menu_button(menu_layout, 'ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ', 'Health Wallet Page', 'This is the health wallet page content.')
        self.add_menu_button(menu_layout, 'ΕΠΙΚΟΙΝΩΝΙΑ', 'Contact Page', 'This is the contact page content.')

        exit_button = QPushButton('ΕΞΟΔΟΣ')
        exit_button.clicked.connect(self.close_application)
        menu_layout.addWidget(exit_button)
        menu_layout.addStretch()  # Add stretch to push menu items to the top

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)
        menu_widget.setStyleSheet("background-color: #CDEAC0;")
        menu_widget.setMinimumWidth(self.frameGeometry().width() // 5)
        return menu_widget

    def add_menu_button(self, menu_layout, text, window_title, window_content):
        button = QPushButton(text, self)
        if text == 'ΑΡΧΙΚΗ':
            button.clicked.connect(self.show_home_page)
        else:
            button.clicked.connect(lambda: self.show_content(window_title, window_content))
        menu_layout.addWidget(button)

    def show_home_page(self):
        # Clear the current content
        self.content_area.setParent(None)

        # Recreate the main content area
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()

        self.greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        self.greeting_label.setAlignment(Qt.AlignCenter)
        self.greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.content_layout.addWidget(self.greeting_label)

        self.bottom_layout = QHBoxLayout()
        self.box1 = QLineEdit(self)
        self.box2 = QTextEdit(self)
        self.box1.setMinimumSize(200, 50)
        self.box2.setMinimumSize(200, 50)
        self.bottom_layout.addWidget(self.box1)
        self.bottom_layout.addWidget(self.box2)
        self.content_layout.addLayout(self.bottom_layout)

        self.content_area.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_area)

    def show_content(self, title, content):
        # Clear the current content
        self.content_area.setParent(None)

        # Create new content area
        self.content_area = ContentWidget(content)
        self.main_layout.addWidget(self.content_area)

    def close_application(self):
        QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
