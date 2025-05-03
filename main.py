import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

INITIAL_LIVES = lives = 6

mystery_word = "apple tree"
display_word = ["_" if char.isalpha() else char for char in mystery_word]
game_over = False
btns = []


LETTERS = {
    1: ('a','b','c','d','e','f'),
    2: ('g','h','i','j','k','l'),
    3: ('m','n','o','p','q','r'),
    4: ('s','t','u','v','w','x'),
    5: ('','','y','z','','')
}


def check_letter_in_word(letter):
    if letter in mystery_word:
        update_display(letter)
    else:
        draw_hangman()

    has_won()


def update_display(letter):
    for i in range(len(mystery_word)):
        if mystery_word[i] == letter:
            display_word[i] = letter

    word_display_label.configure(text=" ".join(display_word))


def has_won():
    global game_over
    if "_" not in display_word:
        tk.messagebox.showinfo("Info", "Congratulations!!! You have guessed the word!")
        game_over = True
    if lives == 0:
        tk.messagebox.showerror("Error", f"Game Over! The word was {mystery_word}")
        game_over = True
    if game_over:
        for btn in btns:
            btn.configure(state=ctk.DISABLED)


def on_button_click(letter, btn):
    check_letter_in_word(letter)
    btn.configure(state=ctk.DISABLED)


def draw_hangman():
    global lives
    global my_image

    lives -= 1   
    lives_label.configure(text=f"Lives: {lives}")
    
    my_image = ctk.CTkImage(dark_image=Image.open(F"image{INITIAL_LIVES-lives}.jpg"), size=(110,150))
    my_label.configure(image=my_image)
    my_label.image = my_image


root = ctk.CTk()
root.geometry("550x500")
root.title("Hangman")

frame =ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text='Hangman', font=('Arial', 24))
title.pack(pady=12, padx=10)

my_label = ctk.CTkLabel(frame, text="", image="")
my_label.pack(pady=20)
my_image = ctk.CTkImage(dark_image=Image.open("blank_image.jpg"), size=(110,150))
my_label.configure(image=my_image)
my_label.image = my_image

lives_label = ctk.CTkLabel(frame, text=f"Lives: {lives}", font=("Arial", 14))
lives_label.pack()

word_display_label = ctk.CTkLabel(frame, text=" ".join(display_word), font=("Arial", 14))
word_display_label.pack()


MAX_COLUMNS = 6
MAX_ROWS = 5
keyboard_frame = ctk.CTkFrame(root)
for i in range(0, MAX_COLUMNS):
    keyboard_frame.columnconfigure(i, weight=1)

for row in range(1, MAX_ROWS+1):
    for col in range(0, MAX_COLUMNS):
        letter = LETTERS[row][col]
        if letter.isalpha():
            btn = ctk.CTkButton(
                keyboard_frame, 
                text=f"{letter}", 
                font=("Arial", 18), 
            )
        else:
            continue
        
        btn.grid(row=row, column=col, sticky=ctk.W+ctk.E)
        btn.configure(command = lambda l=letter, b=btn : on_button_click(l, b))
        btns.append(btn)

keyboard_frame.pack(fill='x')

root.mainloop()