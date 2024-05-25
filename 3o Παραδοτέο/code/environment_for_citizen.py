import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, 
                             QHBoxLayout, QLabel, QLineEdit, QTextEdit, QTabWidget, QMenuBar, QMessageBox, 
                             QTableWidget, QTableWidgetItem)
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

class MedicalProfileWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Create labels and line edits for user details
        self.first_name_label = QLabel("Όνομα:", self)
        self.first_name_edit = QLineEdit("Γιάννης", self)

        self.last_name_label = QLabel("Επώνυμο:", self)
        self.last_name_edit = QLineEdit("Παπαδόπουλος", self)

        self.age_label = QLabel("Ηλικία:", self)
        self.age_edit = QLineEdit("30", self)

        self.weight_label = QLabel("Βάρος:", self)
        self.weight_edit = QLineEdit("70kg", self)

        self.height_label = QLabel("Ύψος:", self)
        self.height_edit = QLineEdit("180cm", self)

        self.pressure_label = QLabel("Πίεση:", self)
        self.pressure_edit = QLineEdit("120/80", self)

        self.blood_group_label = QLabel("Ομάδα Αίματος:", self)
        self.blood_group_edit = QLineEdit("O+", self)

        self.eye_color_label = QLabel("Χρώμα Ματιών:", self)
        self.eye_color_edit = QLineEdit("Καστανά", self)

        # Add widgets to the layout
        self.layout.addWidget(self.first_name_label)
        self.layout.addWidget(self.first_name_edit)
        self.layout.addWidget(self.last_name_label)
        self.layout.addWidget(self.last_name_edit)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_edit)
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_edit)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_edit)
        self.layout.addWidget(self.pressure_label)
        self.layout.addWidget(self.pressure_edit)
        self.layout.addWidget(self.blood_group_label)
        self.layout.addWidget(self.blood_group_edit)
        self.layout.addWidget(self.eye_color_label)
        self.layout.addWidget(self.eye_color_edit)

        # Add edit button
        self.edit_button = QPushButton("ΕΠΕΞΕΡΓΑΣΙΑ ΔΕΔΟΜΕΝΩΝ", self)
        self.edit_button.clicked.connect(self.save_data)
        self.layout.addWidget(self.edit_button)

        self.setLayout(self.layout)

    def save_data(self):
        # Get data from line edits and do something with it (e.g., save to a file or database)
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        age = self.age_edit.text()
        weight = self.weight_edit.text()
        height = self.height_edit.text()
        pressure = self.pressure_edit.text()
        blood_group = self.blood_group_edit.text()
        eye_color = self.eye_color_edit.text()

        # Here you can perform actions with the retrieved data, such as saving it to a file or database
        with open('medical_profile.txt', 'w') as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Last Name: {last_name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Weight: {weight}\n")
            file.write(f"Height: {height}\n")
            file.write(f"Pressure: {pressure}\n")
            file.write(f"Blood Group: {blood_group}\n")
            file.write(f"Eye Color: {eye_color}\n")

        # Optionally, you can display a message to confirm that the data has been saved
        QMessageBox.information(self, "Αποθήκευση Δεδομένων", "Τα δεδομένα αποθηκεύτηκαν επιτυχώς.")

        # You can also clear the line edits after saving the data if needed
        self.clear_line_edits()

    def clear_line_edits(self):
        # Clear all line edits
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.age_edit.clear()
        self.weight_edit.clear()
        self.height_edit.clear()
        self.pressure_edit.clear()
        self.blood_group_edit.clear()
        self.eye_color_edit.clear()

class HealthWalletWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Create a label and table for displaying expenses
        self.expenses_label = QLabel("Δαπάνες Ασθενή:", self)
        self.expenses_table = QTableWidget(0, 2, self)
        self.expenses_table.setHorizontalHeaderLabels(["Φάρμακο", "Τιμή (€)"])

        # Create inputs for new expense
        self.new_expense_layout = QHBoxLayout()
        self.med_name_input = QLineEdit(self)
        self.med_name_input.setPlaceholderText("Φάρμακο")
        self.med_price_input = QLineEdit(self)
        self.med_price_input.setPlaceholderText("Τιμή (€)")
        self.add_expense_button = QPushButton("Προσθήκη", self)
        self.add_expense_button.clicked.connect(self.add_expense)
        self.new_expense_layout.addWidget(self.med_name_input)
        self.new_expense_layout.addWidget(self.med_price_input)
        self.new_expense_layout.addWidget(self.add_expense_button)

        # Create a label for total monthly expenses
        self.total_label = QLabel("Συνολικό Μηνιαίο Ποσό: 0.0€", self)

        # Add widgets to the layout
        self.layout.addWidget(self.expenses_label)
        self.layout.addWidget(self.expenses_table)
        self.layout.addLayout(self.new_expense_layout)
        self.layout.addWidget(self.total_label)

        self.setLayout(self.layout)

    def add_expense(self):
        med_name = self.med_name_input.text()
        med_price = self.med_price_input.text()

        if med_name and med_price:
            try:
                price = float(med_price)
                row_position = self.expenses_table.rowCount()
                self.expenses_table.insertRow(row_position)
                self.expenses_table.setItem(row_position, 0, QTableWidgetItem(med_name))
                self.expenses_table.setItem(row_position, 1, QTableWidgetItem(f"{price:.2f}"))

                self.update_total()

                self.med_name_input.clear()
                self.med_price_input.clear()
            except ValueError:
                QMessageBox.warning(self, "Σφάλμα", "Η τιμή πρέπει να είναι αριθμός.")
        else:
            QMessageBox.warning(self, "Σφάλμα", "Συμπληρώστε όλα τα πεδία.")

    def update_total(self):
        total = 0.0
        for row in range(self.expenses_table.rowCount()):
            price_item = self.expenses_table.item(row, 1)
            if price_item:
                total += float(price_item.text())

        self.total_label.setText(f"Συνολικό Μηνιαίο Ποσό: {total:.2f}€")

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)

        self.input_layout = QHBoxLayout()
        self.message_input = QLineEdit(self)
        self.send_button = QPushButton("Αποστολή", self)
        self.send_button.clicked.connect(self.send_message)

        self.input_layout.addWidget(self.message_input)
        self.input_layout.addWidget(self.send_button)

        self.layout.addWidget(self.chat_area)
        self.layout.addLayout(self.input_layout)

        self.setLayout(self.layout)

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.chat_area.append(f"Εσύ: {message}")
            self.message_input.clear()
            # Here you could also add the code to send the message to the server or handle it accordingly

class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.help_label = QLabel("Βοήθεια", self)
        self.help_label.setAlignment(Qt.AlignCenter)
        self.help_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.help_text = QTextEdit(self)
        self.help_text.setReadOnly(True)
        self.help_text.setText("Εδώ μπορείτε να βρείτε βοήθεια σχετικά με τη χρήση της εφαρμογής...\n\n"
                               "1. Για να περιηγηθείτε στην εφαρμογή, χρησιμοποιήστε το μενού στα αριστερά.\n"
                               "2. Στην καρτέλα ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ, μπορείτε να δείτε και να επεξεργαστείτε τα ιατρικά σας στοιχεία.\n"
                               "3. Στην καρτέλα ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ, μπορείτε να προσθέσετε και να δείτε τις δαπάνες σας.\n"
                               "4. Στην καρτέλα CHAT, μπορείτε να συνομιλήσετε με έναν σύμβουλο ή γιατρό.\n"
                               "5. Εάν χρειάζεστε επιπλέον βοήθεια, επικοινωνήστε μαζί μας μέσω της καρτέλας ΕΠΙΚΟΙΝΩΝΙΑ.")
        
        self.layout.addWidget(self.help_label)
        self.layout.addWidget(self.help_text)

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
        self.tab2 = ChatWidget()  # Use ChatWidget for the chat page
        self.tab3 = HelpWidget()  # Use HelpWidget for the help page
        self.tab4 = MedicalProfileWidget()  # Use MedicalProfileWidget for the medical profile page
        self.tab5 = HealthWalletWidget()  # Use HealthWalletWidget for the health wallet page
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