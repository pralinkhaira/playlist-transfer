import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

class SpotifyService:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.sp = None

    def authenticate(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope='playlist-modify-public'
        ))

    def fetch_playlists(self):
        if not self.sp:
            raise Exception("Spotify service not authenticated.")
        return self.sp.current_user_playlists()

    def add_track_to_playlist(self, playlist_id, track_uri):
        if not self.sp:
            raise Exception("Spotify service not authenticated.")
        self.sp.playlist_add_items(playlist_id, [track_uri])

    def get_playlist_tracks(self, playlist_id):
        if not self.sp:
            raise Exception("Spotify service not authenticated.")
        results = self.sp.playlist_tracks(playlist_id)
        return [item['track'] for item in results['items']]