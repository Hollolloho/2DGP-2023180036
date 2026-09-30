import os
from pico2d import *
# 파일이 위치한 폴더로 작업 경로 강제 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here

def draw_chracter(x, y, frame):
    clear_canvas()
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    delay(0.01)

def character_left():
    for x in range(0, 800, 2):
        frame = (x +1) % 8
        draw_chracter(x, 90, frame )
def character_right():
    for x in range(800, 0, -2):
        frame = (x +1) % 8
        draw_chracter(x, 90, frame )
def character_left_run():

    pass
def character_right_run():
    pass


while True:
    grass.draw(400, 30)

    character_right()
    character_left()
    character_left_run()
    character_right_run()

close_canvas()

