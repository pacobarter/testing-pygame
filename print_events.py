# -*- coding: utf-8 -*-
#

import pygame
import pygame.locals as locals
import sys



if __name__=='__main__':

    pygame.init()

    screen_size=(800,600)
    screen=pygame.display.set_mode(screen_size,0,32)

    font=pygame.font.SysFont('Courier New', 12)
    font_height=font.get_linesize()

    events_txt=[]

    while True:
    
        event=pygame.event.wait()
        
        events_txt.append(str(event))
        events_txt=events_txt[-screen_size[1]/font_height:]

        if event.type==locals.QUIT:
            sys.exit()

        screen.fill((0,0,0))
        
        y=screen_size[1]-font_height
        for txt in reversed(events_txt):
            screen.blit(font.render(txt,True,(0,250,0)),(0,y))
            y-=font_height
            
        pygame.display.update()
