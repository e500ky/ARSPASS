import random
from tkinter import messagebox
from tkinter.font import BOLD
from customtkinter import *
import json

set_default_color_theme("green")

class PassCreator(CTk):
    def __init__(self):
        super().__init__()
        self.title("ARSPASS")
        self.setAppSize()
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.window()

    def setAppSize(self):
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        self.appWidth = int(self.screenWidth /5*1.125)
        self.appHeight = int(self.screenHeight /5*2.5)

        self.geometry(f"{self.appWidth}x{self.appHeight}+{int((self.screenWidth - self.appWidth) / 2)}+{int((self.screenHeight - self.appHeight) / 2)}")

    def load(self):
        set_appearance_mode(self.loadJson("theme"))

        self.es_dif += 1

        self.after(self.es_dif, self.load)

    def loadJson(self, configure_):
        with open('config.json', 'r') as f:
            self.config = json.load(f)

            self.getConfig = {
                "font.family": self.config["font.family"],
                "theme": self.config["theme"],
                "theme.color": self.config["theme.color"]
            }

            f.close()

            return self.getConfig[configure_]

    def window(self):
        self.header = CTkLabel(self, text="ARSPASS", font=(self.loadJson("font.family"), 60, BOLD))
        self.header.pack(pady=(50, 0))

        self.description = CTkLabel(self, text="Password Creator", font=(self.loadJson("font.family"), 25), text_color="#777")
        self.description.pack(pady=(0, 60))

        self.difficulty = CTkFrame(self, corner_radius=10)
        self.difficulty.pack(pady=(10, 10), expand=False, fill=X, padx=(20, 20))

        self.dif_text = "Medium"

        self.difficulty_label = CTkLabel(self.difficulty, text=f"Difficulty Level: {self.dif_text}", font=(self.loadJson("font.family"), 18))
        self.difficulty_label.pack(side=TOP, anchor="w", padx=20, pady=(20, 15))

        self.difficulty_options = ["Hard", "Medium", "Easy"]
        self.difficulty_var = StringVar()
        self.difficulty_var.set(self.difficulty_options[1])

        self.eno = CTkLabel(self.difficulty, text="", height=15)
        self.eno.pack(fill=X, padx=20, side=BOTTOM)

        self.difficulty_buttons = [CTkRadioButton(self.difficulty, text=difficulty, font=(self.loadJson("font.family"), 16), variable=self.difficulty_var, value=difficulty).pack(fill=X, side=BOTTOM, padx=20, pady=(5, 5)) for difficulty in self.difficulty_options]

        self.es_dif = 0
        self.updateDifficulity()

        self.lenght = CTkFrame(self, corner_radius=10)
        self.lenght.pack(pady=(10, 0), expand=False, fill=X, padx=(20, 20))
        
        self.pass_lenght = 6
        self.length_label = CTkLabel(self.lenght, text=f"Password Length: {str(self.pass_lenght)}", font=(self.loadJson("font.family"), 18))
        self.length_label.pack(side=TOP, anchor="w", padx=20, pady=(20, 15))

        self.length_spinbox = CTkSlider(self.lenght, from_=6, to=36, number_of_steps=10)
        self.length_spinbox.pack(fill=X, padx=20, pady=(5, 20))
        self.length_spinbox.bind("<Motion>", lambda event: (self.length_label.configure(text=f"Password Length: {str(int(self.length_spinbox.get()))}")))
        self.length_spinbox.set(6)

        self.password_entry = CTkEntry(self, font=(self.loadJson("font.family"), 18), text_color="#777", justify="center", border_width=1, height=40, corner_radius=10, placeholder_text="PASSWORD", state="normal")
        self.password_entry.pack(pady=(20, 0), fill=X, padx=20)
        self.password_entry.configure(state="disabled")
        self.password_entry.bind("<Button-1>", lambda event:self.copy())

        self.generate_button = CTkButton(self, text="Generate Password", font=(self.loadJson("font.family"), 18), command=self.generatePassword, corner_radius=10, height=40)
        self.generate_button.pack(pady=(20, 30), fill=X, padx=120)

        self.copyright = CTkLabel(self, text=f"Copyright © 2024 ArsTech. All rights reserved.", font=(self.loadJson("font.family"), 12), text_color="#777")
        self.copyright.pack(pady=(20, 0))

        self.load()

    def copy(self):
        if self.password_entry.get() != None and self.password_entry.get() != "":
            self.password_entry.configure(state="normal", border_width=0)
            self.password_entry.select_range(0, END)
            self.password_entry.clipboard_clear()
            self.password_entry.clipboard_append(self.password_entry.get())
            self.password_entry.configure(state="disabled", border_width=1)
            messagebox.showinfo("Copy Password", "Password copied successfully.\n\nPassword: {0}".format(self.password_entry.get()))

    def updateLenght(self):
        self.length_label.configure(text=f"Password Length: {str(self.length_spinbox.get())}")

        self.es_dif += 1

        self.after(self.es_dif, self.updateLenght)

    def updateDifficulity(self):
        self.dif_text = self.difficulty_var.get()
        self.difficulty_label.configure(text=f"Difficulty Level: {self.difficulty_var.get()}")

        self.es_dif += 1

        self.difficulty_label.after(self.es_dif, self.updateDifficulity)

    def generatePassword(self):
        self.password_entry.configure(state="normal")
        difficulty = self.difficulty_var.get()
        lenght = self.length_spinbox.get()

        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        uppercase_letters = lowercase_letters.upper()
        digits = "0123456789"
        special_characters = """!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"""

        if difficulty == "Hard":
            characters = lowercase_letters + uppercase_letters + digits + special_characters
        elif difficulty == "Medium":
            characters = lowercase_letters + uppercase_letters + digits
        else:
            characters = lowercase_letters + uppercase_letters

        password = "".join(random.choice(characters) for _ in range(int(lenght)))

        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        self.password_entry.configure(state="disabled")

if __name__ == "__main__":
    app = PassCreator()
    app.mainloop()