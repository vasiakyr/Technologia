import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QTextEdit, QMessageBox,
    QComboBox, QCalendarWidget, QWidget, QScrollArea, QFrame, QTextBrowser
)
from PyQt5.QtCore import Qt, QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Health Application")
        self.setGeometry(100, 100, 1200, 600)
        self.content_area = None

        self.main_layout = QHBoxLayout()
        self.menu_widget = self.create_menu()
        self.main_layout.addWidget(self.menu_widget)

        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()

        self.greeting_label = QLabel('Welcome, ΟΝΟΜΑ ΧΡΗΣΤΗ!', self)
        self.greeting_label.setAlignment(Qt.AlignCenter)
        self.greeting_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.content_layout.addWidget(self.greeting_label)

        self.content_area.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_area)

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

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

    def add_menu_button(self, menu_layout, text, window_title=None, window_content=None):
        button = QPushButton(text, self)
        if text == 'ΑΡΧΙΚΗ':
            button.clicked.connect(self.show_home_page)
        elif text == 'ΒΟΗΘΕΙΑ':
            button.clicked.connect(self.show_help_page)
        else:
            button.clicked.connect(lambda: self.show_content(window_title, window_content))
        menu_layout.addWidget(button)

    def show_home_page(self):
        self.clear_content()
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

    def show_help_page(self):
        self.clear_content()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Αναζήτηση γιατρού...")

        self.search_button = QPushButton("Αναζήτηση", self)
        self.search_button.clicked.connect(self.search_doctors)

        self.results_area = QScrollArea(self)
        self.results_area.setWidgetResizable(True)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        layout = QVBoxLayout()
        layout.addLayout(search_layout)
        layout.addWidget(self.results_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def search_doctors(self):
        search_text = self.search_input.text()
        doctors = [
            {'name': 'Dr. Ιωάννης Παπαδόπουλος', 'specialty': 'Παθολόγος', 'location': 'Αθήνα', 'address': 'Λεωφόρος Κηφισίας 10', 'availability': '09:00-17:00', 'rating': '4.5', 'phone_number': '2101234567'},
            {'name': 'Dr. Μαρία Καραγιάννη', 'specialty': 'Δερματολόγος', 'location': 'Θεσσαλονίκη', 'address': 'Οδός Εγνατία 22', 'availability': '10:00-16:00', 'rating': '4.7', 'phone_number': '2310123456'}
        ]
        filtered_doctors = [doctor for doctor in doctors if search_text.lower() in doctor['name'].lower()]

        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout()

        for doctor in filtered_doctors:
            doctor_widget = DoctorWidget(doctor, self)
            self.results_layout.addWidget(doctor_widget)

        self.results_widget.setLayout(self.results_layout)
        self.results_area.setWidget(self.results_widget)

    def show_content(self, title, content):
        self.clear_content()
        self.content_area = QLabel(content, self)
        self.main_layout.addWidget(self.content_area)

    def clear_content(self):
        if self.content_area:
            self.main_layout.removeWidget(self.content_area)
            self.content_area.deleteLater()
            self.content_area = None

    def close_application(self):
        QApplication.instance().quit()


class DoctorWidget(QWidget):
    def __init__(self, doctor, parent=None):
        super().__init__(parent)
        self.doctor = doctor
        self.layout = QVBoxLayout()

        self.name_label = QLabel(f"Όνομα: {doctor['name']}")
        self.specialty_label = QLabel(f"Ειδικότητα: {doctor['specialty']}")
        self.location_label = QLabel(f"Περιοχή: {doctor['location']}")
        self.address_label = QLabel(f"Διεύθυνση: {doctor['address']}")
        self.availability_label = QLabel(f"Διαθεσιμότητα: {doctor['availability']}")
        self.rating_label = QLabel(f"Αξιολογήσεις: {doctor['rating']}")

        self.phone_button = QPushButton("Τηλέφωνο", self)
        self.phone_button.clicked.connect(self.show_phone)

        self.chat_button = QPushButton("Τσατ", self)
        self.chat_button.clicked.connect(self.start_chat)

        self.appointment_button = QPushButton("Ραντεβού", self)
        self.appointment_button.clicked.connect(self.book_appointment)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.specialty_label)
        self.layout.addWidget(self.location_label)
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.availability_label)
        self.layout.addWidget(self.rating_label)
        self.layout.addWidget(self.phone_button)
        self.layout.addWidget(self.chat_button)
        self.layout.addWidget(self.appointment_button)
        self.setLayout(self.layout)

    def show_phone(self):
        QMessageBox.information(self, "Αριθμός Τηλεφώνου", f"Ο αριθμός τηλεφώνου του {self.doctor['name']} είναι {self.doctor['phone_number']}")

    def start_chat(self):
        self.chat_window = ChatWidget(self.doctor)
        self.chat_window.show()

    def book_appointment(self):
        self.appointment_window = AppointmentWidget(self.doctor)
        self.appointment_window.show()


class ChatWidget(QWidget):
    def __init__(self, doctor, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Συνομιλία με τον {doctor['name']}")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.chat_display = QTextBrowser(self)
        self.chat_display.append("Πώς μπορώ να σας βοηθήσω;")

        self.message_input = QLineEdit(self)
        self.send_button = QPushButton("Αποστολή", self)
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.message_input)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.chat_display.append(f"Εσείς: {message}")
            self.message_input.clear()


class AppointmentWidget(QWidget):
    def __init__(self, doctor, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Κλείσιμο Ραντεβού με τον {doctor['name']}")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate.currentDate().addDays(1))
        self.calendar.setMaximumDate(QDate.currentDate().addMonths(3))
        self.layout.addWidget(self.calendar)

        self.confirm_button = QPushButton("Επιβεβαίωση Ραντεβού", self)
        self.confirm_button.clicked.connect(self.confirm_appointment)
        self.layout.addWidget(self.confirm_button)
        self.setLayout(self.layout)

    def confirm_appointment(self):
        selected_date = self.calendar.selectedDate().toString(Qt.ISODate)
        QMessageBox.information(self, "Επιβεβαίωση Ραντεβού", f"Το ραντεβού σας με τον {self.doctor['name']} έχει κλειστεί για {selected_date}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
