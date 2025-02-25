# decrypt.py
import base64
import zlib
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from cryptography.fernet import Fernet
from ttkthemes import ThemedTk
from tkinter import ttk

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode('utf-8'))


def extract_message(image_path, password):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    binary_message = ''

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)

    binary_message = binary_message[:binary_message.find('00000000')]
    encrypted_message = bytearray(int(binary_message[i:i + 8], 2) for i in range(0, len(binary_message), 8))

    key = generate_key(password)
    cipher_suite = Fernet(key)
    compressed_message = cipher_suite.decrypt(bytes(encrypted_message))
    return zlib.decompress(compressed_message).decode('utf-8')


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    entry_image.delete(0, 'end')
    entry_image.insert(0, file_path)


def decrypt_message():
    image_path = entry_image.get()
    password = entry_password.get()

    try:
        message = extract_message(image_path, password)
        label_status.config(text=f"Extracted message: {message}")
        label_status.configure(foreground='green')
    except Exception as e:
        label_status.config(text="Failed to extract message. Incorrect password or corrupted image.")
        label_status.configure(foreground='red')

root = ThemedTk(theme="arc")
root.title("Decrypt Hidden Message")
root.geometry("400x300")
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

ttk.Label(frame, text="Enter Password:").pack()
entry_password = ttk.Entry(frame, width=40, show="*")
entry_password.pack()

ttk.Button(frame, text="Extract Message", command=decrypt_message).pack(pady=10)
label_status = ttk.Label(frame, text="")
label_status.pack()

root.mainloop()
