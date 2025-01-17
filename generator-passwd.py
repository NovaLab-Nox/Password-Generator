import string
import secrets
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import cryptography
from cryptography.fernet import Fernet
# constantes
LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation
GENERATE = LETTERS + NUMBERS + SYMBOLS

# paramètres
LENGTH = 10  # longueur du mot de passe
VERSION = "1.2.2"  # version du programme

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator | Developed by : Nox")
        self.root.geometry("645x350")
        style = ttk.Style()
        style.theme_use("clam")
        self.password = self.generate_password(LENGTH)
        self.password_label = None
        self.create_widgets()

    def generate_password(self, length):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password

    def hash_password(password):
        import hashlib
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def store_password(password):
        # utiliser un mécanisme de chiffrement pour stocker le mot de passe
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(password.encode())
        return cipher_text

    def create_widgets(self):
        tk.Label(self.root, text="Password Generator", font=("Courier", 24), foreground="#ff0000", background="#000000",
                 borderwidth=2, relief="raised").pack()
        self.password_label = tk.Label(self.root, text=f"Votre mot de passe est : {self.password}", foreground="#ff0000", background="#000000", width=100, font="Courier")
        self.password_label.pack()
        tk.Button(self.root, text="Générer un nouveau mot de passe", command=self.generate_new_password).pack()
        tk.Button(self.root, text="Copier le mot de passe", command=self.copy_password).pack()
        tk.Button(self.root, text="Quitter", command=self.root.destroy).pack()

    def generate_new_password(self):
        self.password = self.generate_password(LENGTH)
        self.password_label['text'] = f"Votre nouveau mot de passe est : {self.password}"

    def copy_password(self):
        pyperclip.copy(self.password)
        messagebox.showinfo("Mot de passe copié", "Le mot de passe a été copié dans le presse-papier")

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    print("Welcome on Password Generator")
    print("Developed by : Nox")
    print("Version: " + VERSION)
    generator = PasswordGenerator()
    generator.run()
