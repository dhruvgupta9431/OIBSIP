import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate random password
def generate_password():
    length = password_length.get()
    if not length.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
        return

    length = int(length)
    if length <= 0:
        messagebox.showerror("Invalid Input", "Password length must be greater than zero.")
        return

    characters = ''
    if include_letters.get():
        characters += string.ascii_letters
    if include_numbers.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Selection", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg='#d0eaff')  # Light blue background color
root.resizable(False, False)

# Create a frame to center the content
frame = tk.Frame(root, bg='#d0eaff')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Add header
header = tk.Label(frame, text="Random Password Generator", bg='#d0eaff', font=("Helvetica", 24, "bold"))
header.grid(row=0, column=0, columnspan=2, pady=20)

# Create and place widgets inside the frame
tk.Label(frame, text="Password Length:", bg='#d0eaff', font=("Helvetica", 14)).grid(row=1, column=0, padx=10, pady=10)
password_length = tk.Entry(frame, font=("Helvetica", 14))
password_length.grid(row=1, column=1, padx=10, pady=10)

include_letters = tk.BooleanVar()
include_numbers = tk.BooleanVar()
include_special = tk.BooleanVar()

tk.Checkbutton(frame, text="Include Letters", variable=include_letters, bg='#d0eaff', font=("Helvetica", 14)).grid(row=2, column=0, columnspan=2, pady=5)
tk.Checkbutton(frame, text="Include Numbers", variable=include_numbers, bg='#d0eaff', font=("Helvetica", 14)).grid(row=3, column=0, columnspan=2, pady=5)
tk.Checkbutton(frame, text="Include Special Characters", variable=include_special, bg='#d0eaff', font=("Helvetica", 14)).grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(frame, text="Generate Password", command=generate_password, bg='#4caf50', fg='white', font=("Helvetica", 14)).grid(row=5, column=0, columnspan=2, pady=10)

password_var = tk.StringVar()
tk.Entry(frame, textvariable=password_var, state='readonly', width=50, font=("Helvetica", 14)).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, bg='#2196f3', fg='white', font=("Helvetica", 14)).grid(row=7, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
