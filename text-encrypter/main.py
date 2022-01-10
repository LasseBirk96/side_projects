import tkinter as tk
import cryptocode
import random


class App:
    def __init__(self, root):
        root.title("Text Encrypter")
        height = 275
        width = 350
        metrics = f"{width}x{height}"
        root.geometry(metrics)
        root.resizable(width=False, height=False)

        self.label_button = tk.Button(
            root,
            text="Text Encrypter",
            font=("Times New Roman", 24),
            command=self.change_color,
        )
        self.label_button.place(x=0, y=15, width=350, height=30)

        self.text_entry = tk.Entry(root, font=("Times New Roman", 16))
        self.text_entry.place(x=65, y=60, width=275, height=30)
        self.text_entry_label = tk.Label(
            root, text="Text:", font=("Times New Roman", 16)
        )
        self.text_entry_label.place(x=10, y=60, width=40, height=30)

        self.key_entry = tk.Entry(root, font=("Times New Roman", 16))
        self.key_entry.place(x=65, y=100, width=275, height=30)
        self.key_entry_label = tk.Label(root, text="Key:", font=("Times New Roman", 16))
        self.key_entry_label.place(x=10, y=100, width=40, height=30)

        self.encrypt_button = tk.Button(
            root,
            text="Encrypt",
            font=("Times New Roman", 16),
            command=self.encrypt_text,
        )

        self.encrypt_button.place(x=10, y=140, width=330, height=30)

        self.decrypt_button = tk.Button(
            root,
            text="Decrypt",
            font=("Times New Roman", 16),
            command=self.decrypt_text,
        )
        self.decrypt_button.place(x=10, y=180, width=330, height=30)

        self.result_entry = tk.Entry(root, font=("Times New Roman", 16))
        self.result_entry.place(x=65, y=220, width=275, height=30)
        self.result_entry_label = tk.Label(
            root, text="Result:", font=("Times New Roman", 16)
        )
        self.result_entry_label.place(x=10, y=220, width=50, height=30)

        # state="disabled" means that you can't interact with the field it self
        self.result_entry.config(state="disabled")

    def encrypt_text(self):
        """This method encrypts the text with a given key"""
        text = self.text_entry.get()
        key = self.key_entry.get()
        result = cryptocode.encrypt(text, key)
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def decrypt_text(self):
        """This method decrypts the text with a given key"""
        text = self.text_entry.get()
        key = self.key_entry.get()
        result = cryptocode.decrypt(text, key)
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def change_color(self):
        """Changes color on the header, if clicked"""
        array_of_colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        random_number = random.randint(0, len(array_of_colors) - 1)
        self.label_button.config(fg=array_of_colors[random_number])


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
