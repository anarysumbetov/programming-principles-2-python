import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

radius = 5
color = (255, 0, 0)
mode = "draw"  # draw, rect, circle, erase (by def - draw)

drawing = False
start_pos = None

screen.fill((255, 255, 255)) 

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
                print("COLOR CHANGED TO RED")
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
                print("COLOR CHANGED TO GREEN")
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
                print("COLOR CHANGED BLUE")
            elif event.key == pygame.K_d:
                color = (0, 0, 0)
                print("COLOR CHANGED TO BLACK")

            elif event.key == pygame.K_1:
                mode = "draw"
                print("MODE CHANGED TO DRAW")
            elif event.key == pygame.K_2:
                mode = "rect"
                print("MODE CHANGED TO RECT")
            elif event.key == pygame.K_3:
                mode = "circle"
                print("MODE CHANGED TO CIRCLE")
            elif event.key == pygame.K_4:
                mode = "square"
                print("MODE CHANGED TO SQUARE")
            elif event.key == pygame.K_5:
                mode = "right_tr"
                print("MODE CHANGED TO RIGHT TRIANGLE")
            elif event.key == pygame.K_6:
                mode = "eq_tr"
                print("MODE CHANGED TO EQUILATERAL TRIANGLE")
            elif event.key == pygame.K_7:
                mode = "rhombus"
                print("MODE CHANGED TO RHOMBUS")
            elif event.key == pygame.K_e:
                mode = "erase"
                print("MODE CHANGED TO ERASE")

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, 4)

            elif mode == "circle":
                end_pos = event.pos
                radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius_circle, 4)
            elif mode == "square":
                end_pos = event.pos
                x = end_pos[0]-start_pos[0]
                y = end_pos[1] - start_pos[1]
                ss = min(abs(x), abs(y))
                square = pygame.Rect(start_pos, (ss, ss))
                pygame.draw.rect(screen, color, square, 4)
            elif mode == "right_tr":
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                points = [(x1, y1),(x2, y1), (x1, y2)]
                pygame.draw.polygon(screen, color, points, 4)
            elif mode == "eq_tr":
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                side = ((x2 - x1)**2 + (y2-y1)**2) ** 0.5
                h = (3**0.5 / 2) * side
                s1 = (x1, y1)
                s2 = (x1 + side, y1)
                s3 = (x1 + side/2, y1-h)
                pygame.draw.polygon(screen, color, [s1, s2, s3], 4)
            elif mode == "rhombus":
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                center_x = (x1 + x2)//2
                center_y = (y1 + y2)//2
                w1 = abs(x2 - x1)//2
                w2 = abs(y2 - y1)//2
                points = [(center_x, center_y - w2), (center_x + w1, center_y), (center_x, center_y + w2), (center_x - w1, center_y)]
                pygame.draw.polygon(screen, color, points, 4)
        if event.type == pygame.MOUSEMOTION and drawing:

            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, radius)

            elif mode == "erase":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, radius * 5)

    pygame.display.flip()
    clock.tick(60)