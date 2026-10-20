from pico2d import *
from math import *

open_canvas(800, 600)
character = load_image('character.png')
grass = load_image('grass.png')

x = 400
y = 300
angle = 0

while True:
    clear_canvas()
    character.draw(x, y)
    update_canvas()

    angle += 1

    angle = angle % 360

    x = 400 + 200 * cos(radians(angle))
    y = 300 + 200 * sin(radians(angle))


    delay(0.01)

close_canvas()