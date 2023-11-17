from lib.my_tracks import *

def test_no_tracks_added():
    music_tracks = my_tracks()
    assert music_tracks.show_tracks() == []

def test_one_track_added():
    music_tracks = my_tracks()
    music_tracks.add_track("track1")
    assert music_tracks.show_tracks() == ["track1"]

def test_multiple_tracks_added():
    music_tracks = my_tracks()
    music_tracks.add_track("track1")
    music_tracks.add_track("track2")
    music_tracks.add_track("track3")
    music_tracks.add_track("track4")
    music_tracks.add_track("track5")
    music_tracks.add_track("track6")
    music_tracks.add_track("track7")
    music_tracks.add_track("track8")
    music_tracks.add_track("track9")
    music_tracks.add_track("track10")
    assert music_tracks.show_tracks() == ["track1","track2","track3","track4","track5","track6","track7","track8","track9","track10"]