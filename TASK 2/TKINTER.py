import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)
    key = np.resize(key, img_array.shape)
    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image.png")
    return "encrypted_image.png"

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)
    key = np.resize(key, encrypted_array.shape)
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image.png")
    return "decrypted_image.png"

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)
        load_image(file_path, label_original)

def load_image(image_path, label):
    img = Image.open(image_path)
    img.thumbnail((250, 250))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

def encrypt():
    image_path = entry_image_path.get()
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
    encrypted_image_path = encrypt_image(image_path, key)
    load_image(encrypted_image_path, label_encrypted)
    np.save("encryption_key.npy", key)
    messagebox.showinfo("Success", "Image encrypted successfully.")

def decrypt():
    encrypted_image_path = "encrypted_image.png"
    try:
        key = np.load("encryption_key.npy")
    except FileNotFoundError:
        messagebox.showerror("Error", "Encryption key not found. Encrypt an image first.")
        return
    
    decrypted_image_path = decrypt_image(encrypted_image_path, key)
    load_image(decrypted_image_path, label_decrypted)
    messagebox.showinfo("Success", "Image decrypted successfully.")

# Create the main window
root = tk.Tk()
root.title("Image Encryption and Decryption @Sherwin @ProdigyInfoTech")
root.geometry("800x600")
root.resizable(True, True)

# Load background image
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

def resize_background(event):
    new_width = event.width
    new_height = event.height
    resized_image = background_image.resize((new_width, new_height), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")
    canvas.lower("all")

canvas.bind("<Configure>", resize_background)

# Create and place the widgets on the canvas
frame = tk.Frame(root, bg='#2b2b2b')
frame.place(relx=0.5, rely=0.5, anchor="center")

label_heading = tk.Label(frame, text="Image Encryptor & Decryptor🛠️", fg='white', bg='#2b2b2b', font=("Helvetica", 16, "bold"))
label_heading.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

label_image_path = tk.Label(frame, text="Select Image:", fg='white', bg='#2b2b2b')
label_image_path.grid(row=1, column=0, padx=10, pady=10)

entry_image_path = tk.Entry(frame, width=50, bg='#3c3c3c', fg='white', insertbackground='white')
entry_image_path.grid(row=1, column=1, padx=10, pady=10)

button_browse = tk.Button(frame, text="Browse", command=select_image, bg='#5a5a5a', fg='white', activebackground='#757575', activeforeground='white')
button_browse.grid(row=1, column=2, padx=10, pady=10)

button_encrypt = tk.Button(frame, text="Encrypt Image", command=encrypt, bg='#5a5a5a', fg='white', activebackground='#757575', activeforeground='white')
button_encrypt.grid(row=2, column=0, columnspan=3, pady=10)

button_decrypt = tk.Button(frame, text="Decrypt Image", command=decrypt, bg='#5a5a5a', fg='white', activebackground='#757575', activeforeground='white')
button_decrypt.grid(row=3, column=0, columnspan=3, pady=10)

label_original = tk.Label(root, bg='#2b2b2b')
label_original.place(relx=0.1, rely=0.8, anchor="center")

label_encrypted = tk.Label(root, bg='#2b2b2b')
label_encrypted.place(relx=0.5, rely=0.8, anchor="center")

label_decrypted = tk.Label(root, bg='#2b2b2b')
label_decrypted.place(relx=0.9, rely=0.8, anchor="center")

root.mainloop()
