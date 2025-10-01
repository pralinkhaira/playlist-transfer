import tkinter as tk
from tkinter import messagebox

class PlaylistForm:
    def __init__(self, master, transfer_callback):
        self.master = master
        self.transfer_callback = transfer_callback
        
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Enter Playlist Link or ID:")
        self.label.pack()

        self.playlist_entry = tk.Entry(self.frame, width=60)
        self.playlist_entry.pack(pady=(5, 10))

        self.transfer_button = tk.Button(self.frame, text="Start Transfer", command=self.initiate_transfer, bg="blue", fg="white")
        self.transfer_button.pack()

    def initiate_transfer(self):
        playlist_input = self.playlist_entry.get().strip()
        if not playlist_input:
            messagebox.showerror("Input Error", "Please enter a playlist link or ID.")
            return
        self.transfer_callback(playlist_input)

    def clear(self):
        self.playlist_entry.delete(0, tk.END)