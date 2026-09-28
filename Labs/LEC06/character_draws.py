# 실습 과제 진행

from pico2d import *
from math import *

open_canvas(1200, 800)

def draw_character(x,y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)

def draw_circle():
    for angle in range(0, 360, 5):
        x = 600 + 200 * cos(radians(angle))
        y = 400 + 200 * sin(radians(angle))
        draw_character(x, y)

def move_top():
    for x in range(50, 750, 5):
        draw_character(x, 550)

def move_right():
    for y in range(550, 50, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 50, -5):
        draw_character(x, 50)

def move_left():
    for y in range(50, 550, 5):
        draw_character(50, y)

def draw_rectangle():
    print("RECTANGLE")

    clear_canvas()

    move_top()
    move_right()
    move_bottom()
    move_left()

    update_canvas()
    pass

def draw_triangle():
    clear_canvas()
    character.draw(600, 400)
    update_canvas()
    print("TRIANGLE")
    pass   



character = load_image('character.png')

while True:
    #draw_circle()
    draw_rectangle()
    #draw_triangle()

close_canvas()

