import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QTabWidget, QMenuBar
from PyQt5.QtGui import QIcon
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

        # Set the application icon
        self.setWindowIcon(QIcon('app_icon.png'))  # Make sure app_icon.png is in the same directory

        # Set the size of the window
        self.setFixedSize(1200, 600)

        # Create the main layout
        self.main_layout = QHBoxLayout()

        # Add the menu widget to the main layout
        self.menu_widget = self.create_menu()
        self.main_layout.addWidget(self.menu_widget)

        # Create right side with tabs
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.tab1 = self.create_home_page()
        self.tab2 = ContentWidget("This is the chat page content.")
        self.tab3 = ContentWidget("This is the help page content.")
        self.tab4 = ContentWidget("This is the medical profile page content.")
        self.tab5 = ContentWidget("This is the health wallet page content.")
        self.tab6 = ContentWidget("This is the contact page content.")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}''')

        self.main_layout.addWidget(self.right_widget)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 4)

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

        # Add the menu bar with About action
        self.create_menubar()

    def create_menu(self):
        menu_layout = QVBoxLayout()
        self.add_menu_button(menu_layout, 'ΑΡΧΙΚΗ', 0)
        self.add_menu_button(menu_layout, 'CHAT', 1)
        self.add_menu_button(menu_layout, 'ΒΟΗΘΕΙΑ', 2)
        self.add_menu_button(menu_layout, 'ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ', 3)
        self.add_menu_button(menu_layout, 'ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ', 4)
        self.add_menu_button(menu_layout, 'ΕΠΙΚΟΙΝΩΝΙΑ', 5)

        exit_button = QPushButton('ΕΞΟΔΟΣ')
        exit_button.clicked.connect(self.close_application)
        menu_layout.addWidget(exit_button)
        menu_layout.addStretch()

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)
        menu_widget.setStyleSheet("background-color: #CDEAC0;")
        return menu_widget

    def add_menu_button(self, menu_layout, text, index):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.right_widget.setCurrentIndex(index))
        menu_layout.addWidget(button)

    def create_home_page(self):
        home_widget = QWidget()
        home_layout = QVBoxLayout()

        greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        greeting_label.setAlignment(Qt.AlignCenter)
        greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        home_layout.addWidget(greeting_label)

        bottom_layout = QHBoxLayout()

        left_box = QVBoxLayout()
        left_label = QLabel('Προσωπικά Στοιχεία', self)
        left_label.setAlignment(Qt.AlignCenter)
        left_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        left_box.addWidget(left_label)

        self.name_label = QLabel('Ονοματεπώνυμο:', self)
        self.name_edit = QLineEdit(self)
        self.name_edit.setReadOnly(True)
        left_box.addWidget(self.name_label)
        left_box.addWidget(self.name_edit)

        self.email_label = QLabel('email:', self)
        self.email_edit = QLineEdit(self)
        self.email_edit.setReadOnly(True)
        left_box.addWidget(self.email_label)
        left_box.addWidget(self.email_edit)

        self.phone_label = QLabel('Τηλέφωνο:', self)
        self.phone_edit = QLineEdit(self)
        self.phone_edit.setReadOnly(True)
        left_box.addWidget(self.phone_label)
        left_box.addWidget(self.phone_edit)

        self.edit_button = QPushButton('Επεξεργασία', self)
        self.edit_button.clicked.connect(self.enable_editing)
        left_box.addWidget(self.edit_button)

        self.save_button = QPushButton('Αποθήκευση', self)
        self.save_button.clicked.connect(self.save_data)
        self.save_button.setVisible(False)  # initially hidden
        left_box.addWidget(self.save_button)

        left_box.addWidget(QTextEdit(self))

        right_box = QVBoxLayout()
        right_label = QLabel('Ειδοποιήσεις', self)
        right_label.setAlignment(Qt.AlignCenter)
        right_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        right_box.addWidget(right_label)
        right_box.addWidget(QLineEdit(self))
        right_box.addWidget(QTextEdit(self))

        bottom_layout.addLayout(left_box)
        bottom_layout.addLayout(right_box)

        home_layout.addLayout(bottom_layout)

        home_widget.setLayout(home_layout)
        return home_widget

    def enable_editing(self):
        self.name_edit.setReadOnly(False)
        self.email_edit.setReadOnly(False)
        self.phone_edit.setReadOnly(False)
        self.save_button.setVisible(True)  # show the save button

    def save_data(self):
        # Add code here to save the data
        self.name_edit.setReadOnly(True)
        self.email_edit.setReadOnly(True)
        self.phone_edit.setReadOnly(True)
        self.save_button.setVisible(False)  # hide the save button again

    def create_menubar(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

    def close_application(self):
        QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
