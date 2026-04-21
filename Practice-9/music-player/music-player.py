import pygame
import os
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 200))
font = pygame.font.SysFont("Arial", 30)

playlist = ["songs/Toby_Fox_-_Nyeh_Heh_Heh_Bonetrousle.mp3", "songs/Toby_Fox_-_Undertale_-_Another_Medium.mp3", "songs/Undertale_-_Asgore.mp3", "songs/Toby_Fox-065-CORE.mp3"]

current = 0
playing = False
start = 0

def load_track(curr):
    pygame.mixer.music.load(playlist[curr])

def play():
    global playing, start
    pygame.mixer.music.play()
    playing = True
    start = time.time()

def stop():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_track():
    global current
    current = (current + 1) % len(playlist)
    load_track(current)
    play()

def prev_track():
    global current
    current = (current - 1) % len(playlist)
    load_track(current)
    play()

def get_name():
    return os.path.basename(playlist[current])

def draw_ui():
    screen.fill((30, 30, 30))

    track_text = font.render("Track: " + get_name(), True, (255, 255, 255))
    screen.blit(track_text, (20, 20))

    status_text = font.render("Playing" if playing else "Stopped", True, (150, 150, 150))
    screen.blit(status_text, (20, 60))

    if playing:
        elapsed = int(time.time() - start)
        time_text = font.render(f"Time: {elapsed} seconds", True, (150, 150, 150))
        screen.blit(time_text, (20, 100))

    pygame.display.flip()

load_track(current)

running = True
while running:
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_q:
                running = False
pygame.quit()