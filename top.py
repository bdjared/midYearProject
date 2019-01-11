from pygame import *
init()

win = display.set_mode((500, 500))

display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    time.delay(100)

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()

    if keys[K_LEFT]:
        x -= vel
    if keys[K_RIGHT]:
        x += vel
    if keys[K_UP]:
        y -= vel
    if keys[K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    draw.rect(win, (255, 0, 0), (x, y, width, height))
    display.update()


quit()
