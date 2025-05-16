import customtkinter as ctk
from game_window import GameWindow
import tkinter as tk


class MainMenu:
    root = ''

    def __init__(self, root):
        self.root = root
        self.categories = ["Countries", "Animals", "Food"]
        self.create_ui()

    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self.frame, text='Welcome to Hangman!', font=('Arial', 24))
        self.title.pack(pady=12, padx=10)

        self.combo_box = ctk.CTkComboBox(master=self.frame, values=self.categories, width=240, height=35, font=("Arial", 14), state="readonly")
        self.combo_box.set("Select Category")
        self.combo_box.pack(pady=12, padx=10)

        self.play_button = ctk.CTkButton(master=self.frame, text="Play Game", command=self.select_category)
        self.play_button.pack(pady=20)


    def select_category(self):
        value = self.combo_box.get()

        if value == "Select Category":
            tk.messagebox.showerror("Error", "Please select a category.")
            return

        selected_category = self.combo_box.get()
        GameWindow(selected_category, self.root)
        