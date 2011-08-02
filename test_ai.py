# -- coding: utf-8 --
# =============================================================================
#                                                                            
#   test_ai.py                                                              
#   (c) 2011 rjimenez                                                        
#                                                                            
#   Description                                                              
#                                                                            
# ============================================================================= 

import math
import pygame
import ai.sandbox
import ai.objects

MOUSE_BTN_LEFT=1

#
#
class MyAgent(ai.objects.Agent):
    def __init__(self,x,y,angle):
        ai.objects.Agent.__init__(self,x,y,angle)

    # TODO quitar 'target' de la clase base Agent para hacerlo mas generico
    def update(self, target, clock):
        xf=target.x
        yf=target.y
        
        dx=(self.pto.x-xf)**2
        dy=(self.pto.y-yf)**2
        
        if math.sqrt(dx+dy)<1:
            self.set_move(False)
        else:
            self.set_move(True)
        
        if self.move:
            self.pto.x = 0.8*self.pto.x + 0.2 * xf
            self.pto.y = 0.8*self.pto.y + 0.2 * yf

#
#
class SBTest(ai.sandbox.SandBox):
    def __init__(self, w,h, caption,fps):
        ai.sandbox.SandBox.__init__(self,w, h, caption, self.init_all, self.update_frame, self.event_manager, fps)
        
        self.color=(132,32,32)
        self.back_color=(25,25,25)

        self.update=False

        self.target=ai.objects.Target(200,300)
        self.agent=MyAgent(400,100,math.pi/6.0)
        
        self.track=ai.objects.Track()
        self.track.add_point(self.agent.pto)

    #
    #   Inicializacion del Sistema
    #
    def init_all(self, screen):
        self.bg=pygame.Surface(screen.get_size())
        self.bg=self.bg.convert()

    #
    #   Actualizacion del frame
    #
    def update_frame(self, screen, clock):
        
        #   update del status
        #
        if self.update:
            self.agent.update(self.target, clock)
            self.track.add_point(self.agent.pto)
        
        #   redraw de los objetos
        #
        self.bg.fill(self.back_color)
    
        self.target.draw(self.bg)
        self.agent.draw(self.bg)
        self.track.draw(self.bg)
    
        #   actualizacion del screen
        #
        screen.blit(self.bg,(0,0))


    #
    #   Gestion de eventos
    #
    def event_manager(self, lst_event):
        ret=True
    
        for event in lst_event:
            if event.type == pygame.QUIT:
                ret=False
            
            elif event.type == pygame.KEYDOWN:
                ret=self.manage_key_down(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ret=self.manage_mouse_btn_down(event)
            
        return ret

    #       event MOUSE_BTN_DOWN
    #
    def manage_mouse_btn_down(self, event):
        if event.button==MOUSE_BTN_LEFT:
            self.target.set_pos(event.pos)
        
        return True



    #       event KEY DOWN
    #
    def manage_key_down(self, event):
        ret=True
    
        if event.key == pygame.K_ESCAPE:
            ret=False
            
        elif event.key == pygame.K_SPACE:
            self.update=True
        
        return ret



    
###############################################################################    
if __name__=='__main__':
    s=SBTest(800,600, 'Kinematic', 30)
    s.loop()


