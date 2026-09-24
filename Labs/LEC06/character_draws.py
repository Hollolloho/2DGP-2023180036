# 실습 과제 진행

from pico2d import *
from math import *

open_canvas(1200, 800)

angle = 0
x = 600
y = 400

def move_circle():
    global angle, x, y
    clear_canvas()
    character.draw(x, y)
    
    delay(0.01)
    update_canvas()

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



character = load_image('character.png')

while True:
    move_circle(angle, x, y)
    #move_rectangle()
    #move_triangle()

close_canvas()
