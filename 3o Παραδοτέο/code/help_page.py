import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QCalendarWidget, QWidget, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QMessageBox, QComboBox, QCheckBox, QRadioButton, QButtonGroup, QScrollArea, QFrame, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QPushButton

class ContentWidget(QWidget):
    def __init__(self, content):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel(content, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class HelpWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        self.button1 = QPushButton("ΧΡΕΙΑΖΟΜΑΙ ΦΑΡΜΑΚΑ")
        self.button2 = QPushButton("ΨΑΧΝΩ ΓΙΑΤΡΟ")
        self.button3 = QPushButton("ΘΕΛΩ ΝΑ ΔΩΣΩ ΑΙΜΑ")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        self.button1.clicked.connect(parent.show_medicine_options)
        self.button2.clicked.connect(parent.show_doctor_search)
        self.button3.clicked.connect(lambda: parent.show_content("Θέλω Να Δώσω Αίμα", "Περιεχόμενο για Θέλω Να Δώσω Αίμα"))

        self.setLayout(self.layout)


class MedicineWidget(QWidget):
    # Define signal for when a medicine is selected
    medicine_selected = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        # Συμπτώματα
        self.symptom_layout = QHBoxLayout()
        self.symptom_label = QLabel("ΣΥΜΠΤΩΜΑΤΑ:", self)
        self.symptom_input = QLineEdit(self)
        self.symptom_list = QComboBox(self)
        self.symptom_list.addItems(["Πυρετός", "Βήχας", "Πονοκέφαλος"])  # Προσθήκη λίστας συμπτωμάτων
        self.symptom_layout.addWidget(self.symptom_label)
        self.symptom_layout.addWidget(self.symptom_input)
        self.symptom_layout.addWidget(self.symptom_list)

        # Απαιτείται Συνταγή
        self.prescription_layout = QHBoxLayout()
        self.prescription_label = QLabel("ΑΠΑΙΤΕΙΤΑΙ ΣΥΝΤΑΓΗ;", self)
        self.prescription_yes = QRadioButton("ΝΑΙ", self)
        self.prescription_no = QRadioButton("ΟΧΙ", self)
        self.prescription_group = QButtonGroup(self)
        self.prescription_group.addButton(self.prescription_yes)
        self.prescription_group.addButton(self.prescription_no)
        self.prescription_layout.addWidget(self.prescription_label)
        self.prescription_layout.addWidget(self.prescription_yes)
        self.prescription_layout.addWidget(self.prescription_no)

        # Search Button
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.perform_search)

        self.layout.addLayout(self.symptom_layout)
        self.layout.addLayout(self.prescription_layout)
        self.layout.addWidget(self.search_button)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def perform_search(self):
        # Πάρτε τα συμπτώματα που έχει εισάγει ο χρήστης
        selected_symptom = self.symptom_list.currentText()
        user_input_symptom = self.symptom_input.text()

        # Προετοιμάστε τα συμπτώματα για αναζήτηση (συμπτώματα + τυχόν επιπρόσθετα συμπτώματα που έχει εισάγει ο χρήστης)
        symptoms = [selected_symptom]
        if user_input_symptom:
            symptoms.append(user_input_symptom)

        # Πραγματοποιήστε την πραγματική αναζήτηση φαρμάκων εδώ, χρησιμοποιώντας τα συμπτώματα
        # Για τώρα, θα απλώς εκπέμψουμε ένα προκαθορισμένο λίστα φαρμάκων ως παράδειγμα
        medicines = [
            {"name": "Παρακεταμόλη", "description": "Για την ελάφρυνση του πυρετού και της πονοκέφαλου",
             "prescription_required": False},
            {"name": "Αμοξικιλλίνη", "description": "Αντιβιοτικό για τη θεραπεία βακτηριακών λοιμώξεων",
             "prescription_required": True},
            {"name": "Βουδεσονίδη", "description": "Για την αντιμετώπιση του βήχα", "prescription_required": False},
        ]

        # Εκπομπή των αποτελεσμάτων χρησιμοποιώντας το σήμα medicine_selected
        self.medicine_selected.emit(medicines)

class MedicineResultsWidget(QWidget):
    def __init__(self, medicines, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        for medicine in medicines:
            # Δημιουργία πλαισίου για κάθε φάρμακο
            medicine_frame = QFrame(self)
            medicine_frame.setFrameShape(QFrame.Box)
            medicine_frame.setLineWidth(2)
            medicine_layout = QVBoxLayout(medicine_frame)

            # Ετικέτα για το όνομα του φαρμάκου
            medicine_name_label = QLabel(f"{medicine['name']}", self)
            medicine_layout.addWidget(medicine_name_label)

            # Ετικέτα για την περιγραφή του φαρμάκου
            medicine_description_label = QLabel(f"{medicine['description']}", self)
            medicine_layout.addWidget(medicine_description_label)

            # Ετικέτα για την απαίτηση συνταγής
            prescription_required_label = QLabel(f"Απαιτεί συνταγή: {'Ναι' if medicine['prescription_required'] else 'Όχι'}", self)
            medicine_layout.addWidget(prescription_required_label)

            # Κουμπί για εμφάνιση περαιτέρω πληροφοριών
            select_button = QPushButton("Επιλογή", self)
            select_button.clicked.connect(lambda checked, med=medicine: self.show_medicine_details(med))
            medicine_layout.addWidget(select_button)

            # Προσθήκη του πλαισίου στην κύρια διάταξη
            self.layout.addWidget(medicine_frame)


        self.setLayout(self.layout)

    def show_medicine_details(self, medicine):
        # Εδώ μπορείτε να υλοποιήσετε τη λειτουργία που θέλετε όταν γίνει κλικ στο φάρμακο
        print("Εμφάνιση περαιτέρω πληροφοριών για το φάρμακο:", medicine['name'])



class ReviewWidget(QWidget):
    def __init__(self, doctor, parent):
        super().__init__(parent)
        self.doctor = doctor
        self.layout = QVBoxLayout()

        # Τίτλος
        self.title_label = QLabel(f"Υποβολή Αξιολόγησης για {doctor['name']}", self)
        self.layout.addWidget(self.title_label)

        # Πεδίο Αξιολόγησης
        self.review_text = QTextEdit(self)
        self.review_text.setPlaceholderText("Γράψτε την αξιολόγησή σας εδώ...")
        self.layout.addWidget(self.review_text)

        # Επιλογή Αστεριών
        self.rating_label = QLabel("Βαθμολογία:", self)
        self.layout.addWidget(self.rating_label)
        self.star_layout = QHBoxLayout()
        self.star_buttons = []
        for i in range(5):
            star_button = QRadioButton(f"{i + 1} Αστέρια", self)
            self.star_buttons.append(star_button)
            self.star_layout.addWidget(star_button)
        self.layout.addLayout(self.star_layout)

        # Κουμπί Υποβολής
        self.submit_button = QPushButton("Υποβολή", self)
        self.submit_button.clicked.connect(self.submit_review)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit_review(self):
        review_text = self.review_text.toPlainText()
        rating = next((i + 1 for i, btn in enumerate(self.star_buttons) if btn.isChecked()), None)
        if review_text and rating:
            # Προσθήκη αξιολόγησης σε μια λίστα αξιολογήσεων (θα μπορούσε να είναι βάση δεδομένων σε πραγματική εφαρμογή)
            self.parent().add_review(self.doctor, review_text, rating)
            self.parent().show_message("Ευχαριστούμε για την αξιολόγησή σας!")
        else:
            self.parent().show_message("Παρακαλώ συμπληρώστε την αξιολόγηση και επιλέξτε βαθμολογία.")
class ChatWidget(QWidget):
    def __init__(self, doctor, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        self.chat_label = QLabel(f"Chat με τον {doctor['name']}", self)
        self.layout.addWidget(self.chat_label)

        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.layout.addWidget(self.chat_history)

        self.chat_input = QLineEdit(self)
        self.chat_input.setPlaceholderText("Πληκτρολογήστε το μήνυμά σας εδώ...")
        self.layout.addWidget(self.chat_input)

        self.send_button = QPushButton("Αποστολή", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        # Αυτόματη αποστολή πρώτου μηνύματος
        self.chat_history.append(f"Dr. {doctor['name']}: Πώς μπορώ να σας βοηθήσω;")

    def send_message(self):
        message = self.chat_input.text()
        if message:
            self.chat_history.append(f"Εσείς: {message}")
            self.chat_input.clear()

class AppointmentWidget(QWidget):
    def __init__(self, doctor, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        self.calendar_label = QLabel(f"Κλείσιμο Ραντεβού με τον {doctor['name']}", self)
        self.layout.addWidget(self.calendar_label)

        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate.currentDate())
        self.layout.addWidget(self.calendar)

        self.book_button = QPushButton("Κλείσιμο Ραντεβού", self)
        self.book_button.clicked.connect(self.book_appointment)
        self.layout.addWidget(self.book_button)

        self.setLayout(self.layout)

    def book_appointment(self):
        selected_date = self.calendar.selectedDate()
        QMessageBox.information(self, "Ραντεβού Κλεισμένο", f"Το ραντεβού σας με τον {self.parent().doctor['name']} έχει κλειστεί για τις {selected_date.toString()}")

class DoctorSearchWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        # Πλαίσιο: ΤΙ ΨΑΧΝΕΤΕ;
        self.search_label = QLabel("ΤΙ ΨΑΧΝΕΤΕ;", self)
        self.search_label.setStyleSheet(
            "color: green; padding: 5px; border: 2px solid black; border-radius: 5px; font-weight: bold;")
        self.search_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.search_label)

        # Πλαίσιο: ΣΕ ΤΙ ΓΙΑΤΡΟ ΝΑ ΑΠΕΥΘΥΝΘΩ
        self.doctor_label = QLabel("ΣΕ ΤΙ ΓΙΑΤΡΟ ΝΑ ΑΠΕΥΘΥΝΘΩ", self)
        self.doctor_label.setStyleSheet("font-weight: bold; color: black;")
        self.doctor_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.doctor_label)

        # Ειδικότητα
        self.specialty_label = QLabel("Ειδικότητα:", self)
        self.specialty_combo = QComboBox(self)
        self.specialty_combo.addItems(["Γενικός Ιατρός", "Παιδίατρος", "Οδοντίατρος"])
        self.layout.addWidget(self.specialty_label)
        self.layout.addWidget(self.specialty_combo)

        # Περιοχή
        self.location_label = QLabel("Περιοχή:", self)
        self.location_combo = QComboBox(self)
        self.location_combo.addItems(["Αθήνα", "Θεσσαλονίκη", "Πάτρα"])
        self.layout.addWidget(self.location_label)
        self.layout.addWidget(self.location_combo)

        # Κατ' οίκον επίσκεψη
        self.home_visit_label = QLabel("Κατ' οίκον επίσκεψη:", self)
        self.home_visit_yes = QRadioButton("ΝΑΙ", self)
        self.home_visit_no = QRadioButton("ΟΧΙ", self)
        self.home_visit_group = QButtonGroup(self)
        self.home_visit_group.addButton(self.home_visit_yes)
        self.home_visit_group.addButton(self.home_visit_no)
        self.home_visit_layout = QHBoxLayout()
        self.home_visit_layout.addWidget(self.home_visit_yes)
        self.home_visit_layout.addWidget(self.home_visit_no)
        self.layout.addWidget(self.home_visit_label)
        self.layout.addLayout(self.home_visit_layout)

        # Search Button
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.perform_search)
        self.layout.addWidget(self.search_button)

        self.setLayout(self.layout)

    def perform_search(self):
        specialty = self.specialty_combo.currentText()
        location = self.location_combo.currentText()
        home_visit = self.home_visit_yes.isChecked()
        # Dummy data for doctors
        doctors = [
            {"name": "Dr. John Doe", "specialty": "Γενικός Ιατρός", "rating": "★★★★★", "location": "Αθήνα", "address": "Οδός Παράδειγμα 1", "availability": "Δευτέρα-Παρασκευή"},
            {"name": "Dr. Jane Smith", "specialty": "Παιδίατρος", "rating": "★★★★☆", "location": "Θεσσαλονίκη", "address": "Οδός Παράδειγμα 2", "availability": "Τρίτη-Σάββατο"},
            {"name": "Dr. Alice Johnson", "specialty": "Οδοντίατρος", "rating": "★★★☆☆", "location": "Πάτρα", "address": "Οδός Παράδειγμα 3", "availability": "Δευτέρα-Τετάρτη"},
        ]
        self.parent.show_doctor_results(doctors)

class DoctorActionsWidget(QWidget):
    def __init__(self, doctor, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()

        self.phone_button = QPushButton("Τηλέφωνο", self)
        self.phone_button.clicked.connect(lambda: self.call_doctor(doctor))  # Connect phone button

        self.chat_button = QPushButton("Τσατ", self)
        self.chat_button.clicked.connect(lambda: self.start_chat_with_doctor(doctor))  # Connect chat button

        self.appointment_button = QPushButton("Ραντεβού", self)
        self.appointment_button.clicked.connect(lambda: self.book_appointment_with_doctor(doctor))  # Connect appointment button

        self.layout.addWidget(self.phone_button)
        self.layout.addWidget(self.chat_button)
        self.layout.addWidget(self.appointment_button)

        self.setLayout(self.layout)

    def call_doctor(self, doctor):
        # Πραγματοποιήστε την κλήση του γιατρού χρησιμοποιώντας τον αριθμό τηλεφώνου
        phone_number = doctor.get('phone_number', None)
        if phone_number:
            # Εδώ θα μπορούσατε να υλοποιήσετε τη λειτουργία κλήσης
            pass

    def start_chat_with_doctor(self, doctor):
        # Εδώ θα μπορούσατε να ξεκινήσετε ένα τσατ με τον γιατρό
        pass

    def book_appointment_with_doctor(self, doctor):
        # Εδώ θα μπορούσατε να εμφανίσετε ένα ημερολόγιο για τον χρήστη να επιλέξει μια ημερομηνία
        pass

class DoctorDetailsWidget(QWidget):
    def __init__(self, doctor, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setWindowFlag(Qt.FramelessWindowHint)  # Remove window frame
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); border-radius: 15px; padding: 20px;")

        # Doctor details
        self.name_label = QLabel(f"Όνομα: {doctor['name']}", self)
        self.specialty_label = QLabel(f"Ειδικότητα: {doctor['specialty']}", self)
        self.location_label = QLabel(f"Περιοχή: {doctor['location']}", self)
        self.address_label = QLabel(f"Διεύθυνση Γραφείου: {doctor['address']}", self)
        self.availability_label = QLabel(f"Διαθεσιμότητα Ραντεβού: {doctor['availability']}", self)
        self.rating_label = QLabel(f"Αξιολογήσεις: {doctor['rating']}", self)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.specialty_label)
        self.layout.addWidget(self.location_label)
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.availability_label)
        self.layout.addWidget(self.rating_label)

        # Interaction buttons
        self.button_layout = QHBoxLayout()
        self.phone_button = QPushButton("Τηλέφωνο", self)
        self.phone_button.clicked.connect(lambda: self.call_doctor(doctor))  # Connect phone button
        self.phone_button.setCheckable(True)  # Κάνει το κουμπί επιλέξιμο
        self.chat_button = QPushButton("Τσατ", self)
        self.chat_button.clicked.connect(lambda: self.start_chat_with_doctor(doctor))  # Connect chat button
        self.chat_button.setCheckable(True)  # Κάνει το κουμπί επιλέξιμο
        self.appointment_button = QPushButton("Ραντεβού", self)
        self.appointment_button.clicked.connect(lambda: self.book_appointment_with_doctor(doctor))  # Connect appointment button
        self.appointment_button.setCheckable(True)  # Κάνει το κουμπί επιλέξιμο

        self.button_layout.addWidget(self.phone_button)
        self.button_layout.addWidget(self.chat_button)
        self.button_layout.addWidget(self.appointment_button)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

 # Add DoctorActionsWidget
        self.actions_widget = DoctorActionsWidget(doctor, self)
        self.layout.addWidget(self.actions_widget)

        self.setLayout(self.layout)
class DoctorResultsWidget(QWidget):
    def __init__(self, doctors, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        for doctor in doctors:
            doctor_frame = QFrame(self)
            doctor_frame.setFrameShape(QFrame.Box)
            doctor_frame.setLineWidth(2)
            doctor_layout = QVBoxLayout(doctor_frame)

            doctor_name_label = QLabel(f"Όνομα: {doctor['name']}", self)
            doctor_specialty_label = QLabel(f"Ειδικότητα: {doctor['specialty']}", self)
            doctor_rating_label = QLabel(f"Αξιολογήσεις: {doctor['rating']}", self)

            select_button = QPushButton("Επιλογή", self)
            select_button.clicked.connect(lambda checked, d=doctor: self.parent.show_doctor_details(d))

            doctor_layout.addWidget(doctor_name_label)
            doctor_layout.addWidget(doctor_specialty_label)
            doctor_layout.addWidget(doctor_rating_label)
            doctor_layout.addWidget(select_button)

            self.scroll_layout.addWidget(doctor_frame)

        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        self.setLayout(self.layout)


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
        self.content_area = HelpWidget(self)
        self.main_layout.addWidget(self.content_area)

    def show_medicine_options(self):
        self.clear_content()
        self.content_area = MedicineWidget(self)
        self.main_layout.addWidget(self.content_area)
        self.connect_medicine_widget(self.content_area)

    def show_medicine_results(self, medicines):
        self.clear_content()
        self.content_area = MedicineWidget(medicines, self)
        # Connect the signal to show medicine details
        self.content_area.medicine_selected.connect(self.show_medicine_details)
        self.main_layout.addWidget(self.content_area)

    def connect_medicine_widget(self, widget):
        widget.medicine_selected.connect(self.show_medicine_results)

    def show_medicine_details(self, medicine):
        self.clear_content()
        self.content_area = MedicineWidget(medicine, self)
        self.main_layout.addWidget(self.content_area)

    def show_doctor_search(self):
        self.clear_content()
        self.content_area = DoctorSearchWidget(self)
        self.main_layout.addWidget(self.content_area)

    def show_doctor_results(self, doctors):
        self.clear_content()
        self.content_area = DoctorResultsWidget(doctors, self)
        self.main_layout.addWidget(self.content_area)

    def show_doctor_details(self, doctor):
        self.clear_content()
        self.content_area = DoctorDetailsWidget(doctor, self)
        self.main_layout.addWidget(self.content_area)

    def show_chat_widget(self, doctor):
        self.clear_main_layout()
        self.chat_widget = ChatWidget(doctor, self)
        self.main_layout.addWidget(self.chat_widget)

    def show_phone_number(self, doctor):
        QMessageBox.information(self, "Αριθμός Τηλεφώνου", f"Ο αριθμός τηλεφώνου του {doctor['name']} είναι {doctor['phone']}")

    def show_appointment_widget(self, doctor):
        self.clear_main_layout()
        self.appointment_widget = AppointmentWidget(doctor, self)
        self.main_layout.addWidget(self.appointment_widget)

    def show_content(self, title, content):
        self.clear_content()
        self.content_area = ContentWidget(content)
        self.main_layout.addWidget(self.content_area)

    def clear_content(self):
        if self.content_area:
            self.main_layout.removeWidget(self.content_area)
            self.content_area.deleteLater()
            self.content_area = None

    def close_application(self):
        QApplication.instance().quit()

    def show_medicine_results(self, medicines):
        self.clear_content()
        self.content_area = MedicineResultsWidget(medicines, self)
        self.main_layout.addWidget(self.content_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

