import pygame
import tkinter as tk
from tkinter import ttk

def load_gui(app):
    app.root.title("Annoying as hell")
    app.root.geometry('500x300')
    app.root.configure(bg='lightblue')

    pygame.mixer.init()
    pygame.mixer.set_num_channels(20)

    style = ttk.Style()
    style.configure("TButton", font=('Arial', 20), background='green')

    app.treeview = ttk.Treeview(app.root, columns=('File', 'Duration'), show='headings')
    app.treeview.column('File', width=200, anchor='w')
    app.treeview.column('Duration', width=100, anchor='w')
    app.treeview.heading('File', text='File')
    app.treeview.heading('Duration', text='Duration')
    app.treeview.pack(side=tk.LEFT, fill=tk.BOTH)

    app.volume_scale = tk.Scale(app.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Volume")
    app.volume_scale.set(0.5)
    app.volume_scale.pack()

    app.add_button = ttk.Button(app.root, text="Add Sound", command=app.add_sound)
    app.remove_button = ttk.Button(app.root, text="Remove Sound", command=app.remove_sound)
    app.clear_button = ttk.Button(app.root, text="Clear All", command=app.clear_sounds)
    app.toggle_listener = ttk.Button(app.root, text="Start", command=app.toggle_listening)

    app.add_button.pack(pady=10)
    app.remove_button.pack(pady=10)
    app.clear_button.pack(pady=10)
    app.toggle_listener.pack(pady=10)
