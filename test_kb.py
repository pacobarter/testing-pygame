# -*- coding: utf-8 -*-
#

import pygame
import pygame.locals as ctes
import sys

pygame.init()

screen=pygame.display.set_mode((800,600),0,32)
img=pygame.image.load('img.jpg').convert()

x,y = 0,0
movx,movy = 0,0

while True:

    for evt in pygame.event.get():
        if evt.type==ctes.QUIT:
            sys.exit()
            
        if evt.type==ctes.KEYDOWN:
            if evt.key==ctes.K_j:
                movx-=1
            elif evt.key==ctes.K_l:
                movx+=1
            elif evt.key==ctes.K_i:
                movy-=1
            elif evt.key==ctes.K_m:
                movy+=1
        
        elif evt.type==ctes.KEYUP:
            if evt.key==ctes.K_j:
                movx=0
            elif evt.key==ctes.K_l:
                movx=0
            elif evt.key==ctes.K_i:
                movy=0
            elif evt.key==ctes.K_m:
                movy=0
            

    x+=movx
    y+=movy
    
    screen.fill((0,0,0))
    screen.blit(img,(x,y))


    pygame.display.update()
