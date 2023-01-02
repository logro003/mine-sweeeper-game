import settings

def frame_height(percent_of_window):
    return settings.WINDOW_HEGIHT*(percent_of_window/100)

def frame_width(percent_of_window):
    return settings.WINDOW_WIDTH*(percent_of_window/100)

def button_width(frame_width):
    return int(frame_width*0.05/settings.GRID_SIZE)

def button_height(frame_height):
    return int(frame_height*0.05/settings.GRID_SIZE)