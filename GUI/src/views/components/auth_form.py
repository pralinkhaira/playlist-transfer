import tkinter as tk
from tkinter import messagebox

class AuthForm:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="🎧 Spotify Authentication", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(self.frame, text="Client ID").grid(row=1, column=0, sticky="w")
        self.client_id_entry = tk.Entry(self.frame, width=60)
        self.client_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Client Secret").grid(row=2, column=0, sticky="w")
        self.client_secret_entry = tk.Entry(self.frame, width=60, show="*")
        self.client_secret_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Redirect URI (optional)").grid(row=3, column=0, sticky="w")
        self.redirect_uri_entry = tk.Entry(self.frame, width=60)
        self.redirect_uri_entry.insert(0, "http://localhost:8888/callback")
        self.redirect_uri_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="📄 YTMusic Auth File (e.g., headers_auth.json)", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w")
        self.yt_auth_entry = tk.Entry(self.frame, width=60)
        self.yt_auth_entry.insert(0, "headers_auth.json")
        self.yt_auth_entry.grid(row=4, column=1)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit, bg="blue", fg="white", font=("Arial", 11, "bold"))
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    def submit(self):
        client_id = self.client_id_entry.get().strip()
        client_secret = self.client_secret_entry.get().strip()
        redirect_uri = self.redirect_uri_entry.get().strip()
        yt_auth_file = self.yt_auth_entry.get().strip()

        if not client_id or not client_secret or not yt_auth_file:
            messagebox.showerror("Missing Input", "Please fill all required fields.")
            return

        # Here you would typically handle the authentication logic
        messagebox.showinfo("Success", "Authentication details submitted successfully!")