# -*- coding: utf-8 -*-
#

import pygame
import pygame.locals as locals
import sys
import threading
import time

class LinePrinter(threading.Thread):
    def __init__(self,msg):
        super(LinePrinter,self).__init__()
        
        self.msg=msg
        self.idx=0

    def run(self):
        while self.idx<len(self.msg)-1:
            self.idx+=1
            time.sleep(0.01)
            
    def __str__(self):
        return self.msg[:self.idx]

#
#   MAIN
#
if __name__=='__main__':

    pygame.init()

    try:
        screen_size=(800,600)
        screen=pygame.display.set_mode(screen_size,0,32)

        font=pygame.font.SysFont('Courier New', 12)
        font_height=font.get_linesize()

        events_txt=[]

        while True:
        
            event_lst=pygame.event.get()

            for evt in event_lst:
                if evt.type==locals.QUIT:
                    sys.exit()

        #        events_txt.append(str(event))
                lp=LinePrinter(str(evt))
                lp.start()
            
                events_txt.append(lp)
                events_txt=events_txt[-screen_size[1]/font_height:]

            screen.fill((0,0,0))
        
            y=screen_size[1]-font_height
            for txt in reversed(events_txt):
                screen.blit(font.render(str(txt),True,(0,210,0)),(0,y))
                y-=font_height
                
            pygame.display.update()

    except:
        pygame.quit()


