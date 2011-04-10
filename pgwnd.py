import pygame
import random

class PGWindow:

    def __init__(self,w,h):
        pygame.init() 

        self.screen = pygame.display.set_mode([w,h])
        self.screen.fill([255,255,255])

        self.mainloop = True
        self.x = 25
        self.y = 0
        self.color = (32,32,32)
        self.fontsize = 1
        self.delta = 0
        self.fps = 30
        self.clock = pygame.time.Clock()


    def loop(self):
        while self.mainloop:
            tick_time = self.clock.tick(self.fps) # milliseconds since last frame

            pygame.display.set_caption("press Esc to quit. FPS: %.2f" % (self.clock.get_fps()))

            self.fontsize = random.randint(35, 150)
            myFont = pygame.font.SysFont("None", self.fontsize)
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

            self.screen.fill((255,255,255))

            self.screen.blit(myFont.render("I love the pygame cookbook", 0, (self.color)), (self.x,self.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mainloop = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.mainloop = False

            pygame.display.update()

        pygame.quit()        