class my_tracks():
    def __init__(self):
        self._tracks = []

    def add_track(self, text):
        self._tracks.append(text)

    def show_tracks(self):
        return self._tracks
