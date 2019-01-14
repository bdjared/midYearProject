from pygame import *
init()

win = display.set_mode((500, 500))

display.set_caption("First Game")

x = 0
y = 0
width = 20
height = 20
vel = 20

run = True
while run:
    time.delay(100)

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()

    if keys[K_LEFT]:
        if x - vel >= 0:
            x -= vel
        else:
            x = 0
        time.delay(100)
    if keys[K_RIGHT]:
        if x + vel <= 480:
            x += vel
        else:
            x = 480
        time.delay(100)
    if keys[K_UP]:
        if y - vel >= 0:
            y -= vel
        else:
            y = 0
        time.delay(100)
    if keys[K_DOWN]:
        if y + vel <= 480:
            y += vel
        else:
            y = 480
        time.delay(100)

    win.fill((0, 0, 0))
    draw.rect(win, (255, 0, 0), (x, y, width, height))
    display.update()

quit()
