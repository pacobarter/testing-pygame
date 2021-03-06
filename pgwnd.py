# -*- coding: utf-8 -*-
#

import pygame
import pygame.locals as locals
#import random

class PGWindow:

    def __init__(self, w, h, caption, fn_init, fn_frame_updater, fn_event_manager, fps):
        pygame.init() 

        self.screen = pygame.display.set_mode((w,h), locals.DOUBLEBUF)
        pygame.display.set_caption(caption)

        self.mainloop = True
        
        self.fps = fps
        self.clock = pygame.time.Clock()

        self.frame_updater=fn_frame_updater
        self.event_manager=fn_event_manager
        
        if fn_init:
            fn_init(self.screen)
        

    def loop(self):
        try:
            # bucle ppal
            while self.mainloop:
                # actualizamos el tiempo
                tick_time = self.clock.tick(self.fps) # milliseconds since last frame

                # gestion de eventos
                lst_evt=pygame.event.get()
                self.mainloop=self.event_manager(lst_evt)

                # actualizacion del frame
                self.frame_updater(self.screen, self.clock)

                # update del display
                pygame.display.update()
        
        finally:
            pygame.quit()        