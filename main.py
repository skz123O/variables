def on_button_pressed_a():
    global counting
    counting += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global counting
    counting = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counting
    counting += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

counting = 0
counting = 0