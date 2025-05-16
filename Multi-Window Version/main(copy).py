import customtkinter as ctk
from main_menu import MainMenu
from game_window import GameWindow

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()    
root.geometry("500x300")
root.resizable(False, False)
root.title("Hangman Client")

if __name__ == "__main__":
    try:
        app = MainMenu(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

