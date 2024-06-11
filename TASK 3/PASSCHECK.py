import tkinter as tk
from tkinter import ttk, messagebox
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~`\-\\]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    error_msgs = ["Password must be at least 8 characters long.",
                  "Password must contain at least one digit.",
                  "Password must contain at least one uppercase letter.",
                  "Password must contain at least one lowercase letter.",
                  "Password must contain at least one special character (!@#$%^&*()_+{}[]:;<>,.?/~`-\\)."]

    strength = sum(errors)
    return strength, [error_msgs[i] for i in range(len(errors)) if errors[i]]

def update_strength_bar(password):
    strength, _ = check_password_strength(password)
    progress = int(((5 - strength) / 5) * 100)  # Convert strength to a percentage for the progress bar
    strength_bar['value'] = progress

    if progress > 80:
        strength_bar['style'] = 'green.Horizontal.TProgressbar'
    elif progress > 50:
        strength_bar['style'] = 'blue.Horizontal.TProgressbar'
    elif progress > 30:
        strength_bar['style'] = 'orange.Horizontal.TProgressbar'
    else:
        strength_bar['style'] = 'red.Horizontal.TProgressbar'

def check_password():
    password = password_entry.get()
    strength, error_msgs = check_password_strength(password)
    if strength == 0:
        messagebox.showinfo("Password Strength", "Strong password!")
    else:
        messagebox.showwarning("Password Strength", "Weak password!\n{}".format("\n".join(error_msgs)))

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.configure(bg="#f0f0f0")  # Set background color

# Define color scheme
bg_color = "#f0f0f0"
fg_color = "#333333"
accent_color = "#007bff"  # Blue color
button_bg_color = "#007bff"
button_fg_color = "#ffffff"

password_label = tk.Label(root, text="Enter Password:", bg=bg_color, fg=fg_color)
password_label.grid(row=0, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*", bg=bg_color, fg=fg_color, insertbackground=accent_color)
password_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry.bind("<KeyRelease>", lambda event: update_strength_bar(password_entry.get()))

strength_label = tk.Label(root, text="Password Strength:", bg=bg_color, fg=fg_color)
strength_label.grid(row=1, column=0, padx=10, pady=5)

style = ttk.Style()
style.theme_use('default')
style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
style.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')
style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

strength_bar = ttk.Progressbar(root, length=200, mode='determinate', style="red.Horizontal.TProgressbar")
strength_bar.grid(row=1, column=1, padx=10, pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password, bg=button_bg_color, fg=button_fg_color)
check_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
