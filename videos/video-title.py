import argparse
parser = argparse.ArgumentParser()
parser.add_argument('title')
parser.add_argument('author')
args = parser.parse_args()

import pygame, os
import yaml

pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 220)
title = myfont.render(args.title, False, pygame.Color('black'))
myfont = pygame.font.SysFont('Comic Sans MS', 120)
author = myfont.render(args.author, False, pygame.Color('black'))

for _ in range(8):
    screen.fill(pygame.Color('white'))
    screen.blit(title, (width//2 - title.get_width()//2, 300))
    if author.get_width() > width:
        screen.blit(author, (0, 600))
    else:
        screen.blit(author, (width//2 - author.get_width()//2, 600))
    pygame.display.flip()
    pygame.time.wait(1000)

pygame.quit()
