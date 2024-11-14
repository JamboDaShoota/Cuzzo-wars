
def map_value(value, from_min, from_max, to_min, to_max):
    # Maps a value from one range to another
    return to_min + (value - from_min) * (to_max - to_min) / (from_max - from_min)

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))
