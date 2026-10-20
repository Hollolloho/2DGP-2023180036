from pico2d import *


open_canvas(800, 600)
character = load_image('character.png')
grass = load_image('grass.png')

x = 300
y = 200

right = True
up = False
left = False
down = False

while True:
    clear_canvas()
    character.draw(x, y)
    update_canvas()

    if(right):
     x += 2
     if(x >= 600):
        x = 600
        right = False
        up = True
    elif(up):
        y += 2
        if(y >= 400):
            y = 400
            up = False
            left = True
    elif(left):
        x -= 2
        if(x <= 300):
            x = 300
            left = False
            down = True
    elif(down):
        y -= 2
        if(y <= 200):
            y = 200
            down = False
            right = True

    delay(0.01)

close_canvas()