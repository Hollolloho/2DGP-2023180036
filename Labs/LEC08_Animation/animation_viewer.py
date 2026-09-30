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

# 스프라이트 시트 개별 로드
idle_sheet = load_image('_spritesheet_IDLE.png')
walk_sheet = load_image('_spritesheet_WALK.png')
run_sheet = load_image('_spritesheet_RUN.png')

# IDLE 대기 프레임 데이터
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

# WALK 걷기 프레임 데이터
WALK_FRAMES = [
    {'left': 0, 'bottom': 1, 'width': 106, 'height': 239, 'offset_x': -1.5},
    {'left': 117, 'bottom': 0, 'width': 89, 'height': 242, 'offset_x': -2.0},
    {'left': 238, 'bottom': 2, 'width': 80, 'height': 241, 'offset_x': 5.5},
    {'left': 342, 'bottom': 0, 'width': 89, 'height': 244, 'offset_x': 5.0},
    {'left': 445, 'bottom': 0, 'width': 94, 'height': 244, 'offset_x': 1.5},
    {'left': 557, 'bottom': 1, 'width': 87, 'height': 243, 'offset_x': 1.0},
    {'left': 679, 'bottom': 0, 'width': 73, 'height': 241, 'offset_x': 7.0},
    {'left': 780, 'bottom': 1, 'width': 82, 'height': 238, 'offset_x': 3.5}
]

# RUN 달리기 프레임 데이터 (10프레임)
RUN_FRAMES = [
    {'left': 1, 'bottom': 5, 'width': 197, 'height': 233, 'offset_x': -7.0},
    {'left': 253, 'bottom': 0, 'width': 118, 'height': 245, 'offset_x': -7.5},
    {'left': 495, 'bottom': 5, 'width': 77, 'height': 242, 'offset_x': 1.0},
    {'left': 705, 'bottom': 4, 'width': 95, 'height': 238, 'offset_x': 7.0},
    {'left': 889, 'bottom': 14, 'width': 144, 'height': 226, 'offset_x': 2.5},
    {'left': 1094, 'bottom': 34, 'width': 183, 'height': 205, 'offset_x': 14.0},
    {'left': 1333, 'bottom': 6, 'width': 129, 'height': 236, 'offset_x': 13.0},
    {'left': 1558, 'bottom': 4, 'width': 101, 'height': 239, 'offset_x': 11.0},
    {'left': 1751, 'bottom': 3, 'width': 111, 'height': 238, 'offset_x': -4.0},
    {'left': 1937, 'bottom': 8, 'width': 149, 'height': 232, 'offset_x': -12.0}
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

def play_idle():
    global running
    for f in IDLE_FRAMES:
        check_events()
        if not running:
            return
        clear_canvas()
        draw_x = CENTER_X + int(f['offset_x'] * SCALE)
        draw_w = int(f['width'] * SCALE)
        draw_h = int(f['height'] * SCALE)
        idle_sheet.clip_draw(f['left'], f['bottom'], f['width'], f['height'], draw_x, CENTER_Y, draw_w, draw_h)
        update_canvas()
        delay(0.08)

def play_walk():
    global running
    for f in WALK_FRAMES:
        check_events()
        if not running:
            return
        clear_canvas()
        draw_x = CENTER_X + int(f['offset_x'] * SCALE)
        draw_w = int(f['width'] * SCALE)
        draw_h = int(f['height'] * SCALE)
        walk_sheet.clip_draw(f['left'], f['bottom'], f['width'], f['height'], draw_x, CENTER_Y, draw_w, draw_h)
        update_canvas()
        delay(0.09)

def play_run():
    global running
    for f in RUN_FRAMES:
        check_events()
        if not running:
            return
        clear_canvas()
        draw_x = CENTER_X + int(f['offset_x'] * SCALE)
        draw_w = int(f['width'] * SCALE)
        draw_h = int(f['height'] * SCALE)
        run_sheet.clip_draw(f['left'], f['bottom'], f['width'], f['height'], draw_x, CENTER_Y, draw_w, draw_h)
        update_canvas()
        delay(0.06)

close_canvas()
