import pygame
import random
from colours import *
pygame.init()
w = 600
h = 600
cell = 30
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

score = 0
level = 1
FPS = 4
#font for displaying text
font = pygame.font.SysFont("Calibri", 25)
def draw_grid(): #func to draw grid on the screen
    for i in range(h // cell):
        for j in range(w // cell):
            pygame.draw.rect(screen, colorBLACK, (i * cell, j * cell, cell, cell), 1)


class Point: #class to store x, y coord
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake: 
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1 #move in x dir
        self.dy = 0 #move in y dir

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        #head move
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def check_wall_collision(self): #checks if snake hits wall
        head = self.body[0]
        return head.x < 0 or head.x >= w // cell or head.y < 0 or head.y >= h // cell

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorGREEN, ((head.x * cell) + 1, (head.y * cell) + 1, cell - 2, cell - 2))

        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorBLGREEN, ((segment.x * cell) + 1, (segment.y * cell) + 1, cell - 2, cell - 2))

    def check_collision(self, food): #check if snake eats
        global score
        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:
            score += food.current["value"]
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)


class Food:
    def __init__(self):
        self.types = [
            {"color": colorRED, "value": 1, "lifetime": 4000}, #basic
            {"color": colorGREEN, "value": 2, "lifetime": 3000}, #norm
            {"color": colorBLUE, "value": 3, "lifetime": 2000}, #rare
        ]
        self.spawn_time = 0
        self.generate_random_pos([])
    #generate food at random position (not inside snake)
    def generate_random_pos(self, snake_body):
        self.current = random.choices(self.types, weights=[60, 30, 10])[0]
        while True:
            new_x = random.randint(0, w // cell - 1)
            new_y = random.randint(0, h // cell - 1)

            conflict = False
            for segment in snake_body:
                if segment.x == new_x and segment.y == new_y:
                    conflict = True
                    break

            if not conflict:
                self.pos = Point(new_x, new_y)
                self.spawn_time = pygame.time.get_ticks()
                break

    def draw(self):
        pygame.draw.rect(screen, self.current["color"], ((self.pos.x * cell) + 1, (self.pos.y * cell) + 1, cell - 2, cell - 2))
    #check if food expired, time is over
    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.current["lifetime"]


snake = Snake()
food = Food()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBACKGROUND)
    draw_grid()

    snake.move()

    if snake.check_wall_collision():
        print("GAME OVER")
        running = False

    snake.check_collision(food)

    if food.is_expired(): #respawn food if expired
        food.generate_random_pos(snake.body)

    if score != 0:
        level = score // 3 + 1 #update level based on score

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)

    screen.blit(score_text, (20, 10))
    screen.blit(level_text, (20, 30))

    pygame.display.flip()
    clock.tick(FPS + level * 2) #increasing speed

pygame.quit()