import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "connect satilites"

actors = []

for i in range(8):
    satilite = Actor("satilite")
    satilite.pos = random.randint(100,600),random.randint(100,600)
    actors.append(satilite)
def update():
    pass

def draw():
    screen.blit("spacebackgound",(0,0))
    for satilite in actors:
        satilite.draw()
        screen.draw.text(str(actors.index(satilite)+ 1),(satilite.x,satilite.y + 15))

def on_mouse_down(pos):
    pass

pgzrun.go()



