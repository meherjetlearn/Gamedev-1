import pgzrun
import random
import time
import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 500


score = 0
delay = 0.5
fireballM = False

zuko = Actor("zuko")
zuko.pos = (500,450)
fireball = Actor("fire")
fireball.pos = (-100,-100)
ships = []
gameOver = False
shipDes = 0


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("sounds/sound.wav")
sound.set_volume(0.25)

def createShips():
    num = 0
    for i in range(7):
        temp = Actor("ship")
        ships.append(temp)
        ships[i].pos = (125*num+33,50)
        num = num + 1

createShips()

def fire():
    global fireballM
    fireball.pos = (zuko.x,(zuko.y-5))
    fireballM = True
    sound.play(1)


def draw():
    global gameOver,ships,shipDes,count
    screen.blit("sky",(0,0))
    zuko.draw()
    fireball.draw()
    # time.sleep(delay)
    if fireballM == True:
        fireball.y = fireball.y - 7

    for i in ships:
        i.draw()
        i.y = i.y + random.randint(0,3) - 0.8

    if gameOver:
        screen.clear()
        screen.fill("red")
        screen.draw.text("You Lose",center=(500,250),fontsize=180)
    if shipDes == 7:
        screen.clear()
        screen.fill("green")
        screen.draw.text("You Win",center=(500,250),fontsize=180)
count = -1

def update():
    global gameOver,ships,shipDes,count
    if keyboard.left:
        if zuko.x > 10:
            zuko.x = zuko.x - 10
    elif keyboard.right:
        if zuko.x < 990:
            zuko.x = zuko.x + 10
    elif  keyboard[keys.SPACE]:
        fire()
    for k in ships:
        if k.y > 450:
            gameOver = True
    for l in ships:
        if fireball.colliderect(l):
            ships.remove(l)
            shipDes = shipDes + 1
            fireball.pos = (2000,2000)



pgzrun.go()
pygame.quit()