# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class_name = my_tracks
takes no inital parameters

method_name = add_track
parameters = 1 string that has the name of the track

method_name = show_tracks
parameters none
returns a list of tracks

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

def test_no_tracks_added():
    music_tracks = my_tracks()
    music_tracks.show_tracks() == []


def test_one_track_added():
    music_tracks = my_tracks()
    music_tracks.add_track("track1")
    music_tracks.show_tracks() == ["track1"]


def test_multiple_tracks_added
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
    music_tracks.show_tracks() == ["track1","track2","track3","track4","track5","track6","track7","track8","track9","track10"]



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

