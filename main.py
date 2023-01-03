def on_button_pressed_a():
    global vTime
    vTime = vTime + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global vTime
    while vTime > 0:
        basic.pause(1000)
        vTime = vTime - 1
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

vTime = 0
vTime = 0

def on_forever():
    basic.show_number(vTime)
basic.forever(on_forever)
