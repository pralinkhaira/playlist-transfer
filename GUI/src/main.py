import tkinter as tk
from views.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Bidirectional Playlist Transfer: Spotify ⇄ YouTube Music")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()