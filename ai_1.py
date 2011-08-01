# -*- coding: utf-8 -*-
#

import pygame
import pgwnd
import math

MOUSE_BTN_LEFT=1

#.............................................................................................
#   clase Point
#
class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def set_pos(self, position):
        self.x=position[0]
        self.y=position[1]

#.............................................................................................
#   clase Cross
#
class Cross(Point):
    def __init__(self, x,y, color):
        Point.__init__(self, x,y)

        self.color=color
        
        self.d=10

    def draw(self, surface):
        pygame.draw.line(surface, self.color, (self.x, self.y-self.d), (self.x, self.y+self.d))
        pygame.draw.line(surface, self.color, (self.x-self.d, self.y), (self.x+self.d, self.y))

#.............................................................................................
#   clase Objetivo
#
class Objetivo(Cross):
    def __init__(self, x,y):
        Cross.__init__(self, x,y, (250,0,0))


#.............................................................................................
#   clase Track
#
class Track:
    def __init__(self):
        self.ptos=[]
        self.color=(0,200,0)

    def add_point(self, p):
        self.add(p.x,p.y)

    def add(self, x,y):
        self.ptos.append((x,y))

    def draw(self, surface):
        if len(self.ptos)>1:
            pygame.draw.lines(surface, self.color, False, self.ptos)

#.............................................................................................
#   clase Agente
#
class Agente:
    def __init__(self, x,y, angle):
        self.pto=Point(x,y)
        self.angle=angle
        
        self.d=15
        self.rad=3
        self.color=(0,50,200)
    
        self.move=False
    
    def draw(self, surface):
        p1=(self.pto.x, self.pto.y)
        p2=(self.pto.x + self.d*math.cos(self.angle), self.pto.y + self.d*math.sin(self.angle))
        
        pygame.draw.line(surface, self.color,p1,p2)
        pygame.draw.circle(surface, self.color, p1, self.rad)
    
    def set_move(self, move):
        self.move=move

    def swap_move(self):
        self.set_move(not self.move)
    
    def update(self, objetivo, clock):
        xf=objetivo.x
        yf=objetivo.y
        
        dx=(self.pto.x-xf)**2
        dy=(self.pto.y-yf)**2
        
        if math.sqrt(dx+dy)<1:
            self.set_move(False)
        else:
            self.set_move(True)
        
        if self.move:
            self.pto.x = 0.8*self.pto.x + 0.2 * xf
            self.pto.y = 0.8*self.pto.y + 0.2 * yf

#.............................................................................................
#   clase SandBox (dibuja en pantalla y gestiona eventos)
#
class SandBox:

    def __init__(self):
        self.color=(132,32,32)
        self.back_color=(25,25,25)

        self.update=False

        self.objetivo=Objetivo(200,300)
        self.agent=Agente(400,100,math.pi/6.0)
        
        self.track=Track()
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
            self.agent.update(self.objetivo, clock)
            self.track.add_point(self.agent.pto)
        
        #   redraw de los objetos
        #
        self.bg.fill(self.back_color)
    
        self.objetivo.draw(self.bg)
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
            self.objetivo.set_pos(event.pos)
        
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


#--------------------------------------------------------------
#       MAIN
#--------------------------------------------------------------
if __name__=='__main__':
    print 'Using pygame version:', pygame.ver

    s=SandBox()

    wnd=pgwnd.PGWindow(800,600, 'Kinematic', s.init_all, s.update_frame, s.event_manager, 30)
    wnd.loop()


