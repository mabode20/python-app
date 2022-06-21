import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk() #base of the app

canvas = tk.Canvas(root, height=700, width=700, bg="#264D42")
canvas.pack()

frame = tk.Frame(root, bg="yellow")
frame.place(relwidth=0.8, relheight=0.8)

root.mainloop()
