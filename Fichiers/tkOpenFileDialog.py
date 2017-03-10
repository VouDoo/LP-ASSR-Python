import tkinter as tk
from tkinter import filedialog

root = tk.Tk().withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
