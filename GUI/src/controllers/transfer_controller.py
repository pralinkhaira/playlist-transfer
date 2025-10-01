class TransferController:
    def __init__(self, spotify_service, youtube_service):
        self.spotify_service = spotify_service
        self.youtube_service = youtube_service

    def transfer_to_youtube(self, playlist_id, client_id, client_secret, yt_auth_file):
        tracks = self.spotify_service.get_playlist_tracks(playlist_id, client_id, client_secret)
        yt_playlist_id = self.youtube_service.create_playlist("Imported from Spotify", "Transferred via Script")
        for track in tracks:
            video_id = self.youtube_service.search_track(track)
            if video_id:
                self.youtube_service.add_track_to_playlist(yt_playlist_id, video_id)

    def transfer_to_spotify(self, yt_playlist_id, client_id, client_secret, redirect_uri):
        tracks = self.youtube_service.get_playlist_tracks(yt_playlist_id)
        sp_playlist_id = self.spotify_service.create_playlist("Imported from YT Music", client_id, client_secret, redirect_uri)
        for track in tracks:
            uri = self.spotify_service.search_track(track)
            if uri:
                self.spotify_service.add_track_to_playlist(sp_playlist_id, uri)