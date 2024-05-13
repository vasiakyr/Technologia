import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

class DrugSearchPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ΚΑΛΩΣ ΗΡΘΕΣ "ΟΝΟΜΑ ΧΡΗΣΤΗ"')

        # Widgets
        self.label_title = QLabel('Drug Search', self)
        self.label_instructions = QLabel('Enter drug name:', self)
        self.lineedit_drug_name = QLineEdit(self)
        self.button_search = QPushButton('Search', self)

        # Apply font, style, and color to the widgets
        self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; color: #336699;")
        self.label_instructions.setStyleSheet("font-size: 18px; color: #333333;")
        self.lineedit_drug_name.setStyleSheet("font-size: 16px; color: #333333; background-color: #f0f0f0;")
        self.button_search.setStyleSheet("font-size: 16px; color: #ffffff; background-color: #008000;")

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

        # Content layout
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.label_title)
        content_layout.addWidget(self.label_instructions)
        content_layout.addWidget(self.lineedit_drug_name)
        content_layout.addWidget(self.button_search)

        # Combine menu and content layouts using QHBoxLayout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.menu_widget)
        main_layout.addLayout(content_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Connect button signal to function
        self.button_search.clicked.connect(self.search_drug)

        # Set the fixed size of the window
        self.setFixedSize(1200, 600)  # Adjust the width and height as needed

    def search_drug(self):
        # Get the drug name entered by the user
        drug_name = self.lineedit_drug_name.text()

        # Here you would implement the functionality to filter drugs based on the name
        # and display the results to the user in a new window or widget.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrugSearchPage()
    window.show()
    sys.exit(app.exec_())
