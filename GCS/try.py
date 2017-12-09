#import randomm
import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load('FLAG.png'))
    caption = 'Simulation'
    pygame.display.set_caption(caption, 'Spine Runtime')
    pygame.display.set_mode((350,300), DOUBLEBUF|OPENGL)
    
main()


verticies = [
    [0,0, 0],
    [0 ,0, 0],
    [0 ,0, 0],
    [0 ,0 ,0]
    ]

#x1=np.cos()



edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),#3,0
    (3,1)
    )

colors = (
    (1,0,0),
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )


plane_surface=(
    (0,1,2,3)
    )

img = pygame.image.load('di (2).bmp')
#pygame.display.set_caption('Simulation' , iconyfied_title=None) 
textureData = pygame.image.tostring(img, "RGB", 1)
width = img.get_width()
height = img.get_height()

im = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, im)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
glEnable(GL_TEXTURE_2D)
gluPerspective(45, 1, 0.1, 50)

glTranslatef(0,0,-10)


def wall():
    glColor3fv(colors[4])
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex2f(-4,-4)
    glTexCoord2f(0,1)
    glVertex2f(-4,4)
    glTexCoord2f(1,1)
    glVertex2f(4,4)
    glTexCoord2f(1,0)
    glVertex2f(4,-4)
    glEnd()


def glider(d):
    global verticies
    
    x1=2*np.cos((np.pi*330/180)+d)
    y1=2*np.sin((np.pi*330/180)+d)
    
    x2=2*np.cos((np.pi/2)+d)
    y2=2*np.sin((np.pi/2)+d)
    
    x3=2*np.cos((np.pi*210/180)+d)
    y3=2*np.sin((np.pi*210/180)+d)
    
    verticies[0][0]=x1
    verticies[0][1]=y1
    verticies[1][0]=x2
    
    verticies[1][1]=y2
    
    verticies[2][0]=x3
    verticies[2][1]=y3
    glColor3fv(colors[0])
    glBegin(GL_QUADS)
    for surface in plane_surface:
        glVertex3fv(verticies[surface])
    glEnd()
    
    glColor3fv(colors[1])
    

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
   
    glEnd()
    
degree=0
h=1.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    wall()
    glider(degree)
    #degree=random.randint(1,6)
    degree=degree+0.261
    if degree>6.28:
        degree=0
        
        
    
    
    pygame.display.flip()
    pygame.time.wait(50)
