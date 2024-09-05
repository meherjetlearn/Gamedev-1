import pgzrun

WIDTH = 1200
HEIGHT = 800
#first
ship = Actor('galaga')
#2
ship.x=WIDTH//2
ship.y= HEIGHT-100
#3
def draw():
    screen.clear() #so that we dont see the copy of actors when we move right orleft
    ship.draw()


def update():
    if keyboard.left:
        ship.x -=5
    if keyboard.right:
        ship.x +=5



pgzrun.go()