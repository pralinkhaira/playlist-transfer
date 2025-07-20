import tkinter as tk
from tkinter import messagebox
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from ytmusicapi import YTMusic
import re

# GUI Setup
root = tk.Tk()
root.title("Bidirectional Playlist Transfer: Spotify ⇄ YouTube Music")
root.geometry("700x550")

# --- Input Sections ---
tk.Label(root, text="🎧 Spotify Authentication", font=("Arial", 12, "bold")).pack(pady=(10, 0))
tk.Label(root, text="Client ID").pack()
client_id_entry = tk.Entry(root, width=60)
client_id_entry.pack()

tk.Label(root, text="Client Secret").pack()
client_secret_entry = tk.Entry(root, width=60, show="*")
client_secret_entry.pack()

tk.Label(root, text="Redirect URI (optional)").pack()
redirect_uri_entry = tk.Entry(root, width=60)
redirect_uri_entry.insert(0, "http://localhost:8888/callback")
redirect_uri_entry.pack()

tk.Label(root, text="📄 YTMusic Auth File (e.g., headers_auth.json)", font=("Arial", 12, "bold")).pack(pady=(15, 0))
yt_auth_entry = tk.Entry(root, width=60)
yt_auth_entry.insert(0, "headers_auth.json")
yt_auth_entry.pack()

tk.Label(root, text="🎵 Playlist Transfer", font=("Arial", 12, "bold")).pack(pady=(15, 0))
direction_var = tk.StringVar(value="spotify_to_yt")
tk.Radiobutton(root, text="Spotify ➞ YouTube Music", variable=direction_var, value="spotify_to_yt").pack()
tk.Radiobutton(root, text="YouTube Music ➞ Spotify", variable=direction_var, value="yt_to_spotify").pack()

tk.Label(root, text="Enter Playlist Link or ID:").pack(pady=(5, 0))
playlist_entry = tk.Entry(root, width=60)
playlist_entry.pack()

# --- Logic Functions ---
def extract_spotify_id(link):
    match = re.search(r'playlist/([a-zA-Z0-9]+)', link)
    return match.group(1) if match else link

def transfer():
    client_id = client_id_entry.get().strip()
    client_secret = client_secret_entry.get().strip()
    redirect_uri = redirect_uri_entry.get().strip()
    yt_auth_file = yt_auth_entry.get().strip()
    playlist_input = playlist_entry.get().strip()
    direction = direction_var.get()

    if not client_id or not client_secret or not yt_auth_file or not playlist_input:
        messagebox.showerror("Missing Input", "Please fill all required fields.")
        return

    try:
        if direction == "spotify_to_yt":
            playlist_id = extract_spotify_id(playlist_input)
            sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret
            ))
            results = sp.playlist_tracks(playlist_id)
            tracks = []
            for item in results['items']:
                track = item['track']
                tracks.append(f"{track['name']} {track['artists'][0]['name']}")

            ytmusic = YTMusic(yt_auth_file)
            yt_playlist_id = ytmusic.create_playlist("Imported from Spotify", "Transferred via Script")
            for track in tracks:
                search_results = ytmusic.search(track, filter="songs")
                if search_results:
                    video_id = search_results[0]["videoId"]
                    ytmusic.add_playlist_items(yt_playlist_id, [video_id])
            messagebox.showinfo("Success", "Playlist transferred to YouTube Music!")

        elif direction == "yt_to_spotify":
            ytmusic = YTMusic(yt_auth_file)
            playlist = ytmusic.get_playlist(playlist_input, limit=100)
            tracks = [f"{track['title']} {track['artists'][0]['name']}" for track in playlist['tracks']]

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope='playlist-modify-public'
            ))
            user_id = sp.current_user()['id']
            sp_playlist = sp.user_playlist_create(user_id, "Imported from YT Music", public=True)

            track_uris = []
            for track in tracks:
                result = sp.search(q=track, limit=1, type='track')
                if result['tracks']['items']:
                    uri = result['tracks']['items'][0]['uri']
                    track_uris.append(uri)

            sp.playlist_add_items(sp_playlist['id'], track_uris)
            messagebox.showinfo("Success", "Playlist transferred to Spotify!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# --- Transfer Button ---
tk.Button(root, text="Start Transfer", command=transfer, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=20)
tk.Label(root, text="Ensure you've run YTMusic.setup() once before using headers_auth.json", fg="gray").pack(pady=10)
tk.Label(root, text="Made with ❤️ by Pralin", font=("Arial", 10), fg="red").pack(pady=(10, 20))

root.mainloop()


root.mainloop()
