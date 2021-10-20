import pygame
import time
from pygame import *

pygame.init()
clock = time.Clock()


screenw,screenh = display.Info().current_w,display.Info().current_h



window = display.set_mode((screenw,screenh))
bg = image.load('images/bg.png').convert_alpha()
background = transform.scale(bg,(screenw,screenh))


class locations(object):
    border = image.load('images/thumbnails/border.png').convert_alpha()
    locimgs = [transform.scale(border,(round(screenw/1920*(border.get_width())),round(screenh/1080*(border.get_height()))))]
    for x in range(1,21):
        img = (image.load('images/thumbnails/'+str(x)+'.png'))
        locimgs.append(transform.scale(img,(round(screenw/1920*220),round(screenh/1080*135))))
    tabimgs = [image.load('images/extra tab/base.png'),image.load('images/extra tab/img1.png'),image.load('images/extra tab/img2.png'),image.load('images/extra tab/img3.png'),image.load('images/extra tab/img4.png'),
               image.load('images/extra tab/1.png'),image.load('images/extra tab/2.png'),image.load('images/extra tab/3.png'),image.load('images/extra tab/4.png'),
               image.load('images/extra tab/5.png'),image.load('images/extra tab/6.png'),image.load('images/extra tab/7.png'),image.load('images/extra tab/8.png'),
               image.load('images/extra tab/9.png'),image.load('images/extra tab/10.png'),]
    tabslist = []
    for x in range(0,15):
        tabslist.append((transform.scale(tabimgs[x],(round(screenw/1920*(tabimgs[x].get_width())),round(screenh/1080*(tabimgs[x].get_height()))))))

    def __init__(self):
        self.pointpos = [(screenw/1920*653,screenh/1080*481),(screenw/1920*705,screenh/1080*444),(screenw/1920*758,screenh/1080*409),(screenw/1920*809,screenh/1080*377),
                         (screenw/1920*864,screenh/1080*348),(screenw/1920*914,screenh/1080*323),(screenw/1920*969,screenh/1080*305),(screenw/1920*1031,screenh/1080*295),(screenw/1920*1095,screenh/1080*289),(screenw/1920*1156,screenh/1080*297),
                          (screenw/1920*1216,screenh/1080*311),(screenw/1920*1277,screenh/1080*335),(screenw/1920*1337,screenh/1080*366),(screenw/1920*1392,screenh/1080*396),(screenw/1920*1443,screenh/1080*430),(screenw/1920*1490,screenh/1080*464),
                         (screenw/1920*1541,screenh/1080*504),(screenw/1920*1593,screenh/1080*545),(screenw/1920*1647,screenh/1080*586),(screenw/1920*1700,screenh/1080*624)]
        self.tabopen = False
        self.count = 0
        self.flashc = 0
        self.change = 1
        self.timeimage = 0
        self.timehitbox = [(screenw/1920*220,screenh/1080*70),(screenw/1920*560,screenh/1080*70),(screenw/1920*910,screenh/1080*70),(screenw/1920*1220,screenh/1080*70)]
        
    def draw(self):
        if not self.tabopen:
            for x in range (0,20):

                if mosx >= self.pointpos[x][0] and mosx <= self.pointpos[x][0]+screenw/1920*20 and mosy >= self.pointpos[x][1] and mosy <= self.pointpos[x][1]+screenh/1080*20:
                    window.blit(self.locimgs[0],(self.pointpos[x][0]-screenw/1920*118,self.pointpos[x][1]-screenh/1080*227))
                    window.blit(self.locimgs[x+1],(self.pointpos[x][0]-screenw/1920*100,self.pointpos[x][1]-screenh/1080*210))
                    if x == 10 and mouse.get_pressed()[0] == True:
                            self.tabopen = True
        else: 
            window.blit(self.tabslist[0],(0,0))
            if self.count != 3:
                self.count+=1
            else:
                self.count = 0
                if self.flashc == 9:
                    self.change = -1
                elif self.flashc == 0:
                    self.change = 1
                self.flashc += self.change
            window.blit(self.tabslist[5+self.flashc],(screenw/1920*1500,screenh/1080*250))
            window.blit(self.tabslist[1+self.timeimage],(0,0))
            
            for x in range(0,4):
                if mosx >= self.timehitbox[x][0] and mosx <= self.timehitbox[x][0]+screenw/1920*100 and mosy >= self.timehitbox[x][1] and mosy <= self.timehitbox[x][1]+screenh/1080*30 and mouse.get_pressed()[0]:
                    self.timeimage = x
                
    
def redraw():
    global mosy,mosx
    window.blit(background,(0,0))
    loc.draw()


#######################################
loc = locations()


fps = 25
run = True

while run:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys[K_ESCAPE]:
            run = False

    (mosx,mosy) = mouse.get_pos()

    redraw()
    display.update()
    clock.tick(fps)
    
quit()
