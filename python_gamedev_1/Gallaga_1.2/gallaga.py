import pgzrun
import random
WIDTH=1200
HEIGHT=600
ship=Actor('ship')
ship.x=600
ship.y=550
score=0
gameover=False
bullets=[]
enemys=[]
for i in range (3):
    enemys.append(Actor('bug'))
    enemys[-1].x=random.randint(40,WIDTH-40)
    enemys[-1].y=-100


 


def draw():
    global gameover, score
    screen.clear()
    screen.fill('blue4')
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemys:
        enemy.draw()
    if gameover ==True:
        screen.fill('purple')
        screen.draw.text('Game over',center=(400,300),fontsize=60)
        screen.draw.text(str(score),center=(400,350),fontsize=60)
    if score > 200:
        screen.fill('purple')
        screen.draw.text('You won',center=(400,300),fontsize=60)

    

    


def update():
    global score, gameover
    if keyboard.left:
        ship.x=ship.x-10
    if keyboard.right:
        ship.x=ship.x+10
    for bullet in bullets:
        if bullet.y<-20:
            bullets.remove(bullet)
        else:
            bullet.y=bullet.y-10
    for enemy in enemys:
        enemy.y=enemy.y+random.randint(1,3)
        if enemy.y > HEIGHT +60:
            enemy.y=-100
            enemy.x=random.randint(40,WIDTH-40)
        if enemy.y > 600:
            enemys.remove(enemy)
            gameover=True
        for bullet in bullets:
                if enemy.colliderect(bullet):
                    score=score+100
                    enemys.remove(enemy)
        



def on_key_down(key):
    if key ==keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y














pgzrun.go()
