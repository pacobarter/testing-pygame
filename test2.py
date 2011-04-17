import pygame
import random
import pgwnd

x=25
y=0
color=(32,32,32)
back_color=(255,255,255)

#
#   Actualizacion del frame
#
def update_frame(screen,clock):
    pygame.display.set_caption("press Esc to quit. FPS: %.2f" % (clock.get_fps()))

    fontsize = random.randint(35, 150)
    myFont = pygame.font.SysFont("None", fontsize)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill(back_color)

    screen.blit(myFont.render("I love the pygame cookbook", 0, (color)), (x,y))

#
#   Gestion de eventos
#
def event_manager(event):
    if event.type == pygame.QUIT:
        return False

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return False
            
    else:
        return True


#--------------------------------------------------------------
#       MAIN
#--------------------------------------------------------------
if __name__=='__main__':
    wnd=pgwnd.PGWindow(640,480,update_frame,event_manager)
    wnd.loop()


