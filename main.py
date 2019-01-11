from pygame import *
from pygame_textinput import *
init()
textinput = TextInput()
win = display.set_mode((500, 500))
clock = time.Clock()
display.set_caption("Battleship")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    win.fill((255, 255, 255))
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False
    textinput.update(events)
    win.blit(textinput.get_surface(), (10, 10))
    display.update()
    clock.tick(30)
    if textinput.update(events):
        print(textinput.get_text())

quit()
