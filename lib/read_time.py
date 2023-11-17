

def read_time(string1, reading_speed):
    words = len(string1.split())
    mins = words // reading_speed
    secs = 0.0
    secs = words % reading_speed
    secs = (secs / reading_speed) * 60
    return f"{mins} minniets and {secs} seconds"
