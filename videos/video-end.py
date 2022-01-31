import argparse
parser = argparse.ArgumentParser()
parser.add_argument('current')
parser.add_argument('next')
args = parser.parse_args()

import pygame, os, math
import yaml

questions = '''Quais as maiores dificuldades?
O que aprendeste?'''
questions = questions.split('\n')

pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 60)
current = myfont.render(args.current, False, pygame.Color('blue'))
myfont = pygame.font.SysFont('Comic Sans MS', 120)
questions = [myfont.render(q, False, pygame.Color('black')) for q in questions]
if args.next:
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    next = myfont.render('Depois: ' + args.next, False, (80, 80, 80))
else:
    next = None
myfont = pygame.font.SysFont('Comic Sans MS', 180)

def str_time(time):
    if time <= 0: return "Time's up!"
    return '%02d:%02d' % (time/60, time%60)

time = 1*60
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
        screen.blit(next, (80, height - next.get_height() - 80))

    time_str = myfont.render(str_time(time), False, pygame.Color('blue'))
    screen.blit(time_str, (width//2 - time_str.get_width()//2, 160))
    screen.blit(current, (width//2 - current.get_width()//2, 80))
    pygame.display.flip()
    pygame.time.wait(1000)
    time -= 1

pygame.quit()
