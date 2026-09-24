# 실습 과제 진행

from pico2d import *
from math import *

open_canvas(1200, 800)

character = load_image('character.png')

def move_circle():
    clear_canvas()
    character.draw(600, 400)


    update_canvas()
    print("CIRCLE")
    pass

def move_rectangle():
    clear_canvas()
    character.draw(600, 400)
    update_canvas()
    print("RECTANGLE")
    pass

def move_triangle():
    clear_canvas()
    character.draw(600, 400)
    update_canvas()
    print("TRIANGLE")
    pass   

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
