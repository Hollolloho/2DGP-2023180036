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

# IDLE 대기 스프라이트 시트 로드
idle_sheet = load_image('_spritesheet_IDLE.png')

# IDLE 대기 프레임 데이터 (10프레임)
IDLE_FRAMES = [
    {'left': 2, 'bottom': 0, 'width': 92, 'height': 239, 'offset_x': -1.0},
    {'left': 100, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5},
    {'left': 198, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5},
    {'left': 296, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5},
    {'left': 394, 'bottom': 0, 'width': 94, 'height': 240, 'offset_x': 0.0},
    {'left': 492, 'bottom': 0, 'width': 94, 'height': 241, 'offset_x': 0.0},
    {'left': 590, 'bottom': 0, 'width': 94, 'height': 241, 'offset_x': 0.0},
    {'left': 688, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5},
    {'left': 786, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5},
    {'left': 884, 'bottom': 0, 'width': 93, 'height': 240, 'offset_x': -0.5}
]

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
