import tkinter as tk
import customtkinter as ctk
import tkkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import random


class GameWindow:
    INITIAL_LIVES = lives = 6

    LETTERS = {
        1: ('a','b','c','d','e','f'), 
        2: ('g','h','i','j','k','l'),
        3: ('m','n','o','p','q','r'),
        4: ('s','t','u','v','w','x'),
        5: ('','','y','z','','')
    }

    game_over = False

    def __init__(self, category, root, dimensions="550x500"):
        self.category = category
        self.root = root
        self.dimensions = dimensions
        self.generate_random_word()
        self.create_ui()


    def generate_random_word(self):
        with open(f"{self.category}.txt") as f:
            random_words = [word.strip() for word in f.readlines()]
            GameWindow.mystery_word = random.choice(random_words)
            GameWindow.display_word = ["_" if char.isalpha() else char for char in GameWindow.mystery_word]
            GameWindow.game_over = False
            GameWindow.btns = []


    def check_letter_in_word(self, letter):
        if letter in GameWindow.mystery_word:
            self.update_display(letter)
        else:
            self.draw_hangman()

        self.has_won()


    def update_display(self, letter):
        for i in range(len(GameWindow.mystery_word)):
            if GameWindow.mystery_word[i] == letter:
                GameWindow.display_word[i] = letter

        word_display_label.configure(text=" ".join(GameWindow.display_word))

    
    def has_won(self):
        if "_" not in GameWindow.display_word:
            tk.messagebox.showinfo("Info", "Congratulations!!! You have guessed the word!")
            game_over = True
        if GameWindow.lives == 0:
            tk.messagebox.showerror("Error", f"Game Over! The word was {GameWindow.mystery_word}")
            GameWindow.game_over = True
        if GameWindow.game_over:
            for btn in GameWindow.btns:
                btn.configure(state=ctk.DISABLED)


    def on_button_click(self, letter, btn):
        self.check_letter_in_word(letter)
        btn.configure(state=ctk.DISABLED)


    def draw_hangman(self):
        global lives
        global my_image

        GameWindow.lives -= 1   
        lives_label.configure(text=f"Lives: {GameWindow.lives}")
        my_image = ctk.CTkImage(dark_image=Image.open(f"image{GameWindow.INITIAL_LIVES - GameWindow.lives}.jpg"), size=(110,150))
        my_label.configure(image=my_image)
        my_label.image = my_image


    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        global my_label
        global lives_label
        global word_display_label

        self.game_window = ctk.CTkToplevel(self.root)
        self.game_window.geometry(self.dimensions)
        self.game_window.title("Hangman Client")

        frame =ctk.CTkFrame(master=self.game_window)
        frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        title = ctk.CTkLabel(master=frame, text='Hangman', font=('Arial', 24))
        title.pack(pady=12, padx=10)
        
        my_label = ctk.CTkLabel(frame, text="", image="")
        my_label.pack(pady=20)
        my_image = ctk.CTkImage(dark_image=Image.open("blank_image.jpg"), size=(110,150))
        my_label.configure(image=my_image)
        my_label.image = my_image
        
        lives_label = ctk.CTkLabel(frame, text=f"Lives: {GameWindow.lives}", font=("Arial", 14))
        lives_label.pack()
        
        word_display_label = ctk.CTkLabel(frame, text=" ".join(GameWindow.display_word), font=("Arial", 14))
        word_display_label.pack()

        self.create_keyboard(self.game_window)


    def create_keyboard(self, root):
        MAX_COLUMNS = 6
        MAX_ROWS = 5
        keyboard_frame = ctk.CTkFrame(root)
        for i in range(0, MAX_COLUMNS):
            keyboard_frame.columnconfigure(i, weight=1)
        
        for row in range(1, MAX_ROWS+1):
            for col in range(0, MAX_COLUMNS):
                letter = GameWindow.LETTERS[row][col]
                if letter.isalpha():
                    btn = ctk.CTkButton(
                        keyboard_frame, 
                        text=f"{letter}", 
                        font=("Arial", 18), 
                    )
                else:
                    continue
                
                btn.grid(row=row, column=col, sticky=ctk.W+ctk.E)
                btn.configure(command = lambda l=letter, b=btn : self.on_button_click(l, b))
                GameWindow.btns.append(btn)
        
        keyboard_frame.pack(fill='x')



        
