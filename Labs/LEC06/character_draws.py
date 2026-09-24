# 실습 과제 진행

from pico2d import *
from math import *

open_canvas(1200, 800)

angle = 0
x = 600
y = 400

right = True
up = False
left = False
Down = False

def move_circle():
    global angle, x, y
    clear_canvas()
    character.draw(x, y)

    angle = angle + 1

    x = 600 + 200 * cos(radians(angle))
    y = 400 + 200 * sin(radians(angle))

    update_canvas()
    delay(0.01)

def move_rectangle():
    global x, y
    global right, up, left, Down

    clear_canvas()
    character.draw(x, y)

    if right:
        x = x + 2
        if x >= 800:
            right = False
            up = True  

    if up:
        y = y + 2
        if y >= 650:
            up = False
            left = True
    
    update_canvas()
    delay(0.01)

def move_triangle():
    clear_canvas()
    character.draw(600, 400)
    update_canvas()
    print("TRIANGLE")



character = load_image('character.png')

while True:
    #move_circle()
    move_rectangle()
    #move_triangle()

close_canvas()
