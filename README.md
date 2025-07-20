# 🎵 Bidirectional Playlist Transfer Tool: Spotify ⇄ YouTube Music

A user-friendly Python GUI tool that allows you to transfer playlists seamlessly between **Spotify** and **YouTube Music**. Powered by `spotipy` and `ytmusicapi`, this tool simplifies the cross-platform music experience.

## 🚀 Features

- Transfer Spotify playlists to YouTube Music
- Transfer YouTube Music playlists to Spotify
- Clean, easy-to-use Tkinter GUI
- Separate input sections for playlist links and auth credentials
- Error handling and user feedback via popups

## 📦 Requirements

- Python 3.7+
- Spotipy
- ytmusicapi
- Tkinter (pre-installed with standard Python distributions)

Install required packages:
```bash
pip install spotipy ytmusicapi
````

## 🔐 Authentication Setup

### Spotify

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Create a new app and copy:

   * `Client ID`
   * `Client Secret`
3. Set a redirect URI like `http://localhost:8888/callback`.

### YouTube Music

1. Run:

   ```python
   from ytmusicapi import YTMusic
   YTMusic.setup()
   ```
2. This will generate `headers_auth.json` which is required to authenticate.

## 🖥️ How to Use

1. Run the Python script:

   ```bash
   python main.py
   ```
2. Choose the direction of transfer:

   * **Spotify ➞ YouTube Music**
   * **YouTube Music ➞ Spotify**
3. Enter the Playlist Link or ID.
4. Provide the required credentials in the input fields:

   * Spotify Client ID, Secret, Redirect URI
   * Path to `headers_auth.json`
5. Click **"Start Transfer"**.
6. Done! 🎉

## 📌 Notes

* This tool does not support private playlists unless proper scopes and permissions are set.
* Ensure your `headers_auth.json` is valid and up to date.

## 📸 Screenshots

![GUI Screenshot Placeholder](#) *(screenshot soon)*

## 🛠️ Contributing

Pull requests are welcome! Feel free to fork and enhance the functionality or UI.

## 📝 License

MIT License

---

> Made with ❤️ by Pralin Khaira
