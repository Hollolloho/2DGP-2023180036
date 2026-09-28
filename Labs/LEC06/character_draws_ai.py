from pico2d import *
import math
import os

open_canvas(1200, 800)

# character.png 이미지 로드 및 실패 검사
character = None
if os.path.exists('character.png'):
    try:
        character = load_image('character.png')
    except Exception as e:
        character = None

if character is None:
    print("[Error] character.png 이미지를 로드하는 데 실패했습니다.")
else:
    print("[Success] character.png 이미지를 성공적으로 로드했습니다.")


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    cx, cy, r = 600, 400, 200
    deg = 0
    # deg가 0에서 시작하여 360이 될 때까지 원운동 진행
    # deg=0일 때 위치: (800, 400), deg=360 종료 시 위치: (800, 400)
    while deg < 360:
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_character(x, y)
        deg += 2
    # deg가 360이 되면 원운동을 마치고 다음 함수(사각형 운동)로 전환


def move_rectangle():
    # 원운동 종료 위치인 (800, 400)에서 시작하여 중심(600, 400) 기준 400x400 사각형을 순회
    
    # 1. 우측 변: 위로 이동 (800, 400) -> (800, 600)
    for cur_y in range(400, 600, 2):
        draw_character(800, cur_y)

    # 2. 상단 변: 왼쪽으로 이동 (800, 600) -> (400, 600)
    for cur_x in range(800, 400, -2):
        draw_character(cur_x, 600)

    # 3. 좌측 변: 아래로 이동 (400, 600) -> (400, 200)
    for cur_y in range(600, 200, -2):
        draw_character(400, cur_y)

    # 4. 하단 변: 오른쪽으로 이동 (400, 200) -> (800, 200)
    for cur_x in range(400, 800, 2):
        draw_character(cur_x, 200)

    # 5. 우측 변: 위로 이동하여 원래 위치 복귀 (800, 200) -> (800, 400)
    for cur_y in range(200, 401, 2):
        draw_character(800, cur_y)
        # 사각형을 한 바퀴 다 돌고 시작 위치 (800, 400)에 도달하면 종료하고 삼각형 운동으로 전환
        if cur_y >= 400:
            return



def move_triangle():
    # 사각형 운동 종료 위치인 (800, 400)에서 시작하여 정삼각형 둘레를 회전
    # 한 변의 길이 = 400
    # P1: (800, 400) - 오른쪽 아래 꼭짓점 (사각형 종료 및 처음 원운동 시작 위치)
    # P2: (600, 400 + 200 * math.sqrt(3)) - 상단 꼭짓점 (~746.41)
    # P3: (400, 400) - 왼쪽 아래 꼭짓점
    p1 = (800.0, 400.0)
    p2 = (600.0, 400.0 + 200.0 * math.sqrt(3))
    p3 = (400.0, 400.0)

    steps = 200  # 변당 스텝 수 (부드러운 속도 유지)

    # 1. P1 -> P2: 사각형 끝난 위치에서 '왼쪽 위'로 이동
    for i in range(steps):
        t = i / steps
        x = p1[0] + (p2[0] - p1[0]) * t
        y = p1[1] + (p2[1] - p1[1]) * t
        draw_character(x, y)

    # 2. P2 -> P3: 왼쪽 아래로 이동
    for i in range(steps):
        t = i / steps
        x = p2[0] + (p3[0] - p2[0]) * t
        y = p2[1] + (p3[1] - p2[1]) * t
        draw_character(x, y)

    # 3. P3 -> P1: 오른쪽으로 이동하여 처음 운동 시작 위치인 (800, 400)으로 귀환
    for i in range(steps + 1):
        t = i / steps
        x = p3[0] + (p1[0] - p3[0]) * t
        y = p3[1] + (p1[1] - p3[1]) * t
        draw_character(x, y)
    # 처음 시작 위치(800, 400)에 도달하여 삼각형 운동 종료 -> 원운동으로 자동 전환


# 순차적 실행: 원운동 -> 사각형 운동 -> 삼각형 운동 무한 반복
while True:
    move_circle()      # 1. 원운동 (deg >= 360 도달 시 종료)
    move_rectangle()   # 2. 사각형 운동
    move_triangle()    # 3. 삼각형 운동

close_canvas()
