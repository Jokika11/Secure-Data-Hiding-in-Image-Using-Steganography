# 🔐 Secure Steganography: Encrypt & Decrypt Messages in Images  

## 📌 Overview  
This project provides a **Python-based steganography tool** that allows users to **hide and encrypt messages** inside images and later extract and decrypt them securely. It uses **Fernet encryption**, **zlib compression**, and **LSB (Least Significant Bit) steganography** for an added layer of security.  

✅ **Encrypt & hide messages** inside images.  
✅ **Extract & decrypt messages** securely using a password.  
✅ **User-friendly GUI** built with `tkinter` & `ttkthemes`.  
✅ **Supports `.png`, `.jpg`, `.jpeg` image formats**.  
✅ **Strong password enforcement** for security.  


## 🚀 Installation  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/Jokika11/Secure-Data-Hiding-in-Image-Using-Steganography.git
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```


## 🔒 Encrypt & Hide a Message (`encrypt_GUI.py`)  

### 🛠 Features  
- Uses **LSB steganography** to store encrypted messages inside images.  
- **Fernet encryption** ensures only authorized users can retrieve messages.  
- **Password strength validation** to prevent weak passwords.  
- **Modern GUI** for an intuitive experience.  

### 🖼️ How It Works  
1. Run `Encrypt_GUI.py`.  
   ```sh
   python Encrypt_GUI.py
   ```
2. Select an image.  
3. Enter your secret message and a strong password.  
4. Click "Encrypt & Hide" to embed the message into the image.  
5. Save the new image with the hidden message.  


## 🔓 Decrypt & Extract a Message (`decrypt_GUI.py`)  

### 🛠 Features  
- Extracts the hidden message from an image using **LSB extraction**.  
- **Password-protected decryption** ensures security.  
- **Error handling** for incorrect passwords or corrupted images.  
- **User-friendly interface** for seamless decryption.  

### 🖼️ How It Works  
1. Run `Decrypt_GUI.py`.  
   ```sh
   python Decrypt_GUI.py
   ```
2. Select the image containing the hidden message.  
3. Enter the correct password.  
4. Click "Extract Message" to retrieve the decrypted content.  


## 🏗️ Built With  
- **Python** - Core Programming Language  
- **tkinter & ttkthemes** - GUI Framework  
- **Pillow (PIL)** - Image Processing  
- **Cryptography** - Secure Encryption  
- **zlib** - Compression Handling  


## 🛡️ Security  
🔹 Uses **Fernet encryption** for confidentiality.  
🔹 **Password enforcement** (uppercase, lowercase, digit, special character).  
🔹 **LSB steganography** ensures discreet message embedding.  

## 📜 License
This project is licensed under the **MIT License**.

## Author
Developed by **Jokika V**


