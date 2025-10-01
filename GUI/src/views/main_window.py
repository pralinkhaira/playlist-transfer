import tkinter as tk
from tkinter import messagebox
from views.components.auth_form import AuthForm
from views.components.playlist_form import PlaylistForm

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Bidirectional Playlist Transfer: Spotify ⇄ YouTube Music")
        self.master.geometry("700x550")

        self.auth_form = AuthForm(self.master)
        self.auth_form.pack(pady=20)

        self.playlist_form = PlaylistForm(self.master)
        self.playlist_form.pack(pady=20)

        self.start_transfer_button = tk.Button(
            self.master,
            text="Start Transfer",
            command=self.start_transfer,
            bg="blue",
            fg="white",
            font=("Arial", 11, "bold")
        )
        self.start_transfer_button.pack(pady=20)

    def start_transfer(self):
        # Logic to initiate the transfer process
        if self.auth_form.validate() and self.playlist_form.validate():
            # Call the transfer logic from the controller
            messagebox.showinfo("Success", "Transfer initiated!")
        else:
            messagebox.showerror("Error", "Please fill in all required fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()