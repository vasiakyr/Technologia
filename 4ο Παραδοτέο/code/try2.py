import tkinter as tk
from tkinter import ttk

# Function to handle submission
def submit_review():
    rating = rating_var.get()
    comments = comments_text.get("1.0", tk.END).strip()
    print(f"Submitted Rating: {rating}/10")
    print(f"Submitted Comments: {comments}")

# Create the main window
root = tk.Tk()
root.title("Doctor Review")
root.geometry("800x600")

# Create sidebar frame
sidebar = tk.Frame(root, bg='darkgreen', width=200)
sidebar.pack(side='left', fill='y')

# Add buttons to the sidebar
buttons = [
    ("ΑΡΧΙΚΗ", lambda: print("ΑΡΧΙΚΗ clicked")),
    ("CHAT", lambda: print("CHAT clicked")),
    ("ΒΟΗΘΕΙΑ", lambda: print("ΒΟΗΘΕΙΑ clicked")),
    ("ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ", lambda: print("ΙΑΤΡΙΚΟ ΠΡΟΦΙΛ clicked")),
    ("ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ", lambda: print("ΠΟΡΤΟΦΟΛΙ ΥΓΕΙΑΣ clicked")),
    ("ΕΠΙΚΟΙΝΩΝΙΑ", lambda: print("ΕΠΙΚΟΙΝΩΝΙΑ clicked")),
    ("ΕΞΟΔΟΣ", lambda: root.quit())
]

for text, command in buttons:
    btn = tk.Button(sidebar, text=text, bg='darkgreen', fg='white', command=command, padx=10, pady=5, anchor='w')
    btn.pack(fill='x')

# Create main content frame
content = tk.Frame(root, bg='white')
content.pack(side='right', fill='both', expand=True)

# Doctor's information frame
doctor_frame = tk.Frame(content, bg='white', padx=20, pady=20)
doctor_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Doctor's image placeholder
doctor_image = tk.Label(doctor_frame, text="", bg='green', width=10, height=5)
doctor_image.grid(row=0, column=0, rowspan=2, padx=20, pady=10)

# Doctor's name
doctor_name = tk.Label(doctor_frame, text="Όνομα Γιατρού", bg='white', font=("Helvetica", 16))
doctor_name.grid(row=0, column=1, sticky='w', pady=10)

# Rating section
rating_label = tk.Label(doctor_frame, text="Κάνε μια αξιολόγηση:", bg='white', font=("Helvetica", 12))
rating_label.grid(row=1, column=1, sticky='w', pady=10)

# Stars rating
rating_var = tk.IntVar()
stars_frame = tk.Frame(doctor_frame, bg='white')
stars_frame.grid(row=2, column=1, sticky='w', pady=10)

for i in range(10):
    star = tk.Radiobutton(stars_frame, text="★", variable=rating_var, value=i+1, bg='white', fg='green', selectcolor='white', indicatoron=0)
    star.pack(side='left', padx=1)

rating_scale = tk.Label(stars_frame, text="/10", bg='white', font=("Helvetica", 12))
rating_scale.pack(side='left', padx=10)

# Comments section
comments_label = tk.Label(doctor_frame, text="Σχόλια:", bg='white', font=("Helvetica", 12))
comments_label.grid(row=3, column=0, sticky='nw', pady=10)

comments_text = tk.Text(doctor_frame, width=50, height=10, borderwidth=1, relief="solid")
comments_text.grid(row=3, column=1, pady=10, padx=20)

# Submit button
submit_button = tk.Button(doctor_frame, text="Υποβολή", bg='green', fg='white', command=submit_review)
submit_button.grid(row=4, column=1, sticky='e', pady=20)

root.mainloop()
