import tkinter as tk
from tkinter import filedialog


def select_folder():
    folder_path = filedialog.askdirectory()
    print("Выбрана папка:", folder_path)


root = tk.Tk()
root.withdraw()  # Скрыть основное окно

select_folder()
