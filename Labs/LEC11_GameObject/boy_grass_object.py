from pico2d import *
import random

frame_width = 100
frame_height = 100

# Game object class here
class Zombie:
    def __init__(self):
        self.x  = random.randint(100, 700)
        self.y  = 90
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')
        self.frame_width = self.image.w // 10
        self.frame_height = self.image.h

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * self.frame_width, 0, self.frame_width, self.frame_height, self.x, self.y, frame_width // 2, frame_height // 2)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass
   

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def reset_world():
    global running
    running = True
    global world
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for boy in range(11)]
    world += team
    zombies = [Zombie() for zombie in range(6)]
    world += zombies

def Update_world():
        for obj in world:
            obj.update()

def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
reset_world()


while running:
    handle_events()
    Update_world()
    render_world()
    delay(0.05)

close_canvas()


#객체 지향 프로그래밍의 과정
# 추상화 원칙을 이용해서 필요한 객체를 추출하고, 객체의 속성과 기능을 결정한다.

# 1. 필요한 객체를 추출한다
# 2. 객체의 속성을 결정한다
# 3. 객체의 행위를 결정한다. (행위란 객체의 상태를 변화시키는 것)
# 4. 객체의 속성과 행위를 합쳐서 클래스를 정의한다.
