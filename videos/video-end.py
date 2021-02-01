import argparse
parser = argparse.ArgumentParser()
parser.add_argument('next')
args = parser.parse_args()

import pygame, os, math
import yaml
os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.init()

questions = '''1. Quais as dificuldades?
2. Como foram superadas?
3. O que aprendeu?'''
questions = questions.split('\n')

info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 120)
questions = [myfont.render(q, False, 'black') for q in questions]
if args.next:
    myfont = pygame.font.SysFont('Comic Sans MS', 80)
    next = myfont.render('Depois: ' + args.next, False, (80, 80, 80))
else:
    next = None
myfont = pygame.font.SysFont('Comic Sans MS', 180)

def str_time(time):
    return '%02d:%02d' % (time/60, time%60)

time = 2*60
while time > 0:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            time = 0
        elif ev.type == pygame.KEYDOWN:
            if ev.unicode == '+':
                time += 30
            elif ev.unicode == '-':
                time -= 30

    screen.fill(pygame.Color('white'))
    for i, q in enumerate(questions):
        screen.blit(q, (width//2 - questions[0].get_width()//2, height//2 - len(questions)*questions[0].get_height()//2 + i*questions[0].get_height()))
    if next:
        screen.blit(next, (80, height - next.get_height()*2))

    time_str = myfont.render(str_time(time), False, 'blue')
    screen.blit(time_str, (width//2 - time_str.get_width()//2, 120))
    pygame.display.flip()
    pygame.time.wait(1000)
    time -= 1

pygame.quit()
