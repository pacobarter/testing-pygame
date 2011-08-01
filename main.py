# -*- coding: utf-8 -*-
#

import pygame
import random
import pgwnd

x=25
y=0
color=(32,32,32)
back_color=(25,25,25)

#
#   Actualizacion del frame
#
def update_frame(screen,clock):
#    pygame.display.set_caption("press Esc to quit. FPS: %.2f" % (clock.get_fps()))

    fontsize = random.randint(35, 150)
    myFont = pygame.font.SysFont("None", fontsize)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill(back_color)

    screen.blit(myFont.render("I love the pygame cookbook", 0, (color)), (x,y))

#
#   Gestion de eventos
#
def event_manager(lst_event):
    ret=True
    
    for event in lst_event:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            ret=False
            
    return ret


#--------------------------------------------------------------
#       MAIN
#--------------------------------------------------------------
if __name__=='__main__':
    print 'Using pygame version:', pygame.ver

    wnd=pgwnd.PGWindow(640,480, 'Test', None, update_frame, event_manager, 30)
    wnd.loop()


