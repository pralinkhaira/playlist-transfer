import json
from ytmusicapi import YTMusic

class YouTubeService:
    def __init__(self, auth_file):
        self.ytmusic = YTMusic(auth_file)

    def create_playlist(self, title, description):
        return self.ytmusic.create_playlist(title, description)

    def add_tracks_to_playlist(self, playlist_id, track_ids):
        self.ytmusic.add_playlist_items(playlist_id, track_ids)

    def search_track(self, query):
        return self.ytmusic.search(query, filter='songs')