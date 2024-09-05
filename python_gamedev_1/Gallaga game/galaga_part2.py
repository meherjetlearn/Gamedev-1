import pgzrun
import random

WIDTH = 1200
HEIGHT = 800
#5 
# defining colors for our game
WHITE=(255,255,255)
GREEB=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

#first
ship = Actor('galaga')
#2 specify inital position of ship
ship.x=WIDTH//2
ship.y= HEIGHT-100

#7
#define list for bulltets
bullets=[]

#12
#define enimies
enemies=[]
enemies.append(Actor("bug"))
enemies[-1].x= random.randint(40,WIDTH-40)
enemies[-1].y= -100

#3
def draw():
    screen.clear() #so that we dont see the copy of actors when we move right orleft
    #6
    screen.fill(BLUE)
    ship.draw()
    #9
    for bullet in bullets:
        bullet.draw()
    #13
    for enemy in enemies:
        enemy.draw()

    #16 to overlap and put ship in front of everything 
    #move it over her
    #ship.draw()
    



#11
def on_key_down(key):
    if key== keys.SPACE:
        bullets.append( Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y       

#4
def update():
    if keyboard.left:
        ship.x -=5
    if keyboard.right:
        ship.x +=5
    
         #8 explain the space key but 
         # it will throw continuous bullets 
         # so we will do 11th comment to solve it
    """    if keyboard.space:
        bullets.append( Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y"""

    #15
    for bullet in bullets:
        if bullet.y<-20:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    """
    #10
    for bullet in bullets:
    #to make it continous we will do 15th comment
            bullet.y-=10    """
    
    #14
    for enemy in enemies:
        enemy.y +=10
        if enemy.y > HEIGHT +60:
            enemy.y=-100
            enemy.x = random.randint(40,WIDTH-40)


pgzrun.go()