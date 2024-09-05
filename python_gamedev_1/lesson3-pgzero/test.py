import pgzrun
WIDTH=800
HEIGHT=800
def draw():
    corner1=(0,0)
    
    r=120
    g=120
    b=120
    width=WIDTH-400
    height=HEIGHT-400
    corner2=(width-50,height-50)
    rect = Rect(corner1, corner2)
    
    screen.draw.rect(rect, (r, g, b))
    screen.draw.circle((300,300),50,(r,g,b))
pgzrun.go()

""""import pgzrun
from random import randint
WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))
    corner1=(0,0)
    
    width = WIDTH
    height = HEIGHT - 200
    for i in range(15):
        rect = Rect(corner1, (width,height))
        rect.center=150,150
        r = 255
        g = 0
        b = randint(120, 255)
        screen.draw.rect(rect, (r,g,b))

        r -= 2
        g += 5

        width -= 10
        height += 10

pgzrun.go()

"""