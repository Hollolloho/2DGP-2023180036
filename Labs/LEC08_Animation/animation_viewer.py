import os
from pico2d import *

# 작업 경로를 현재 파일 위치로 변경하여 상대 경로 이미지 로드 보장
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# 확대 배율 설정
SCALE = 1.6

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True

def check_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

close_canvas()
