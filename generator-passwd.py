import string
import secrets
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

# constantes
LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation
GENERATE = LETTERS + NUMBERS + SYMBOLS

# paramètres
LENGTH = 20  # longueur du mot de passe
VERSION = "1.1.0"  # version du programme

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator | Developed by : Noxious")
        self.root.geometry("450x300")
        self.password = self.generate_password(LENGTH)
        self.password_label = None
        self.create_widgets()

    def generate_password(self, length):
        return "".join(secrets.choice(GENERATE) for i in range(length))

    def create_widgets(self):
        tk.Label(self.root, text="Welcome!", foreground="green", background="grey", width=100, font="Arial").pack()
        self.password_label = tk.Label(self.root, text=f"Votre mot de passe est : {self.password}", foreground="green", background="grey", width=100, font="Arial")
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
