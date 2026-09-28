# 실습 과제 진행

from pico2d import *
from math import *

open_canvas(1200, 800)

angle = 0
x = 600
y = 400

def draw_character(x,y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)


def move_top():
    print("top")
    pass

def move_right():
    print("right")
    pass

def move_bottom():
    print("bottom")
    pass

def move_left():
    print("left")
    pass


def draw_circle():
    global angle, x, y
    clear_canvas()
    character.draw(x, y)

    angle = angle + 1

    x = 600 + 200 * cos(radians(angle))
    y = 400 + 200 * sin(radians(angle))

    update_canvas()
    delay(0.01)

def draw_rectangle():
    clear_canvas()

    move_top()
    move_right()
    move_bottom()
    move_left()

    update_canvas()
    print("RECTANGLE")
    pass

def draw_triangle():
    clear_canvas()
    character.draw(600, 400)
    update_canvas()
    print("TRIANGLE")
    pass   



character = load_image('character.png')

while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()

close_canvas()
