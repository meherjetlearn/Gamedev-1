
import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    x=150
    y=150
    startingcenter= x,y
    #screen.draw.circle(startingcenter,50,(255,0,0))
    r=50

    
    for i in range(5):
        re =randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        screen.draw.filled_circle(startingcenter,r,(re,g,b))

        x-=10
        y-=10
        r-=10
    


pgzrun.go()





    
    



