import pygame
import random

class PGWindow:

    def __init__(self,w,h,frame_updater,event_manager):
        pygame.init() 

        self.screen = pygame.display.set_mode([w,h])

        self.mainloop = True
        
        self.fps = 30
        self.clock = pygame.time.Clock()

        self.frame_updater=frame_updater
        self.event_manager=event_manager
        

    def loop(self):
        # bucle ppal
        while self.mainloop:
            # actualizamos el tiempo
            tick_time = self.clock.tick(self.fps) # milliseconds since last frame

            # funcion de actualizacion
            self.frame_updater(self.screen, self.clock)

            # funcion de gestion de eventos
            for event in pygame.event.get():
                self.mainloop=self.event_manager(event)

            # update del display
            pygame.display.update()

        pygame.quit()        