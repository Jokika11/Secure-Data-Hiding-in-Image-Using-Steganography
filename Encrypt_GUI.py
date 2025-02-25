# encrypt.py
import os
import re
import zlib
import base64
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from cryptography.fernet import Fernet
from ttkthemes import ThemedTk
from tkinter import ttk

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode('utf-8'))

def is_strong_password(password):
    return (
            len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*()_+=\-<>?]", password)
    )

def encrypt_message(message, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)
    compressed_message = zlib.compress(message.encode('utf-8'))
    return cipher_suite.encrypt(compressed_message)

def hide_message(image_path, message, password, output_path):
    image = Image.open(image_path).convert('RGB')
    encrypted_message = encrypt_message(message, password)
    binary_message = ''.join(format(byte, '08b') for byte in encrypted_message)

    pixels = image.load()
    width, height = image.size
    idx = 0
    for y in range(height):
        for x in range(width):
            if idx < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
    image.save(output_path)

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '.png;.jpg;*.jpeg')])
    entry_image.delete(0, 'end')
    entry_image.insert(0, file_path)

def encrypt_and_hide():
    image_path = entry_image.get()
    message = entry_message.get()
    password = entry_password.get()
    output_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Image', '*.png')])

    if not is_strong_password(password):
        label_status.config(text="Weak password! Use uppercase, lowercase, digit, and special character.")
        label_status.configure(foreground='red')
        return

    hide_message(image_path, message, password, output_path)
    label_status.config(text=f"Message hidden in {output_path}")
    label_status.configure(foreground='green')

root = ThemedTk(theme="arc")
root.title("Encrypt and Hide Message")
root.geometry("400x350")
root.configure(bg='black')
root.attributes('-alpha', 0.9)  # Semi-transparent background

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), background='black', foreground='white')

frame = tk.Frame(root, bg='black')
frame.pack(pady=20)

ttk.Label(frame, text="Select Image:").pack()
entry_image = ttk.Entry(frame, width=40)
entry_image.pack()
ttk.Button(frame, text="Browse", command=select_image).pack(pady=5)

ttk.Label(frame, text="Enter Message:").pack()
entry_message = ttk.Entry(frame, width=40)
entry_message.pack()

ttk.Label(frame, text="Enter Password:").pack()
entry_password = ttk.Entry(frame, width=40, show="*")
entry_password.pack()

ttk.Button(frame, text="Encrypt & Hide", command=encrypt_and_hide).pack(pady=10)
label_status = ttk.Label(frame, text="")
label_status.pack()

root.mainloop()