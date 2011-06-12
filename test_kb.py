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

funcs={
    ctes.KEYDOWN : {
        ctes.K_j : lambda mx,my: (mx-1,my),
        ctes.K_l : lambda mx,my: (mx+1,my),
        ctes.K_i : lambda mx,my: (mx,my-1),
        ctes.K_m : lambda mx,my: (mx,my+1)
    },
    
    ctes.KEYUP : {
        ctes.K_j : lambda mx,my: (0,my),
        ctes.K_l : lambda mx,my: (0,my),
        ctes.K_i : lambda mx,my: (mx,0),
        ctes.K_m : lambda mx,my: (mx,0)
    }
}

while True:

    for evt in pygame.event.get():
        if evt.type==ctes.QUIT:
            sys.exit()
        
        try:
            movx,movy = funcs[evt.type][evt.key](movx,movy)
        except:
            movx,movy = 0,0

    x+=movx
    y+=movy
    
    screen.fill((0,0,0))
    screen.blit(img,(x,y))


    pygame.display.update()
