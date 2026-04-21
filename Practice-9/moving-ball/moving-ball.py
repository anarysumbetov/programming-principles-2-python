import pygame
pygame.init()
w = 1200
h = 600
screen = pygame.display.set_mode((w, h))
done = False

clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
x = w // 2
y = h // 2
r = 25
step = 20

while not done:
    keys = pygame.key.get_pressed()
    pygame.draw.circle(screen, red, (x, y), r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if keys[pygame.K_UP]:
        if(y-step-r>=0):
            y-=step
    if keys[pygame.K_DOWN]:
        if(y+step+r<=h):
            y+=step
    if keys[pygame.K_LEFT]:
        if(x-step-r>=0):
            x-=step
    if keys[pygame.K_RIGHT]:
        if(x+step+r<=w):
            x+=step
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()