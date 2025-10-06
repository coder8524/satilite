import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 600
TITLE = "connect satilites"

actors = []

start = time.time()
total_time = 0
game_complete = False

lines = []

target = 0 

for i in range(8):
    satilite = Actor("satilite")
    satilite.pos = random.randint(100,600),random.randint(100,600)
    actors.append(satilite)
def update():
    pass

def draw():
    global game_complete,total_time
    screen.blit("spacebackgound",(0,0))
    for satilite in actors:
        satilite.draw()
        screen.draw.text(str(actors.index(satilite)+ 1),(satilite.x,satilite.y + 15))

    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if game_complete == False:
        total_time = time.time() - start
    if target == 8: game_complete = True
    screen.draw.text(str(total_time),(20,20))
def on_mouse_down(pos):
    global target,lines
    if actors[target].collidepoint(pos):
        if target > 0:
            lines.append((actors[target-1].pos,actors[target].pos))
        target = target + 1
    else:
        target = 0
        lines.clear()




pgzrun.go()



