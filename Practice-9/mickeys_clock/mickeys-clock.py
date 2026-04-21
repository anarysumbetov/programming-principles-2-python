import pygame
from datetime import datetime, timezone
pygame.init()
screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()

clockpng = pygame.image.load("images/clock.PNG")
rhand = pygame.image.load("images/lefthand.PNG")
lhand = pygame.image.load("images/righthand.png")

center = (1280//2, 960//2)

running = True
while running:
    now = datetime.now()
    minutes = now.minute + 8
    sec = now.second
    min_ang = minutes * 6
    sec_ang = sec * 6
    min_rot = pygame.transform.rotate(rhand, -min_ang)
    sec_rot = pygame.transform.rotate(lhand, -sec_ang)
    min_cent = min_rot.get_rect(center=center)
    sec_cent = sec_rot.get_rect(center=center)

    screen.blit(clockpng, (0, 0))
    screen.blit(min_rot, min_cent)
    screen.blit(sec_rot, sec_cent)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(1)
pygame.quit()